# -*- coding: utf-8 -*-
"""Kiem tra moi dan chieu file:dong trong DECISIONS.md va TASKS.md tro dung cho.
Chay lai sau MOI lan sua MATRIX_v0.md hay SPEC_A.md (rui ro R11)."""
import io, re, sys, os
ROOT = sys.argv[1]

EXPECT = {
    ('docs/MATRIX_v0.md', 4): 'Chưa xác minh',
    ('docs/MATRIX_v0.md', 11): 'bất đối xứng',
    ('docs/MATRIX_v0.md', 12): 'Mechanism / Effect',
    ('docs/MATRIX_v0.md', 13): 'VẮNG MẶT',
    ('docs/MATRIX_v0.md', 14): 'quét đầy đủ',
    ('docs/MATRIX_v0.md', 15): 'audit_<commit>.log.jsonl',
    ('docs/MATRIX_v0.md', 16): 'tự chạy',
    ('docs/MATRIX_v0.md', 17): 'NGUYÊN VĂN',
    ('docs/MATRIX_v0.md', 18): 'Chỉ chép các dòng',
    ('docs/MATRIX_v0.md', 24): '| M01 |',
    ('docs/MATRIX_v0.md', 27): '| M04 |',
    ('docs/MATRIX_v0.md', 28): '| M05 |',
    ('docs/MATRIX_v0.md', 29): '| M06 |',
    ('docs/INTERFACE.md', 5): 'không mô tả logic bên trong',
    ('docs/MATRIX_v0.md', 30): '| M07 |',
    ('docs/MATRIX_v0.md', 31): '| M08 |',
    ('docs/MATRIX_v0.md', 33): '| M10 |',
    ('docs/MATRIX_v0.md', 34): '| M11 |',
    ('docs/MATRIX_v0.md', 35): '| M12 |',
    ('docs/MATRIX_v0.md', 39): 'Phân phối giá theo',
    ('docs/MATRIX_v0.md', 40): 'Tỷ lệ được ghép',
    ('docs/MATRIX_v0.md', 48): 'Cột Bằng chứng là',
    ('docs/SPEC_A.md', 11): 'nguyên tắc phủ nhánh',
    ('docs/SPEC_A.md', 15): 'Chuyến ngoài vùng phủ',
    ('docs/SPEC_A.md', 22): 'drivers.json',
    ('docs/SPEC_A.md', 24): 'rides.json',
    ('docs/SPEC_A.md', 26): 'match(ride, drivers, config)',
    ('docs/SPEC_A.md', 28): 'auto_accept',
    ('docs/SPEC_A.md', 30): 'idle',
    ('docs/SPEC_A.md', 31): 'haversine',
    ('docs/SPEC_A.md', 32): 'trips_today',
    ('docs/SPEC_A.md', 33): 'acceptance_rate',
    ('docs/SPEC_A.md', 38): 'fare(distance_km, requested_at, config)',
    ('docs/SPEC_A.md', 46): 'Mở cửa',
    ('docs/SPEC_A.md', 49): 'Km 26+',
    ('docs/SPEC_A.md', 50): '0h–6h',
    ('docs/SPEC_A.md', 53): 'Trần hệ số',
    ('docs/SPEC_A.md', 65): 'danh sách thuộc tính được phép',
    ('docs/SPEC_A.md', 66): 'mô tả logic bên trong',
    ('CLAUDE.md', 30): 'Quy trình bắt buộc',
    ('docs/GREEN_SM_CONTEXT.md', 15): '70%',
    ('docs/GREEN_SM_CONTEXT.md', 22): 'Hà Lan',
    ('.claude/agents/coder-auditor.md', 7): 'CHỈ đọc',
}

cache = {}
def lines(rel):
    if rel not in cache:
        cache[rel] = io.open(os.path.join(ROOT, rel), encoding='utf-8').read().split('\n')
    return cache[rel]

bad = 0
for (rel, n), needle in sorted(EXPECT.items()):
    L = lines(rel)
    got = L[n - 1] if 0 < n <= len(L) else '<NGOAI PHAM VI>'
    ok = needle in got
    if not ok:
        bad += 1
    print('%s %s:%d  mong "%s"  -> %s' % ('OK  ' if ok else 'SAI ', rel, n, needle, got[:70]))

# Moi dan chieu dang ton tai phai nam trong bang EXPECT, neu khong thi chua kiem
print('\n--- Dan chieu co trong file nhung CHUA duoc kiem ---')
known = set()
for (rel, n) in EXPECT:
    known.add((os.path.basename(rel), n))
unchecked = 0
for f in ('docs/DECISIONS.md', 'docs/TASKS.md'):
    txt = io.open(os.path.join(ROOT, f), encoding='utf-8').read()
    for tok in re.findall(r'([A-Za-z_0-9\-]+\.md):([0-9]+(?:[,\-][0-9]+)*)', txt):
        base, nums = tok
        for part in re.split(r'[,\-]', nums):
            if (base, int(part)) not in known:
                print('  CHUA KIEM:', base + ':' + part, '(trong ' + f + ')')
                unchecked += 1
if not unchecked:
    print('  khong co')

print('\nSO DAN CHIEU SAI:', bad, '| SO DAN CHIEU CHUA KIEM:', unchecked)
sys.exit(1 if (bad or unchecked) else 0)
