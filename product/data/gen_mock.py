"""Sinh du lieu tong hop cho san pham mau A (SPEC_A §1).

Du lieu 100% tong hop, seed co dinh lay tu product/config/mock_data.json.
Khong co ten, so dien thoai, bien so, dia chi that.
Chay 2 lan phai ra 3 file JSON giong het nhau.

Chay: python product/data/gen_mock.py
"""

import json
import os
import random
import sys
from datetime import datetime, timedelta, timezone

_DATA_DIR = os.path.dirname(os.path.abspath(__file__))
_PRODUCT_DIR = os.path.dirname(_DATA_DIR)
if _PRODUCT_DIR not in sys.path:
    sys.path.insert(0, _PRODUCT_DIR)

from logger import (  # noqa: E402
    JsonlLogger,
    enable_utf8_stdout,
    load_json_config,
    make_run_id,
    rel,
)

CONFIG_PATH = os.path.join(_PRODUCT_DIR, "config", "mock_data.json")
DRIVERS_PATH = os.path.join(_DATA_DIR, "drivers.json")
CUSTOMERS_PATH = os.path.join(_DATA_DIR, "customers.json")
RIDES_PATH = os.path.join(_DATA_DIR, "rides.json")

_SECONDS_PER_DAY = 24 * 60 * 60


def _make_id(prefix, index, width):
    return "%s%0*d" % (prefix, width, index)


def _weighted(rnd, weights):
    keys = list(weights.keys())
    return rnd.choices(keys, weights=[weights[k] for k in keys], k=1)[0]


def _coord(rnd, low, high, decimals):
    return round(rnd.uniform(low, high), decimals)


def _write_json(path, payload):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def generate(config, logger):
    """Sinh 3 bang du lieu tong hop tu config. Tra ve dict 3 danh sach."""
    rnd = random.Random(config["seed"])
    bbox = config["bbox"]
    decimals = config["coord_decimals"]
    counts = config["counts"]
    idf = config["id_format"]
    ar_lo, ar_hi = config["acceptance_rate_range"]
    ar_dec = config["acceptance_rate_decimals"]
    trips_lo, trips_hi = config["trips_today_range"]

    logger.log(
        func="generate",
        event="gen_start",
        inputs={
            "seed": config["seed"],
            "config_version": config["version"],
            "bbox": bbox,
            "counts": counts,
        },
        outputs={},
        decision=None,
        reason="bat_dau_sinh_du_lieu_tong_hop",
    )

    drivers = []
    for i in range(1, counts["drivers"] + 1):
        record = {
            "driver_id": _make_id(idf["driver_prefix"], i, idf["width"]),
            "lat": _coord(rnd, bbox["lat_min"], bbox["lat_max"], decimals),
            "lon": _coord(rnd, bbox["lon_min"], bbox["lon_max"], decimals),
            "status": _weighted(rnd, config["driver_status_weights"]),
            "vehicle_type": _weighted(rnd, config["vehicle_type_weights"]),
            "acceptance_rate": round(rnd.uniform(ar_lo, ar_hi), ar_dec),
            "trips_today": rnd.randint(trips_lo, trips_hi),
        }
        drivers.append(record)
        logger.log(
            func="generate",
            event="record_generated",
            inputs={"table": "drivers", "index": i},
            outputs=record,
            decision=None,
            reason="sinh_ban_ghi_tai_xe_tong_hop",
        )

    customers = []
    for i in range(1, counts["customers"] + 1):
        record = {
            "customer_id": _make_id(idf["customer_prefix"], i, idf["width"]),
            "segment": _weighted(rnd, config["customer_segment_weights"]),
        }
        customers.append(record)
        logger.log(
            func="generate",
            event="record_generated",
            inputs={"table": "customers", "index": i},
            outputs=record,
            decision=None,
            reason="sinh_ban_ghi_khach_hang_tong_hop",
        )

    base_date = config["base_date"]
    tz = timezone(timedelta(hours=config["utc_offset_hours"]))
    day_start = datetime.fromisoformat(base_date).replace(tzinfo=tz)
    customer_ids = [c["customer_id"] for c in customers]
    n_rides = counts["rides"]

    rides = []
    for i in range(1, n_rides + 1):
        offset_seconds = (i - 1) * _SECONDS_PER_DAY // n_rides
        requested_at = (day_start + timedelta(seconds=offset_seconds)).isoformat()
        record = {
            "ride_id": _make_id(idf["ride_prefix"], i, idf["width"]),
            "customer_id": rnd.choice(customer_ids),
            "vehicle_type": _weighted(rnd, config["vehicle_type_weights"]),
            "pickup_lat": _coord(rnd, bbox["lat_min"], bbox["lat_max"], decimals),
            "pickup_lon": _coord(rnd, bbox["lon_min"], bbox["lon_max"], decimals),
            "dropoff_lat": _coord(rnd, bbox["lat_min"], bbox["lat_max"], decimals),
            "dropoff_lon": _coord(rnd, bbox["lon_min"], bbox["lon_max"], decimals),
            "requested_at": requested_at,
        }
        rides.append(record)
        logger.log(
            func="generate",
            event="record_generated",
            inputs={"table": "rides", "index": i, "offset_seconds": offset_seconds},
            outputs=record,
            decision=None,
            reason="sinh_ban_ghi_chuyen_tong_hop",
        )

    return {"drivers": drivers, "customers": customers, "rides": rides}


def write_tables(tables, logger):
    for name, path in (
        ("drivers", DRIVERS_PATH),
        ("customers", CUSTOMERS_PATH),
        ("rides", RIDES_PATH),
    ):
        _write_json(path, tables[name])
        logger.log(
            func="write_tables",
            event="table_written",
            inputs={"table": name, "path": rel(path)},
            outputs={"n_records": len(tables[name])},
            decision=None,
            reason="ghi_bang_du_lieu_tong_hop_ra_dia",
        )


def main(run_id=None):
    enable_utf8_stdout()
    run_id = run_id or make_run_id()
    logger = JsonlLogger("gen_mock", run_id)
    try:
        config = load_json_config(CONFIG_PATH, logger=logger)
        tables = generate(config, logger)
        write_tables(tables, logger)
        logger.log(
            func="main",
            event="gen_end",
            inputs={"run_id": run_id, "config_version": config["version"]},
            outputs={
                "n_drivers": len(tables["drivers"]),
                "n_customers": len(tables["customers"]),
                "n_rides": len(tables["rides"]),
                "log_file": os.path.basename(logger.path),
            },
            decision=None,
            reason="sinh_du_lieu_tong_hop_xong",
        )
    finally:
        logger.close()
    print("gen_mock run_id=%s" % run_id)
    print("  drivers   -> %s (%d)" % (rel(DRIVERS_PATH), len(tables["drivers"])))
    print("  customers -> %s (%d)" % (rel(CUSTOMERS_PATH), len(tables["customers"])))
    print("  rides     -> %s (%d)" % (rel(RIDES_PATH), len(tables["rides"])))
    print("  log       -> %s" % rel(logger.path))
    return tables


if __name__ == "__main__":
    main()
