"""Ghi log JSONL cho san pham mau A.

Rang buoc cung CLAUDE.md §3: moi dong log co du 9 truong
ts, run_id, module, func, event, inputs, outputs, decision, reason.
Duong dan: logs/<module>_<run_id>.jsonl
run_id: YYYYmmddTHHMMSS theo UTC, dung chung cho moi module trong 1 lan chay.

[Suy luan] Day la sandbox mo phong, khong phai san pham that.
"""

import atexit
import json
import os
from datetime import datetime, timezone

# Thu tu 9 truong bat buoc. Hang so nay DUOC DUNG de dung tung ban ghi log
# trong JsonlLogger.log(), nen thu tu truong trong file log luon bang thu tu o day.
REQUIRED_FIELDS = (
    "ts",
    "run_id",
    "module",
    "func",
    "event",
    "inputs",
    "outputs",
    "decision",
    "reason",
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(REPO_ROOT, "logs")

_PROCESS_RUN_ID = None


def rel(path):
    """Duong dan tuong doi so voi goc repo, dung POSIX separator.

    Path nam ngoai o dia cua repo thi khong co duong dan tuong doi; tra ve
    nguyen path thay vi bao loi, de viec ghi log khong bao gio lam vo luong
    chay cua nguoi goi.
    """
    try:
        return os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
    except ValueError:
        return str(path).replace(os.sep, "/")


def enable_utf8_stdout():
    """Tranh UnicodeEncodeError khi console Windows dung codepage cp1252."""
    import sys

    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def make_run_id():
    """run_id dinh dang YYYYmmddTHHMMSS theo UTC."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")


def process_run_id():
    """run_id dung chung cho ca tien trinh.

    Dung cho cac logger du phong, de log cua nhieu module trong cung mot tien
    trinh van doi chieu cheo duoc voi nhau qua run_id.
    """
    global _PROCESS_RUN_ID
    if _PROCESS_RUN_ID is None:
        _PROCESS_RUN_ID = make_run_id()
    return _PROCESS_RUN_ID


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


class JsonlLogger:
    """Mot logger ung voi mot module, ghi ra logs/<module>_<run_id>.jsonl.

    File mo bang mode "x": neu file da ton tai thi vo ngay bang FileExistsError
    thay vi ghi de im lang bang chung cua lan chay truoc. run_id chi co do phan
    giai 1 giay, nen hai lan chay trong cung mot giay se dung cung ten file.
    """

    def __init__(self, module, run_id, log_dir=None, autoflush=False):
        self.module = module
        self.run_id = run_id
        self.log_dir = log_dir or LOG_DIR
        self.autoflush = autoflush
        os.makedirs(self.log_dir, exist_ok=True)
        self.path = os.path.join(self.log_dir, "%s_%s.jsonl" % (module, run_id))
        self._fh = open(self.path, "x", encoding="utf-8", newline="\n")
        self._context = {}
        self.line_count = 0
        self.decision_count = 0

    def set_context(self, context):
        """Gan cac khoa doi chieu (vi du ride_id) cho cac dong log ke tiep.

        Context do nguoi goi cung cap.
        """
        self._context = dict(context) if context else {}

    def clear_context(self):
        self._context = {}

    def log(self, func, event, inputs=None, outputs=None, decision=None, reason=""):
        values = (
            _now_iso(),
            self.run_id,
            self.module,
            func,
            event,
            self._merge_context(inputs),
            outputs if outputs is not None else {},
            decision,
            reason,
        )
        record = dict(zip(REQUIRED_FIELDS, values))
        self._fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        self.line_count += 1
        if decision is not None:
            self.decision_count += 1
        if self.autoflush:
            self._fh.flush()

    def _merge_context(self, inputs):
        data = dict(inputs) if inputs else {}
        for key, value in self._context.items():
            data.setdefault(key, value)
        return data

    def flush(self):
        if not self._fh.closed:
            self._fh.flush()

    def close(self):
        if not self._fh.closed:
            self._fh.flush()
            self._fh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False


def make_fallback_logger(module):
    """Logger du phong cho truong hop nguoi goi khong truyen logger.

    Dung run_id cua ca tien trinh de doi chieu cheo duoc giua cac module, ghi
    thang tung dong (autoflush) va dong lai luc tien trinh ket thuc, de khong
    mat phan cuoi bo dem khi tien trinh ket thuc bat thuong.
    """
    logger = JsonlLogger(module, process_run_id(), autoflush=True)
    atexit.register(logger.close)
    return logger


def load_json_config(path, logger=None):
    """Doc mot file config JSON. Moi file config bat buoc co truong version.

    Thieu version la mot quyet dinh ve du lieu nghiep vu doc tu config, nen
    ghi log truoc khi bao loi (CLAUDE.md §3). Logger do nguoi goi truyen vao.
    """
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if "version" not in data:
        if logger is not None:
            logger.log(
                func="load_json_config",
                event="config_version_missing",
                inputs={"config_path": rel(path), "keys": sorted(data.keys())},
                outputs={},
                decision=None,
                reason="config_thieu_truong_version",
            )
        raise ValueError("Config thieu truong 'version': %s" % path)
    return data
