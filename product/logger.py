"""Ghi log JSON Lines cho san pham mau A.

Rang buoc cung CLAUDE.md §3: moi dong log co du 9 truong
ts, run_id, module, func, event, inputs, outputs, decision, reason.
Duong dan: logs/<module>_<run_id>.jsonl
run_id: YYYYmmddTHHMMSS theo UTC, dung chung cho moi module trong 1 lan chay.

[Suy luan] Day la sandbox mo phong, khong phai san pham that.
"""

import json
import os
from datetime import datetime, timezone

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

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(_REPO_ROOT, "logs")


def make_run_id():
    """run_id dinh dang YYYYmmddTHHMMSS theo UTC."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")


def _now_iso():
    return datetime.now(timezone.utc).isoformat()


class JsonlLogger:
    """Mot logger ung voi mot module, ghi ra logs/<module>_<run_id>.jsonl."""

    def __init__(self, module, run_id, log_dir=None):
        self.module = module
        self.run_id = run_id
        self.log_dir = log_dir or LOG_DIR
        os.makedirs(self.log_dir, exist_ok=True)
        self.path = os.path.join(self.log_dir, "%s_%s.jsonl" % (module, run_id))
        self._fh = open(self.path, "w", encoding="utf-8", newline="\n")
        self._context = {}
        self.line_count = 0

    def set_context(self, context):
        """Gan cac khoa doi chieu (vi du ride_id) cho cac dong log ke tiep.

        Context do nguoi goi cung cap, khong phai thuoc tinh ma matching/pricing
        tu doc tu ban ghi dau vao.
        """
        self._context = dict(context) if context else {}

    def clear_context(self):
        self._context = {}

    def log(self, func, event, inputs=None, outputs=None, decision=None, reason=""):
        record = {
            "ts": _now_iso(),
            "run_id": self.run_id,
            "module": self.module,
            "func": func,
            "event": event,
            "inputs": self._merge_context(inputs),
            "outputs": outputs if outputs is not None else {},
            "decision": decision,
            "reason": reason,
        }
        self._fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        self.line_count += 1

    def _merge_context(self, inputs):
        data = dict(inputs) if inputs else {}
        for key, value in self._context.items():
            data.setdefault(key, value)
        return data

    def flush(self):
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


def load_json_config(path):
    """Doc mot file config JSON. Moi file config bat buoc co truong version."""
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if "version" not in data:
        raise ValueError("Config thieu truong 'version': %s" % path)
    return data
