"""
Simple Catastrophe Risk Analysis
--------------------------------
Author: Kenneth Otárola
"""


import arcpy
import heapq
import ast
import csv
import re
import os
import numpy as np
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
from operator import itemgetter
from datetime import datetime


# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------


#
# Core helpers
#


def ensure_field(feature_class: str, field_name: str, field_type: str = "DOUBLE"):
    """Add field if it doesn't exist (case-sensitive check for names)"""
    # 1) Attempt to add field; ignore if it already exists
    existing_names = {f.name for f in arcpy.ListFields(feature_class)}
    if field_name not in existing_names:
        arcpy.management.AddField(feature_class, field_name, field_type)


def find_field(fc, target_name):
    """Find a field by name/alias; returns actual field name or None"""
    # 1) Exact name match (case-insensitive)
    t = target_name.lower()
    fields = arcpy.ListFields(fc)
    for f in fields:
        if f.name.lower() == t:
            return f.name
        
    # 2) Suffix-based match (_target or .target)
    for f in fields:
        ln = f.name.lower()
        if ln.endswith("_" + t) or ln.endswith("." + t):
            return f.name

    # 3) Alias match (case-insensitive)
    for f in fields:
        if f.aliasName and f.aliasName.lower() == t:
            return f.name
        
    # 4) Not found
    return None


def parse_TR_from_name(base_name):
    """Extract the last integer sequence from name (e.g., return period)"""
    # 1) Extract last integer sequence from base name (e.g., TR)
    nums = re.findall(r'(\d+)', base_name)
    return int(nums[-1]) if nums else None


def get_endpoints(geom: arcpy.Geometry):
    """First and last point of a polyline, rounded for stable node keys"""
    # 1) Obtain first and last points of a polyline geometry
    first = geom.firstPoint
    last = geom.lastPoint

    # 2) Round coordinates to 3 decimals for stable node keys
    return (round(first.X, 3), round(first.Y, 3)), (round(last.X, 3), round(last.Y, 3))


def create_consolidated_copy(src_fc, out_gdb, out_name):
    """Copy a feature class to the output GDB; returns output path or None"""
    # 1) Guard on empty source
    if not src_fc:
        return None

    # 2) Build target path and recreate feature class
    out_fc = os.path.join(out_gdb, arcpy.ValidateTableName(out_name, out_gdb))
    if arcpy.Exists(out_fc):
        arcpy.management.Delete(out_fc)
    arcpy.management.CopyFeatures(src_fc, out_fc)

    # 3) Return consolidated path
    return out_fc


#
# Raster sampling
#


def sample_raster_to_points(points_fc, raster_path, out_fc, value_field="RASTERVALU"):
    """Copy points_fc to out_fc and attach raster sample values into value_field"""
    # 1) Prepare output feature class as a copy
    if arcpy.Exists(out_fc):
        arcpy.management.Delete(out_fc)
    arcpy.management.CopyFeatures(points_fc, out_fc)

    # 2) Describe raster & extract numeric array 
    desc = arcpy.Describe(raster_path)
    ext  = desc.Extent
    px_w = abs(desc.meanCellWidth)
    px_h = abs(desc.meanCellHeight)
    ras = arcpy.Raster(raster_path)
    arr = arcpy.RasterToNumPyArray(ras)
    arr = arr.astype("float64", copy=False)
    ndv = getattr(ras, "noDataValue", None)
    if ndv is not None:
        try:
            arr[arr == float(ndv)] = np.nan
        except Exception:
            pass
    nrows, ncols = arr.shape

    # 3) Feature coordinates & compute raster indices
    oid_name = arcpy.Describe(out_fc).OIDFieldName
    recs = arcpy.da.FeatureClassToNumPyArray(out_fc, [oid_name, "SHAPE@XY"])
    oids = recs[oid_name].astype("int32")
    xs   = recs["SHAPE@XY"][:, 0]
    ys   = recs["SHAPE@XY"][:, 1]
    cols = np.floor((xs - ext.XMin) / px_w).astype(int)
    rows = np.floor((ext.YMax - ys) / px_h).astype(int)
    valid = (cols >= 0) & (cols < ncols) & (rows >= 0) & (rows < nrows)

    # 4) Sample values and attach as a new field
    vals = np.full(xs.shape, np.nan, dtype="float64")
    if valid.any():
        vals[valid] = arr[rows[valid], cols[valid]]
    ensure_field(out_fc, value_field, "DOUBLE")
    out_arr = np.empty(oids.size, dtype=[("JOIN_ID", "i4"), (value_field, "f8")])
    out_arr["JOIN_ID"]   = oids
    out_arr[value_field] = vals
    arcpy.da.ExtendTable(out_fc, oid_name, out_arr, "JOIN_ID", append_only=False)

    # 5) Return the fc values needed
    return out_fc


def add_raster_field(target_fc, raster_path, value_field="LQ_VAL"):
    """Attach raster sample values into target_fc directly (deletes value_field)"""
    # 1) Describe raster & convert to NumPy (handle NoData)
    desc = arcpy.Describe(raster_path)
    ext  = desc.Extent
    px_w = abs(desc.meanCellWidth)
    px_h = abs(desc.meanCellHeight)
    ras = arcpy.Raster(raster_path)
    arr = arcpy.RasterToNumPyArray(ras)
    arr = arr.astype("float64", copy=False)
    ndv = getattr(ras, "noDataValue", None)
    if ndv is not None:
        try:
            arr[arr == float(ndv)] = np.nan
        except Exception:
            pass
    nrows, ncols = arr.shape

    # 2) Read target feature coords & compute raster indices
    oid_name = arcpy.Describe(target_fc).OIDFieldName
    recs = arcpy.da.FeatureClassToNumPyArray(target_fc, [oid_name, "SHAPE@XY"])
    oids = recs[oid_name].astype("int32")
    xs   = recs["SHAPE@XY"][:, 0]
    ys   = recs["SHAPE@XY"][:, 1]
    cols  = np.floor((xs - ext.XMin) / px_w).astype(int)
    rows  = np.floor((ext.YMax - ys) / px_h).astype(int)
    valid = (cols >= 0) & (cols < ncols) & (rows >= 0) & (rows < nrows)

    # 3) Sample values and attach as a new field
    vals = np.full(xs.shape, np.nan, dtype="float64")
    if valid.any():
        vals[valid] = arr[rows[valid], cols[valid]]
    ensure_field(target_fc, value_field, "DOUBLE")
    out_arr = np.empty(oids.size, dtype=[("JOIN_ID", "i4"), (value_field, "f8")])
    out_arr["JOIN_ID"] = oids
    out_arr[value_field] = vals
    arcpy.da.ExtendTable(target_fc, oid_name, out_arr, "JOIN_ID", append_only=False)


def liquefaction_once(target_fc, liquefa_path, value_field="LQ_VAL"):
    """Attach liquefaction raster values once (only if field doesn't already exist)."""
    # 1) Validate inputs and short-circuit if already present
    if not liquefa_path or not arcpy.Exists(target_fc):
        return
    if any(f.name.upper() == value_field.upper() for f in arcpy.ListFields(target_fc)):
        return

    # 2) Attach liquefaction raster value once
    add_raster_field(target_fc, liquefa_path, value_field=value_field)


#
# Vulnerability database
#


def read_vul_db(csv_path):
    """Parse vulnerability CSV lines formatted as: taxonomy, [xs], [ys]"""
    # 1) Initialize output and compile parsing regex
    vul_db = {}
    pat = re.compile(r'^\s*([^,]+)\s*,\s*(\[[^\]]*\])\s*,\s*(\[[^\]]*\])')

    # 2) Iterate lines, skip headers/empties, parse lists
    with open(csv_path, "r", encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.lower().startswith("taxonomy"):
                continue
            m = pat.match(line)
            if not m:
                continue
            key, xs_str, ys_str = m.groups()
            try:
                xs = list(map(float, ast.literal_eval(xs_str)))
                ys = list(map(float, ast.literal_eval(ys_str)))
                pairs = sorted(zip(xs, ys), key=lambda p: p[0])
                xs_sorted, ys_sorted = zip(*pairs)
                vul_db[key.strip()] = (list(xs_sorted), list(ys_sorted))
            except Exception:
                continue

    # 3) Return the vulnerability database
    return vul_db


def build_vul_key(source, hazard_type, rid=None, vkey=None, lq=None, curve_type="RMD"):
    """Build vulnerability key based on hazard family + curve type + LQ bin + taxonomy"""
    # 1) Normalize hazard and determine prefix via LQ
    hz = (hazard_type or "").strip().lower()
    family = (curve_type or "RMD").strip().upper()

    # 2) Use the correct vulnerability function
    if hz == "earthquake":
        try:
            v_float = float(lq) if lq is not None else float("nan")
            if not np.isfinite(v_float):
                raise ValueError
            v = int(round(v_float))
        except Exception:
            v = None
        if v in (1, 2):
            lq_tag = "LQ1_"
        elif v == 3:
            lq_tag = "LQ2_"
        elif v == 4:
            lq_tag = "LQ3_"
        elif v == 5:
            lq_tag = "LQ4_"
        else:
            lq_tag = ""
        prefix = f"EQ_{family}_{lq_tag}"
        raw_vkey = (source["road_vulEQ"].get(rid) if (source and rid is not None) else vkey)
    else:
        prefix = f"FL_{family}_"
        raw_vkey = (source["road_vulFL"].get(rid) if (source and rid is not None) else vkey)

    # 3) Clean raw key and build the final key
    raw_vkey = raw_vkey.strip() if isinstance(raw_vkey, str) else raw_vkey
    return f"{prefix}{raw_vkey}" if raw_vkey else None


#
# Geometry processing
#


def road_geometry(roads_path, road_segme):
    """Generate reusable points along roads and compute tributary length per point"""
    # 1) Sample points every road_segme metres
    pts = r"in_memory\pts"
    if arcpy.Exists(pts):
        arcpy.management.Delete(pts)
    arcpy.management.GeneratePointsAlongLines(roads_path, pts, Distance=f"{road_segme} Meters", Include_End_Points="END_POINTS")

    # 2) Cache road geometry & lengths estimation
    desc = arcpy.Describe(roads_path)
    oid_name = desc.OIDFieldName
    sr = desc.spatialReference
    id_tramo_name = find_field(roads_path, "ID_TRAMO")
    if not id_tramo_name:
        raise RuntimeError("ID_TRAMO field not found on roads_path.")
    road_vulFL, road_vulEQ, road_geom, road_len_m, road_cost_m, road_len_native, oid_to_tramo = {}, {}, {}, {}, {}, {}, {}
    with arcpy.da.SearchCursor(roads_path, [oid_name, "SHAPE@", "vul_f", "vul_eq", "rep_cost_k", id_tramo_name]) as cur:
        for oid, geom, vkeyf, vkeye, repk_val, tramo in cur:
            road_geom[oid] = geom
            native_len = geom.length
            road_len_native[oid] = native_len
            if sr.type == "Projected" and sr.linearUnitName:
                length_m = native_len * sr.metersPerUnit
            elif sr.type == "Geographic":
                length_m = geom.getLength("GEODESIC", "METERS")
            else:
                length_m = geom.getLength("PLANAR", "METERS")
            road_len_m[oid] = length_m
            road_vulFL[oid] = vkeyf.strip() if isinstance(vkeyf, str) else vkeyf
            road_vulEQ[oid] = vkeye.strip() if isinstance(vkeye, str) else vkeye
            road_cost_m[oid] = float(repk_val) / 1000.0
            oid_to_tramo[oid] = tramo

    # 3) Build per-road sequences of points 
    per_road, pt_s_m = {}, {}
    with arcpy.da.SearchCursor(pts, ["OID@", "ORIG_FID", "SHAPE@"] ) as cur:
        for pt_oid, rid, shp in cur:
            geom = road_geom.get(rid)
            if not geom:
                continue
            _, s_native, _, _ = geom.queryPointAndDistance(shp, use_percentage=False)
            native_len = road_len_native.get(rid, 0.0)
            length_m = road_len_m.get(rid, 0.0)
            s_m = (s_native / native_len) * length_m if native_len > 0.0 else 0.0
            pt_s_m[pt_oid] = (rid, s_m)
            per_road.setdefault(rid, []).append((pt_oid, s_m))

    # 4) Compute tributary length per point
    trib_len_map = {}
    for rid, rows in per_road.items():
        rows.sort(key=itemgetter(1))
        L = road_len_m.get(rid, 0.0)
        for i, (pt_oid, s) in enumerate(rows):
            left_m  = s - rows[i - 1][1] if i > 0 else s
            right_m = (rows[i + 1][1] if i < len(rows) - 1 else L) - s
            trib_len = max(0.0, 0.5 * (left_m + right_m))
            trib_len_map[pt_oid] = trib_len
    ensure_field(pts, "trib_len", "DOUBLE")
    with arcpy.da.UpdateCursor(pts, ["OID@", "trib_len"]) as cur:
        for oid, _ in cur:
            tl = trib_len_map.get(oid, 0.0)
            cur.updateRow((oid, tl))

    # 5) Return points and metadata for reuse 
    road_meta = {"oid_name": oid_name, "road_vulFL": road_vulFL, "road_vulEQ": road_vulEQ, "road_len_m": road_len_m, "sr_type": sr.type, "road_cost_m": road_cost_m, "oid_to_tramo": oid_to_tramo}
    return pts, road_meta


#
# Damage/loss processing
#


def process_roads(roads_path, raster_path, pts_reusable, vul_db, road_meta, hazard_type):
    """Compute per-road repair loss (from RMD curve) and per-road max vulnerability (T curve)"""
    # 1) Sample raster values at the reusable points
    pts_vals = r"in_memory\pts_vals"
    if arcpy.Exists(pts_vals):
        arcpy.management.Delete(pts_vals)
    sample_raster_to_points(pts_reusable, raster_path, pts_vals, value_field="RASTERVALU")

    # 2) Calculate the component damage and loss 
    road_cost = road_meta["road_cost_m"]
    oid_sum, oid_vul = {}, {}
    has_lq = any(f.name.upper() == "LQ_VAL" for f in arcpy.ListFields(pts_vals))
    fields = ["OID@", "ORIG_FID", "trib_len", "RASTERVALU"] + (["LQ_VAL"] if has_lq else [])
    with arcpy.da.SearchCursor(pts_vals, fields) as cur:
        for row in cur:
            if has_lq:
                pt_oid, rid, trib_len, rv, lq_val = row
            else:
                pt_oid, rid, trib_len, rv = row
                lq_val = None
            try:
                rv_val = float(rv)
            except Exception:
                rv_val = np.nan
            if not np.isfinite(rv_val):
                continue

            # 2a) Compute damages per road OID
            full_key_rmd = build_vul_key(road_meta, hazard_type, rid=rid, lq=lq_val, curve_type="RMD")
            if full_key_rmd in vul_db:
                xs_rmd, ys_rmd = vul_db[full_key_rmd]
                if xs_rmd and ys_rmd:
                    lo_rmd, hi_rmd = min(xs_rmd), max(xs_rmd)
                    xq_rmd = max(min(rv_val, hi_rmd), lo_rmd)
                    dmg = float(np.interp(xq_rmd, xs_rmd, ys_rmd)) / 100.0
                    loss = dmg * max(trib_len or 0.0, 0.0) * road_cost.get(rid, 0.0)
                    oid_sum[rid] = oid_sum.get(rid, 0.0) + loss

            # 2b) Compute losses per road OID
            full_key_T = build_vul_key(road_meta, hazard_type, rid=rid, lq=lq_val, curve_type="T")
            if full_key_T in vul_db:
                xs_T, ys_T = vul_db[full_key_T]
                if xs_T and ys_T:
                    lo_T, hi_T = min(xs_T), max(xs_T)
                    xq_T = max(min(rv_val, hi_T), lo_T)
                    vul_val = float(np.interp(xq_T, xs_T, ys_T)) / 24.0   
                    prev_best = oid_vul.get(rid)
                    if (prev_best is None) or (vul_val > prev_best):
                        oid_vul[rid] = vul_val

    # 3) Delete the temporal values not needed
    if arcpy.Exists(pts_vals):
        arcpy.management.Delete(pts_vals)

    # 4) Return the oid values needed
    return oid_sum, oid_vul 


def process_component(comp_name, comp_path, raster_path, vul_db, hazard_type):
    """Compute per-component repair loss (RMD) and per-component vulnerability (T)"""
    # 1) Take the raster values at the component points
    comp_pts = fr"in_memory\{comp_name}_pts"
    sample_raster_to_points(comp_path, raster_path, comp_pts, value_field="RASTERVALU")

    # 2) Calculate the component damage and loss 
    hz_lower = (hazard_type or "").strip().lower()
    is_eq = hz_lower in ("earthquake", "eq")
    vul_field = "vul_eq" if is_eq else "vul_f"
    has_lq = any(f.name.upper() == "LQ_VAL" for f in arcpy.ListFields(comp_pts))
    fields = ["OID@", vul_field, "RASTERVALU", "rep_cost"] + (["LQ_VAL"] if has_lq else [])
    oid_sum, oid_vul = {}, {}
    with arcpy.da.SearchCursor(comp_pts, fields) as cur:
        for row in cur:
            if has_lq:
                oid, vkey, rv, rep_val, lq_val = row
            else:
                oid, vkey, rv, rep_val = row
                lq_val = None
            try:
                rv_val = float(rv)
            except Exception:
                rv_val = np.nan
            if not np.isfinite(rv_val):
                continue

            # 2a) Compute damages per road OID
            key_rmd = build_vul_key(None, hazard_type, vkey=vkey, lq=lq_val, curve_type="RMD")
            dmg_val = 0.0
            if key_rmd and key_rmd in vul_db:
                xs, ys = vul_db[key_rmd]
                if xs and ys and rv_val is not None:
                    lo, hi = min(xs), max(xs)
                    xq = max(min(float(rv_val), hi), lo)
                    dmg_val = (float(np.interp(xq, xs, ys)) / 100.0) * float(rep_val)
            oid_sum[oid] = dmg_val 

            # 2b) Compute losses per road OID
            key_T = build_vul_key(None, hazard_type, vkey=vkey, lq=lq_val, curve_type="T")
            vul_val = 0.0
            if key_T and key_T in vul_db:
                xs_T, ys_T = vul_db[key_T]
                if xs_T and ys_T and rv_val is not None:
                    lo_T, hi_T = min(xs_T), max(xs_T)
                    xq_T = max(min(float(rv_val), hi_T), lo_T)
                    vul_val = float(np.interp(xq_T, xs_T, ys_T)) / 24.0
            oid_vul[oid] = vul_val

    # 3) Delete the temporal values not needed
    if arcpy.Exists(comp_pts):
        arcpy.management.Delete(comp_pts)

    # 4) Return the oid values needed
    return oid_sum, oid_vul


def compute_DAE_fields(fc, hazard_to_TRs_sorted):
    """Compute Direct Annual Expected loss (DAE) per hazard and total DAE"""
    # 1) Prepare output DAE fields (per hazard and total)
    haz_list = list(hazard_to_TRs_sorted.keys())
    for hz in haz_list:
        ensure_field(fc, f"DAE_{hz}", "DOUBLE")
    ensure_field(fc, "DAE", "DOUBLE")

    # 2) Build field lists and index mapping
    damage_fields = [f"damage_{hz}_{tr}" for hz, trs in hazard_to_TRs_sorted.items() for tr in trs]
    dae_fields    = [f"DAE_{hz}" for hz in haz_list]
    read_fields   = ["OID@"] + damage_fields + dae_fields + ["DAE"]
    idx = {n:i for i,n in enumerate(read_fields)}

    # 3) Integrate LEC (area under dama vs freq) per hazard and sum
    with arcpy.da.UpdateCursor(fc, read_fields) as cur:
        for row in cur:
            total = 0.0
            for hz in haz_list:
                trs = hazard_to_TRs_sorted[hz]
                x = [1.0/float(tr) for tr in trs]
                y = [0.0 if (row[idx[f"damage_{hz}_{tr}"]] in (None, "")) else float(row[idx[f"damage_{hz}_{tr}"]]) for tr in trs]
                order = np.argsort(x)
                x_sorted = np.asarray(x, float)[order]
                y_sorted = np.asarray(y, float)[order]
                dae = float(np.trapz(y_sorted, x_sorted) + x_sorted[0] * y_sorted[0]) if len(x_sorted) >= 2 else 0.0
                # dae = float(0.5*(abs(np.trapz(y_sorted, x_sorted))+abs(np.trapz(x_sorted, y_sorted)))) if len(x_sorted) >= 2 else 0.0
                row[idx[f"DAE_{hz}"]] = dae
                total += dae
                
            # 4) Update the total DAE across all hazards
            row[idx["DAE"]] = total
            cur.updateRow(row)


def compute_PAE_fields(fc, hazard_to_TRs_sorted, dlt_total_by_oid: Dict[int, float], vul_mem: Dict[str, Dict[int, Dict[int, float]]]):
    """Compute Probable Annual Economic loss (PAE) per hazard and total PAE"""
    # 1) Prepare output loss and PAE fields (per hazard and total)
    for hz, trs in hazard_to_TRs_sorted.items():
        for tr in trs:
            ensure_field(fc, f"loss_{hz}_{tr}", "DOUBLE")
    for hz in hazard_to_TRs_sorted.keys():
        ensure_field(fc, f"PAE_{hz}", "DOUBLE")
    ensure_field(fc, "PAE_total", "DOUBLE")

    # 2) Write loss fields using in-memory DLT and in-memory vulnerability
    hazards = list(hazard_to_TRs_sorted.keys())
    loss_fields = [f"loss_{hz}_{tr}" for hz, trs in hazard_to_TRs_sorted.items() for tr in trs]
    oid_field = arcpy.Describe(fc).OIDFieldName
    read_write = [oid_field] + loss_fields
    idx = {n: i for i, n in enumerate(read_write)}
    with arcpy.da.UpdateCursor(fc, read_write) as cur:
        for row in cur:
            oid = row[idx[oid_field]]
            dlt_tot = float(dlt_total_by_oid.get(oid, 0.0))
            for hz in hazards:
                for tr in hazard_to_TRs_sorted[hz]:
                    v = float(vul_mem.get(hz, {}).get(tr, {}).get(oid, 0.0))
                    row[idx[f"loss_{hz}_{tr}"]] = dlt_tot * v
            cur.updateRow(row)

    # 3) Integrate loss exceedance curves per hazard and sum totals
    pae_fields = [f"PAE_{hz}" for hz in hazards]
    read_write_fields = loss_fields + pae_fields + ["PAE_total"]
    idx = {n: i for i, n in enumerate(read_write_fields)}
    with arcpy.da.UpdateCursor(fc, read_write_fields) as cur:
        for row in cur:
            total_pae = 0.0
            for hz in hazards:
                trs = hazard_to_TRs_sorted[hz]
                x = [1.0 / float(tr) for tr in trs]
                y = [0.0 if (row[idx[f"loss_{hz}_{tr}"]] in (None, "")) else float(row[idx[f"loss_{hz}_{tr}"]]) for tr in trs]
                order = np.argsort(x)
                x_sorted = np.asarray(x, float)[order]
                y_sorted = np.asarray(y, float)[order]
                pae = float(np.trapz(y_sorted, x_sorted) + x_sorted[0] * y_sorted[0]) if len(x_sorted) >= 2 else 0.0
                # pae = float(0.5 * (abs(np.trapz(y_sorted, x_sorted)) + abs(np.trapz(x_sorted, y_sorted)))) if len(x_sorted) >= 2 else 0.0
                row[idx[f"PAE_{hz}"]] = pae
                total_pae += pae

            # 4) Update the total PAE across all hazards
            row[idx["PAE_total"]] = total_pae
            cur.updateRow(row)


#
# Detour processing
#


def dijkstra(adjacency: Dict[Tuple[float, float], List[Tuple[Tuple[float, float], float, int]]],  start: Tuple[float, float], end: Tuple[float, float], skip_oid: Optional[int] = None):
    """Compute shortest path length between two network nodes using Dijkstra"""
    # 1) Initialize distance dict, min-heap, and visited set
    dist: Dict[Tuple[float, float], float] = {start: 0.0}
    queue: List[Tuple[float, Tuple[float, float]]] = [(0.0, start)]
    visited: set[Tuple[float, float]] = set()

    # 2) Process nodes until queue is empty
    while queue:
        d, u = heapq.heappop(queue)

        # 3) Stop if destination reached
        if u == end:
            return d

        # 4) Skip already-visited nodes
        if u in visited:
            continue
        visited.add(u)

        # 5) Relax edges for all neighbors of u
        for v, weight, oid in adjacency.get(u, []):
            if skip_oid is not None and oid == skip_oid:
                continue
            alt = d + weight
            if alt < dist.get(v, np.inf):
                dist[v] = alt
                heapq.heappush(queue, (alt, v))
                
    # 6) Return None if destination not reachable
    return None


def read_taxonomy_csv(csv_path: str):
    """Read operational parameters (COV, OCU) per traffic taxonomy"""
    # 1) Initialize output dictionary for taxonomy data
    out: Dict[str, Dict[str, float]] = {}

    # 2) Open CSV file safely, tolerate bad characters
    with open(csv_path, "r", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)

        # 3) Iterate over each row, extract taxonomy and numeric fields
        for row in reader:
            tax = (row.get("taxonomy") or "").strip()
            if not tax:
                continue

            # 4) Parse COV and OCU as floats, default to 0.0 if missing 
            try:
                cov = float(row.get("COV", 0) or 0)
            except Exception:
                cov = 0.0
            try:
                ocu = float(row.get("OCU", 0) or 0)
            except Exception:
                ocu = 0.0

            # 5) Store clean values by taxonomy key and return out
            out[tax] = {"COV": cov, "OCU": ocu}
    return out


def road_loss_analysis(exposure_path: str, taxonomy_csv: str, gdp_per_capita_per_day: float):
    """Compute detour-based daily loss totals per road segment"""
    # 1) Get OID field name and confirm geometry structure
    desc = arcpy.Describe(exposure_path)
    oid_field = desc.OIDFieldName

    # 2) Define AADT fields (traffic counts for taxonomy levels)
    t_fields = [f"T{i}" for i in range(9, 16)]

    # 3) Initialize adjacency, edge list, and node degree map
    adjacency: Dict[Tuple[float, float], List[Tuple[Tuple[float, float], float, int]]] = defaultdict(list)
    edges: List[Tuple[Tuple[float, float], Tuple[float, float], float, int]] = []
    node_degree: Dict[Tuple[float, float], int] = defaultdict(int)

    # 4) Populate adjacency and edge data from feature geometry
    with arcpy.da.SearchCursor(exposure_path, [oid_field, "SHAPE@", "Longitud"]) as cur:
        for oid, geom, length in cur:
            try:
                length_val = float(length)
            except Exception:
                length_val = geom.getLength("PLANAR", "METERS")
            a, b = get_endpoints(geom)
            adjacency[a].append((b, length_val, oid))
            adjacency[b].append((a, length_val, oid))
            node_degree[a] += 1
            node_degree[b] += 1
            edges.append((a, b, length_val, oid))

    # 5) Precompute per-edge metrics: dead-end status & detour difference
    oid_is_dead_end: Dict[int, bool] = {}
    oid_diff: Dict[int, float] = {}
    oid_no_alt: Dict[int, bool] = {}
    for a, b, weight, oid in edges:
        dead_end = (node_degree[a] == 1) or (node_degree[b] == 1)
        oid_is_dead_end[oid] = dead_end

        # 5a) Compute alternate path ignoring this edge
        alt_length = dijkstra(adjacency, a, b, skip_oid=oid)

        # 5b) Compute diff = max(0,alt_length-current_length)
        if alt_length is None:
            diff_val = 0.0
            oid_no_alt[oid] = True
        else:
            diff_val = max(0.0, alt_length - weight) / 1000.0
            oid_no_alt[oid] = False
        oid_diff[oid] = float(diff_val) 

    # 6) Load taxonomy parameters (COV and OCU) from CSV
    tax_map = read_taxonomy_csv(taxonomy_csv)
    cov_by_t = {f"T{i}": float(tax_map.get(f"T{i}", {}).get("COV", 0.0)) for i in range(9, 16)}
    ocu_by_t = {f"T{i}": float(tax_map.get(f"T{i}", {}).get("OCU", 0.0)) for i in range(9, 16)}

    # 7) Compute the DLTs (differences and losses multiplication)
    gdp_day = float(gdp_per_capita_per_day)
    dlt_total_by_oid: Dict[int, float] = {}
    cursor_fields = [oid_field] + t_fields
    with arcpy.da.SearchCursor(exposure_path, cursor_fields) as cur:
        for row in cur:
            oid_val = row[0]
            aadt = {t: float(row[1 + i] or 0.0) for i, t in enumerate(t_fields)}
            is_dead = oid_is_dead_end.get(oid_val, False) or oid_no_alt.get(oid_val, False)
            diff_val = oid_diff.get(oid_val, 0.0)
            dlt_vals = []
            for t in t_fields:
                mult = (ocu_by_t[t] * gdp_day) if is_dead else (cov_by_t[t] * diff_val)
                dlt_vals.append(float(aadt[t] * mult))
            dlt_total_by_oid[oid_val] = float(sum(dlt_vals))

    # 8) Return the updated results with the DLTs
    return dlt_total_by_oid


#
# Writeback/aggregation helpers
#


def create_damage_fields(fc, hazard_to_TRs_sorted):
    """Ensure per-hazard, per-TR damage fields exist on the target feature class"""
    # 1) Ensure damage fields exist for every (hazard, TR)
    for hz, tr_list in hazard_to_TRs_sorted.items():
        for tr in tr_list:
            ensure_field(fc, f"damage_{hz}_{tr}", "DOUBLE")
            

def write_damage_by_oid(fc, roads_path, oid_to_loss, field_name):
    """Write per-road OID mapped values (e.g., damage/loss) into a target field on an output copy"""
    # 1) Ensure target field exists on output feature class
    ensure_field(fc, field_name, "DOUBLE")

    # 2) Collect road OIDs in stable order
    rid_list = []
    oid_field_name = arcpy.Describe(roads_path).OIDFieldName
    with arcpy.da.SearchCursor(roads_path, [oid_field_name]) as cur:
        for (rid,) in cur:
            rid_list.append(rid)

    # 3) Write mapped losses to output feature class rows by index
    with arcpy.da.UpdateCursor(fc, [field_name]) as cur:
        for i, row in enumerate(cur):
            rid = rid_list[i] if i < len(rid_list) else None
            row[0] = oid_to_loss.get(rid, 0.0) if rid is not None else 0.0
            cur.updateRow(row)
            

def sum_component_DAE_by_tramo(comp_fc, dae_field="DAE"):
    """Aggregate a component-layer DAE-like field by ID_TRAMO, returning tramo -> summed value"""
    # 1) Resolve tramo field (ID_TRAMO) or fail
    tramo_field = find_field(comp_fc, "ID_TRAMO")
    if not tramo_field:
        raise RuntimeError(f"ID_TRAMO field not found on {comp_fc}.")

    # 2) Resolve actual DAE field name (case-insensitive)
    existing = {f.name.upper(): f.name for f in arcpy.ListFields(comp_fc)}
    dae_actual = existing.get((dae_field or "DAE").upper())
    if not dae_actual:
        return {}

    # 3) Accumulate requested DAE field by tramo
    tramo_sum = {}
    with arcpy.da.SearchCursor(comp_fc, [tramo_field, dae_actual]) as cur:
        for tramo, val in cur:
            tramo_sum[tramo] = tramo_sum.get(tramo, 0.0) + (0.0 if val in (None, "") else float(val))

    # 4) Return the damage sum of the assets within a tramo
    return tramo_sum


def tramo_dlt_from_roads(road_fc, dlt_by_oid: Dict[int, float]):
    """Convert per-road DLT (by road OID) into tramo-level DLT mapping (ID_TRAMO -> DLT)"""
    # 1) Resolve segment identifier field on the road layer
    tramo_field = find_field(road_fc, "ID_TRAMO")
    if not tramo_field:
        raise RuntimeError("ID_TRAMO field not found on road layer (needed to map DLT to components).")

    # 2) Get ObjectID field name for the road feature class
    oid_field = arcpy.Describe(road_fc).OIDFieldName

    # 3) Build mapping for components: tramo_id -> DLT value
    tramo_to_dlt: Dict[object, float] = {}
    with arcpy.da.SearchCursor(road_fc, [oid_field, tramo_field]) as cur:
        for oid, tramo in cur:
            tramo_to_dlt[tramo] = float(dlt_by_oid.get(oid, 0.0))

    # 4) Return DLT aggregated at tramo level
    return tramo_to_dlt


def map_component_dlt_by_tramo(comp_fc, tramo_to_dlt: Dict[object, float]):
    """Map tramo-level DLT values onto component OIDs using each component's ID_TRAMO"""
    # 1) Resolve segment identifier field on the component layer
    tramo_field = find_field(comp_fc, "ID_TRAMO")
    if not tramo_field:
        raise RuntimeError(f"ID_TRAMO field not found on {comp_fc} (needed to map DLT to components).")

    # 2) Get ObjectID field name for the component feature class
    oid_field = arcpy.Describe(comp_fc).OIDFieldName

    # 3) Build mapping for components: component OID -> DLT value
    out: Dict[int, float] = {}
    with arcpy.da.SearchCursor(comp_fc, [oid_field, tramo_field]) as cur:
        for oid, tramo in cur:
            out[int(oid)] = float(tramo_to_dlt.get(tramo, 0.0))

    # 4) Return per-component DLT mapping
    return out


#
# Climate change
#


def parse_tp_fields(mod_fc):
    """Parse TP-TR modification fields (TP###S#M) from the climate-change polygon layer by scenario"""
    # 1) Compile regex to match TP fields (e.g., TP50S2M, TP100S2M)
    pat = re.compile(r"TP(\d+)(S\dM)$", re.I)

    # 2) Initialize output dictionary: scenario -> [(TP, field_name), ...]
    out = defaultdict(list)

    # 3) Scan modification polygon fields and collect TP fields by scenario
    for f in arcpy.ListFields(mod_fc):
        m = pat.fullmatch(f.name)
        if m:
            tp = int(m.group(1))
            scen = m.group(2).upper()
            out[scen].append((tp, f.name))

    # 4) Sort TP fields within each scenario by TP value
    for k in out:
        out[k].sort(key=lambda x: x[0])

    # 5) Return parsed TP fields by scenario
    return out


def apply_TRmods(fc, mod_fc, scen, tp_fields, is_roads=False):
    """Apply TP-based modified return periods to compute scenario-adjusted DAE/PAE for river/coast hazards"""
    # 1) Normalize scenario name and define output fields
    scen = scen.upper()
    out_txt = f"TP_TR_MODS_{scen}"
    out_fields = {
        "damage_river": f"DAE_river_mod_{scen}",
        "damage_coast": f"DAE_coast_mod_{scen}",
        "loss_river":   f"PAE_river_mod_{scen}",
        "loss_coast":   f"PAE_coast_mod_{scen}",
    }

    # 2) Ensure output fields exist
    ensure_field(fc, out_txt, "TEXT")
    for f in out_fields.values():
        ensure_field(fc, f, "DOUBLE")

    # 3) Resolve ObjectID field name of the target feature class
    oid_fc = arcpy.Describe(fc).OIDFieldName

    # 4) Prepare target geometry for spatial join
    tgt = fc
    if is_roads:
        tgt = r"in_memory\cent"
        if arcpy.Exists(tgt):
            arcpy.management.Delete(tgt)
        arcpy.management.FeatureToPoint(fc, tgt, "INSIDE")

    # 5) Spatial join between target features and TP-modification polygons
    sj = r"in_memory\sj"
    if arcpy.Exists(sj):
        arcpy.management.Delete(sj)
    arcpy.analysis.SpatialJoin(
        tgt, mod_fc, sj,
        "JOIN_ONE_TO_ONE", "KEEP_ALL",
        match_option="INTERSECT"
    )

    # 6) Determine correct join-back key (ORIG_FID or TARGET_FID)
    sj_fields = {f.name.upper(): f.name for f in arcpy.ListFields(sj)}
    if is_roads:
        key_field = sj_fields.get("ORIG_FID") or sj_fields.get("TARGET_FID")
    else:
        key_field = sj_fields.get("TARGET_FID") or sj_fields.get("ORIG_FID")
    if not key_field:
        raise RuntimeError("SpatialJoin output missing ORIG_FID/TARGET_FID; cannot map back to fc.")

    # 7) Sort TP fields and extract field names in TP order
    tp_fields = sorted(tp_fields, key=lambda x: x[0])
    join_tp_names = [fn for _, fn in tp_fields]

    # 8) Build mapping: feature OID -> { TP : modified_TR }
    oid2map = {}
    with arcpy.da.SearchCursor(sj, [key_field] + join_tp_names) as cur:
        for row in cur:
            base_oid = row[0]
            if base_oid in (None, ""):
                continue
            mm = {}
            for i, (tp, _) in enumerate(tp_fields):
                v = row[i + 1]
                if v in (None, ""):
                    continue
                try:
                    mm[int(tp)] = float(v)
                except Exception:
                    pass
            if mm:
                oid2map[int(base_oid)] = mm

    # 9) Cleanup temporary spatial join products
    if is_roads and arcpy.Exists(tgt):
        arcpy.management.Delete(tgt)
    if arcpy.Exists(sj):
        arcpy.management.Delete(sj)

    # 10) Build field maps: TP -> damage/loss field name on fc
    def fldmap(prefix):
        pref = prefix.lower() + "_"
        d = {}
        for f in arcpy.ListFields(fc):
            n = f.name.lower()
            if n.startswith(pref):
                s = n.split("_")[-1]
                if s.isdigit():
                    d[int(s)] = f.name
        return d
    tp_to_field = {k: fldmap(k) for k in out_fields.keys()}

    # 11) Build update cursor field list
    fields = [oid_fc, out_txt] + list(out_fields.values())
    for d in tp_to_field.values():
        fields += [d[t] for t in sorted(d)]

    # 12) De-duplicate fields while preserving order
    seen = set()
    fields = [f for f in fields if f and (f not in seen and not seen.add(f))]
    idx = {f: i for i, f in enumerate(fields)}

    # 13) Safe float reader (NULL-safe)
    def getf(row, fname):
        v = row[idx[fname]]
        if v in (None, ""):
            return None
        try:
            return float(v)
        except Exception:
            return None

    # 14) Integrate losses/damages using ONLY mapped TPs
    def integ(row, tp_field_map, tp_tr_map):
        x, y = [], []
        for tp, tr in tp_tr_map.items():
            fname = tp_field_map.get(tp)
            if not fname:
                continue
            yy = getf(row, fname)
            if yy is None:
                continue
            try:
                tr = float(tr)
            except Exception:
                continue
            if tr <= 0:
                continue
            x.append(1.0 / tr)
            y.append(yy)
        if len(x) < 2:
            return 0.0
        o = np.argsort(x)
        xs = np.asarray(x)[o]
        ys = np.asarray(y)[o]
        return float(np.trapz(ys, xs) + xs[0] * ys[0])

    # 15) Update target feature class with modified DAE / PAE values
    with arcpy.da.UpdateCursor(fc, fields) as cur:
        for row in cur:
            oid = int(row[idx[oid_fc]])
            m = oid2map.get(oid, {})
            
            # 15a) Write TP → TR mapping as text
            row[idx[out_txt]] = "; ".join(
                f"TP{tp}_TR{tr:g}" for tp, tr in sorted(m.items())
            ) if m else ""

            # 15b) Compute modified DAE / PAE using exact TP fields
            for pref, out_f in out_fields.items():
                row[idx[out_f]] = integ(row, tp_to_field[pref], m)

            cur.updateRow(row)


def compute_mod_totals(fc, scen):
    """Compute scenario totals: DAE_mod_{scen} and PAE_total_mod_{scen} combining modified river/coast with baseline tsunami/earthquake"""
    # 1) Guard
    if not fc or not arcpy.Exists(fc):
        return

    scen = scen.upper()

    # 2) Target fields to create (ONLY these two)
    dae_mod     = f"DAE_mod_{scen}"
    pae_tot_mod = f"PAE_total_mod_{scen}"
    ensure_field(fc, dae_mod, "DOUBLE")
    ensure_field(fc, pae_tot_mod, "DOUBLE")

    # 3) Source fields (river/coast modified + tsunami/earthquake baseline)
    dae_riv_mod = f"DAE_river_mod_{scen}"
    dae_coa_mod = f"DAE_coast_mod_{scen}"
    pae_riv_mod = f"PAE_river_mod_{scen}"
    pae_coa_mod = f"PAE_coast_mod_{scen}"

    existing = {f.name.upper(): f.name for f in arcpy.ListFields(fc)}

    # 4) Only include fields that exist (case-safe)
    want = [dae_riv_mod, dae_coa_mod, "DAE_tsunami", "DAE_earthquake",
            pae_riv_mod, pae_coa_mod, "PAE_tsunami", "PAE_earthquake"]
    src_fields = [existing[w.upper()] for w in want if w.upper() in existing]

    fields = src_fields + [dae_mod, pae_tot_mod]
    idx = {n: i for i, n in enumerate(fields)}

    def getv(row, fname):
        actual = existing.get(fname.upper())
        if (not actual) or (actual not in idx):
            return 0.0
        v = row[idx[actual]]
        return 0.0 if v in (None, "") else float(v)

    # 5) Compute DAE_mod and PAE_total_mod
    with arcpy.da.UpdateCursor(fc, fields) as cur:
        for row in cur:
            dae_total = (
                getv(row, dae_riv_mod) +
                getv(row, dae_coa_mod) +
                getv(row, "DAE_tsunami") +
                getv(row, "DAE_earthquake")
            )
            pae_total = (
                getv(row, pae_riv_mod) +
                getv(row, pae_coa_mod) +
                getv(row, "PAE_tsunami") +
                getv(row, "PAE_earthquake")
            )

            row[idx[dae_mod]]     = dae_total
            row[idx[pae_tot_mod]] = pae_total
            cur.updateRow(row)
            
            
# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------


def main():
    # 1) Set ArcPy environment flags for outputs
    arcpy.env.overwriteOutput = True
    arcpy.env.addOutputsToMap = True

    # 2) Read the script parameters from ArcGIS
    roads_path  = arcpy.GetParameterAsText(0)
    bridge_path = arcpy.GetParameterAsText(1)
    tunnel_path = arcpy.GetParameterAsText(2)
    draina_path = arcpy.GetParameterAsText(3)
    fl_rive_raw = arcpy.GetParameterAsText(4)   
    fl_coas_raw = arcpy.GetParameterAsText(5)   
    ts_coas_raw = arcpy.GetParameterAsText(6)   
    earthqu_raw = arcpy.GetParameterAsText(7)   
    liquefa_raw = arcpy.GetParameterAsText(8)
    mod_tp_poly = arcpy.GetParameterAsText(9)
    vulner_data = arcpy.GetParameterAsText(10)
    operat_data = arcpy.GetParameterAsText(11)
    gdppca_doub = arcpy.GetParameterAsText(12)
    road_segme  = arcpy.GetParameterAsText(13)

    # 3) Validate the minimum required parameters
    if not roads_path:
        raise ValueError("A roads layer is required. Provide a valid road layer.")
    if not road_segme:
        raise ValueError("Road segment length is required when roads are provided.")
    if not vulner_data:
        raise ValueError("A vulnerability database (.csv) is always required.")
    if (operat_data and not gdppca_doub) or (gdppca_doub and not operat_data):
        raise ValueError("Both Operations database and GDP per capita per day must be provided together, or neither should be provided.")

    # 4) Load taxonomy and vulnerability database
    vul_db = read_vul_db(vulner_data)
    if not vul_db:
        raise ValueError("Vulnerability database could not be loaded or is empty.")

    # 5) Parse hazard rasters and normalize tuples
    ras_haz = []
    for raw, hz in ((fl_rive_raw, "river"),
                    (fl_coas_raw, "coast"),
                    (ts_coas_raw, "tsunami"),
                    (earthqu_raw, "earthquake")):
        if raw:
            for r in raw.split(";"):
                r = r.strip()
                if r:
                    ras_haz.append((r, hz))
    if not ras_haz:
        raise ValueError("At least one hazard raster layer must be provided.")

    # 6) Build hazard-TR map (from raster names)
    hazard_to_TRs = {}
    for raster_path, hz in ras_haz:
        base = arcpy.Describe(raster_path).baseName
        tr = parse_TR_from_name(base)
        if tr is None:
            arcpy.AddWarning(f"Could not parse TR from raster name '{base}'. This raster will be skipped for DAE fields.")
            continue
        hz_key = (hz or "").strip().lower()
        hazard_to_TRs.setdefault(hz_key, set()).add(tr)
    hazard_to_TRs_sorted = {hz: sorted(trs) for hz, trs in hazard_to_TRs.items()}

    # 7) Prepare output geodatabase and paths   
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_gdb = os.path.join(script_dir, "BSA2.gdb")
    gdb_dir = os.path.dirname(target_gdb)
    if not os.path.isdir(gdb_dir):
        os.makedirs(gdb_dir, exist_ok=True)
    if not arcpy.Exists(target_gdb):
        arcpy.management.CreateFileGDB(gdb_dir, os.path.splitext(os.path.basename(target_gdb))[0])

    # 8) Create consolidated working copies per component
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Format: 2025-11-17 at 13:45:22, for example (..._20251117_134522)
    road_damage   = create_consolidated_copy(roads_path, target_gdb, f"roads_results_{stamp}")
    bridge_damage = create_consolidated_copy(bridge_path, target_gdb, f"bridges_results_{stamp}") if bridge_path else None
    tunnel_damage = create_consolidated_copy(tunnel_path, target_gdb, f"tunnels_results_{stamp}") if tunnel_path else None
    draina_damage = create_consolidated_copy(draina_path, target_gdb, f"drainage_results_{stamp}") if draina_path else None
    loc_folder = os.path.join(gdb_dir, "Loc")
    if not os.path.exists(loc_folder):
        os.makedirs(loc_folder)
    loc_path = os.path.join(loc_folder, f"run_config_{stamp}.loc")
    param_names = ["roads_path", "bridge_path", "tunnel_path", "draina_path", "fl_rive_raw", "fl_coas_raw", "ts_coas_raw", "earthqu_raw", "liquefa_raw", "vulner_data", "operat_data", "gdppca_doub", "road_segme", "mod_tp_poly"]
    with open(loc_path, "w", encoding="utf-8") as f:
        for name in param_names:
            f.write(f"{name}={locals()[name]}\n")

    # 9) Resolve liquefaction raster if provided
    liquefa_path = None
    if liquefa_raw:
        for r in liquefa_raw.split(";"):
            r = r.strip()
            if r:
                liquefa_path = r
                break

    # 10) Build reusable road points & attach LQ if needed
    pts, road_meta = road_geometry(road_damage, road_segme)
    has_earthquake = any((hz or "").strip().lower() == "earthquake" for _, hz in ras_haz)
    if has_earthquake and liquefa_path:
        liquefaction_once(pts, liquefa_path, value_field="LQ_VAL")
        if bridge_damage and arcpy.Exists(bridge_damage):
            liquefaction_once(bridge_damage, liquefa_path, value_field="LQ_VAL")
        if tunnel_damage and arcpy.Exists(tunnel_damage):
            liquefaction_once(tunnel_damage, liquefa_path, value_field="LQ_VAL")
        if draina_damage and arcpy.Exists(draina_damage):
            liquefaction_once(draina_damage, liquefa_path, value_field="LQ_VAL")

    # 11) Ensure damage fields exist on each output component 
    for fc in [road_damage, bridge_damage, tunnel_damage, draina_damage]:
        if fc and arcpy.Exists(fc):
            create_damage_fields(fc, hazard_to_TRs_sorted)

    # 12) Validate tramo field on roads output
    id_field = find_field(road_damage, "ID_TRAMO")
    if not id_field:
        raise RuntimeError("ID_TRAMO field not found on road_damage.")

    # 13) Iterate each hazard raster/TR and compute damages
    vul_mem_roads: Dict[str, Dict[int, Dict[int, float]]] = defaultdict(lambda: defaultdict(dict))
    vul_mem_bridge: Dict[str, Dict[int, Dict[int, float]]] = defaultdict(lambda: defaultdict(dict))
    vul_mem_tunnel: Dict[str, Dict[int, Dict[int, float]]] = defaultdict(lambda: defaultdict(dict))
    vul_mem_drain: Dict[str, Dict[int, Dict[int, float]]] = defaultdict(lambda: defaultdict(dict))
    for raster_path, hz in ras_haz:
        hz_key = (hz or "").strip().lower()
        base = arcpy.Describe(raster_path).baseName
        tr = parse_TR_from_name(base)
        if tr is None:
            arcpy.AddWarning(f"Skipping raster '{base}' because TR could not be parsed.")
            continue
        field_name = f"damage_{hz_key}_{tr}"

        # 13a) Roads
        oid_to_loss, oid_to_vul = process_roads(
            roads_path=road_damage,
            raster_path=raster_path,
            pts_reusable=pts,
            vul_db=vul_db,
            road_meta=road_meta,
            hazard_type=hz_key,
        )
        write_damage_by_oid(road_damage, road_damage, oid_to_loss, field_name)
        for rid, v in oid_to_vul.items():
            vul_mem_roads[hz_key][tr][rid] = float(v)

        # 13b) Bridges
        if bridge_damage and bridge_path and arcpy.Exists(bridge_damage):
            oid_to_loss_bridge, oid_to_vul_bridge = process_component(
                comp_name="bridge",
                comp_path=bridge_damage,
                raster_path=raster_path,
                vul_db=vul_db,
                hazard_type=hz_key,
            )
            write_damage_by_oid(bridge_damage, bridge_damage, oid_to_loss_bridge, field_name)
            for oid, v in oid_to_vul_bridge.items():
                vul_mem_bridge[hz_key][tr][oid] = float(v)

        # 13c) Tunnels
        if tunnel_damage and tunnel_path and arcpy.Exists(tunnel_damage):
            oid_to_loss_tunnel, oid_to_vul_tunnel = process_component(
                comp_name="tunnel",
                comp_path=tunnel_damage,
                raster_path=raster_path,
                vul_db=vul_db,
                hazard_type=hz_key,
            )
            write_damage_by_oid(tunnel_damage, tunnel_damage, oid_to_loss_tunnel, field_name)
            for oid, v in oid_to_vul_tunnel.items():
                vul_mem_tunnel[hz_key][tr][oid] = float(v)

        # 13d) Drainage
        if draina_damage and draina_path and arcpy.Exists(draina_damage):
            oid_to_loss_drain, oid_to_vul_drain = process_component(
                comp_name="drainage",
                comp_path=draina_damage,
                raster_path=raster_path,
                vul_db=vul_db,
                hazard_type=hz_key,
            )
            write_damage_by_oid(draina_damage, draina_damage, oid_to_loss_drain, field_name)
            for oid, v in oid_to_vul_drain.items():
                vul_mem_drain[hz_key][tr][oid] = float(v)

    # 14) Compute DAE fields per component and total
    for fc in [road_damage, bridge_damage, tunnel_damage, draina_damage]:
        if fc and arcpy.Exists(fc):
            compute_DAE_fields(fc, hazard_to_TRs_sorted)

    # 15) Ensure per-component and total DAE fields on road layer
    for f in ["DAE_bridge", "DAE_tunnel", "DAE_drainage", "DAE_total"]:
        ensure_field(road_damage, f, "DOUBLE")

    # 16) Aggregate component DAE by tramo and write totals
    bridge_tramo_dae = sum_component_DAE_by_tramo(bridge_damage) if bridge_damage and arcpy.Exists(bridge_damage) else {}
    tunnel_tramo_dae = sum_component_DAE_by_tramo(tunnel_damage) if tunnel_damage and arcpy.Exists(tunnel_damage) else {}
    drain_tramo_dae  = sum_component_DAE_by_tramo(draina_damage) if draina_damage and arcpy.Exists(draina_damage) else {}
    with arcpy.da.UpdateCursor(road_damage, [id_field, "DAE", "DAE_bridge", "DAE_tunnel", "DAE_drainage", "DAE_total"]) as cur:
        for tramo, dae_r, dae_b, dae_t, dae_d, dae_tot in cur:
            b = float(bridge_tramo_dae.get(tramo, 0.0))
            t = float(tunnel_tramo_dae.get(tramo, 0.0))
            d = float(drain_tramo_dae.get(tramo, 0.0))
            r = 0.0 if dae_r is None else float(dae_r)
            cur.updateRow([tramo, r, b, t, d, r + b + t + d])

    # 17) Run road-loss analysis and compute and write PAE fields
    if operat_data and operat_data.strip() and gdppca_doub and str(gdppca_doub).strip():
        dlt_by_oid = road_loss_analysis(road_damage, operat_data, float(gdppca_doub))
        tramo_to_dlt = tramo_dlt_from_roads(road_damage, dlt_by_oid)
    else:
        dlt_by_oid = {}
        tramo_to_dlt = {}
    compute_PAE_fields(road_damage, hazard_to_TRs_sorted, dlt_by_oid, vul_mem_roads)
    if bridge_damage and arcpy.Exists(bridge_damage):
        dlt_bridge_by_oid = map_component_dlt_by_tramo(bridge_damage, tramo_to_dlt)
        compute_PAE_fields(bridge_damage, hazard_to_TRs_sorted, dlt_bridge_by_oid, vul_mem_bridge)
    if tunnel_damage and arcpy.Exists(tunnel_damage):
        dlt_tunnel_by_oid = map_component_dlt_by_tramo(tunnel_damage, tramo_to_dlt)
        compute_PAE_fields(tunnel_damage, hazard_to_TRs_sorted, dlt_tunnel_by_oid, vul_mem_tunnel)
    if draina_damage and arcpy.Exists(draina_damage):
        dlt_drain_by_oid = map_component_dlt_by_tramo(draina_damage, tramo_to_dlt)
        compute_PAE_fields(draina_damage, hazard_to_TRs_sorted, dlt_drain_by_oid, vul_mem_drain)

    # 18) Create Priority field = DAE_total + PAE_total
    for fc in [bridge_damage, tunnel_damage, draina_damage]:
        if fc and arcpy.Exists(fc):
            ensure_field(fc, "Priority", "DOUBLE")
            with arcpy.da.UpdateCursor(fc, ["DAE", "PAE_total", "Priority"]) as cur:
                for dae_tot, pae_tot, _ in cur:
                    d = 0.0 if dae_tot in (None, "") else float(dae_tot)
                    p = 0.0 if pae_tot in (None, "") else float(pae_tot)
                    cur.updateRow([dae_tot, pae_tot, d + p])
    ensure_field(road_damage, "Priority", "DOUBLE")
    with arcpy.da.UpdateCursor(road_damage, ["DAE_total", "PAE_total", "Priority"]) as cur:
        for dae_tot, pae_tot, _ in cur:
            d = 0.0 if dae_tot in (None, "") else float(dae_tot)
            p = 0.0 if pae_tot in (None, "") else float(pae_tot)
            cur.updateRow([dae_tot, pae_tot, d + p])

    # 19) Apply modified TRs per scenario (river/coast only)
    if mod_tp_poly and arcpy.Exists(mod_tp_poly):
        scen_map = parse_tp_fields(mod_tp_poly)
        for scen, tp_fields in scen_map.items():

            # 19a) Apply TP-based modified TRs to all components
            apply_TRmods(road_damage, mod_tp_poly, scen, tp_fields, is_roads=True)
            if bridge_damage and arcpy.Exists(bridge_damage):
                apply_TRmods(bridge_damage, mod_tp_poly, scen, tp_fields, is_roads=False)
            if tunnel_damage and arcpy.Exists(tunnel_damage):
                apply_TRmods(tunnel_damage, mod_tp_poly, scen, tp_fields, is_roads=False)
            if draina_damage and arcpy.Exists(draina_damage):
                apply_TRmods(draina_damage, mod_tp_poly, scen, tp_fields, is_roads=False)

            # 19b) Compute modified hazard totals (river/coast + baseline EQ/tsunami)
            compute_mod_totals(road_damage, scen)
            compute_mod_totals(bridge_damage, scen)
            compute_mod_totals(tunnel_damage, scen)
            compute_mod_totals(draina_damage, scen)        

            # 19c) Ensure new scenario fields exist on roads
            for f in [f"DAE_bridge_mod_{scen}", f"DAE_tunnel_mod_{scen}", f"DAE_drainage_mod_{scen}", f"DAE_total_mod_{scen}", f"Priority_mod_{scen}"]:
                ensure_field(road_damage, f, "DOUBLE")

            # 19d) Sum component DAE_mod_{scen} by tramo
            bmap = sum_component_DAE_by_tramo(bridge_damage, f"DAE_mod_{scen}") if bridge_damage and arcpy.Exists(bridge_damage) else {}
            tmap = sum_component_DAE_by_tramo(tunnel_damage, f"DAE_mod_{scen}") if tunnel_damage and arcpy.Exists(tunnel_damage) else {}
            dmap = sum_component_DAE_by_tramo(draina_damage, f"DAE_mod_{scen}") if draina_damage and arcpy.Exists(draina_damage) else {}

            # 19e) Write component DAE_*_mod and compute DAE_total_mod_{scen}
            with arcpy.da.UpdateCursor(
                road_damage, [id_field, f"DAE_mod_{scen}", f"DAE_bridge_mod_{scen}", f"DAE_tunnel_mod_{scen}", f"DAE_drainage_mod_{scen}", f"DAE_total_mod_{scen}"]
            ) as cur:
                for tramo, r_dae_mod, _, _, _, _ in cur:
                    r = 0.0 if r_dae_mod in (None, "") else float(r_dae_mod)
                    b = float(bmap.get(tramo, 0.0))
                    t = float(tmap.get(tramo, 0.0))
                    d = float(dmap.get(tramo, 0.0))
                    cur.updateRow([tramo, r, b, t, d, r + b + t + d])

            # 19f) Compute Priority_mod_{scen} = DAE_total_mod_{scen} + PAE_total_mod_{scen}
            with arcpy.da.UpdateCursor(road_damage, [f"DAE_total_mod_{scen}", f"PAE_total_mod_{scen}", f"Priority_mod_{scen}"]) as cur:
                for dae_tot, pae_tot, _ in cur:
                    d = 0.0 if dae_tot in (None, "") else float(dae_tot)
                    p = 0.0 if pae_tot in (None, "") else float(pae_tot)
                    cur.updateRow([dae_tot, pae_tot, d + p])
    
    # 20) Try to add outputs to current ArcGIS Pro map
    try:
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        m = aprx.activeMap
        for fc in [road_damage, bridge_damage, tunnel_damage, draina_damage]:
            if fc and arcpy.Exists(fc):
                m.addDataFromPath(fc)
    except Exception as ex:
        arcpy.AddWarning(f"Could not add outputs to map: {ex}")

    # 21) Set multi-value outputs for tool parameters
    for idx, fc in [(14, road_damage), (15, bridge_damage), (16, tunnel_damage), (17, draina_damage)]:
        arcpy.SetParameterAsText(idx, fc if (fc and arcpy.Exists(fc)) else "")
    arcpy.AddMessage("✅ Computation complete.")

if __name__ == "__main__":
    main()
