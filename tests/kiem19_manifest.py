# -*- coding: utf-8 -*-
"""Kiem 19 — canh nguyen tac phu nhanh cua Bach (DECISIONS Q19):
   moi nhanh quyet dinh cua A phai duoc chay it nhat mot lan tren mock data.

   Va sinh manifest du 4 truong tai lap theo dieu kien (b) Bach dat cho Q12:
   commit, seed, lenh, run_id."""
import collections, glob, hashlib, io, json, os, re, subprocess, sys

ROOT, BACKUP, EV = sys.argv[1], sys.argv[2], sys.argv[3]
COMMIT_AT_RUN = sys.argv[4] if len(sys.argv) > 4 else None
os.chdir(ROOT)
FAIL = 0

def rows(mod):
    p = 'logs/%s_%s.jsonl' % (mod, EV)
    if not os.path.exists(p):
        return
    for ln in io.open(p, encoding='utf-8'):
        ln = ln.strip()
        if ln:
            yield json.loads(ln)

# ---------------- thu thap ----------------
rep_path = 'reports/product_run_%s.json' % EV
rep = json.load(io.open(rep_path, encoding='utf-8')) if os.path.exists(rep_path) else None

tier = collections.Counter()
for o in rows('pricing'):
    if o.get('event') == 'fare_tier':
        tier[((o.get('inputs') or {}).get('tier_id', '?'), o.get('reason') or '')] += 1

cand_reason = collections.Counter()
for o in rows('matching'):
    if o.get('event') == 'candidate_eval':
        cand_reason[o.get('reason')] += 1

coef = collections.Counter(r['time_coef'] for r in (rep['results'] if rep else []))
auto = collections.Counter(r['auto_accept'] for r in (rep['results'] if rep else []))
n_unm = rep['summary']['n_unmatched'] if rep else None
n_rides = rep['summary']['n_rides'] if rep else 0

def charged(t):
    return tier.get((t, 'tier_charged_per_km'), 0)

# ---------------- kiem 19 ----------------
print('=== KIEM 19 — nguyen tac phu nhanh (Bach chot 19/10, DECISIONS Q19) ===')
print('    run_id = %s | %d chuyen\n' % (EV, n_rides))
lo, hi = int(n_rides * 0.03), int(n_rides * 0.05)
items = [
    ('a', 'nhanh khong ghep duoc tai xe (3-5%% cua %d = %d..%d)' % (n_rides, lo, hi),
     n_unm is not None and lo <= n_unm <= hi, 'n_unmatched = %s' % n_unm),
    ('b', 'bac `opening` co chuyen duoc tinh tien',
     tier.get(('opening', 'tier_flat_applied'), 0) > 0,
     '%d chuyen' % tier.get(('opening', 'tier_flat_applied'), 0)),
    ('c', 'bac `t2` co chuyen duoc tinh tien', charged('t2') > 0, '%d chuyen' % charged('t2')),
    ('d', 'bac `t3` co chuyen duoc tinh tien', charged('t3') > 0, '%d chuyen' % charged('t3')),
    ('e', 'bac `t4` co chuyen duoc tinh tien', charged('t4') > 0, '%d chuyen' % charged('t4')),
    ('f', 'ca ba he so gio 0.9 / 1.0 / 1.2 deu co chuyen',
     all(coef.get(x, 0) > 0 for x in (0.9, 1.0, 1.2)),
     ' '.join('%.1f:%d' % (x, coef.get(x, 0)) for x in (0.9, 1.0, 1.2))),
    ('g', 'auto_accept co ca True va False',
     auto.get(True, 0) > 0 and auto.get(False, 0) > 0,
     'True:%d False:%d' % (auto.get(True, 0), auto.get(False, 0))),
    ('h', 'bon ly do loai ung vien deu xuat hien',
     all(cand_reason.get(r, 0) > 0 for r in
         ('not_idle', 'wrong_vehicle_type', 'out_of_radius', 'kept_as_candidate')),
     ' '.join('%s:%d' % (r, cand_reason.get(r, 0)) for r in
              ('not_idle', 'wrong_vehicle_type', 'out_of_radius', 'kept_as_candidate'))),
]
bad = []
for k, name, ok, detail in items:
    if not ok:
        bad.append(k)
    print('  [%s] %s. %-52s %s' % ('PASS' if ok else 'FAIL', k, name, detail))

# candidate_eval phai van dung 200 dong moi chuyen
ndrv = len(json.load(io.open('product/data/drivers.json', encoding='utf-8')))
per = collections.Counter()
for o in rows('matching'):
    if o.get('event') == 'candidate_eval':
        per[(o.get('inputs') or {}).get('ride_id')] += 1
vals = sorted(set(per.values()))
ok200 = vals == [ndrv]
if not ok200:
    bad.append('i')
print('  [%s] i. %-55s %s dong/chuyen (drivers=%d)'
      % ('PASS' if ok200 else 'FAIL', 'candidate_eval van du moi tai xe, ke ca chuyen ngoai vung', vals, ndrv))

# muc j — pm phat hien (DECISIONS Q19): nhanh pha hoa trong match() chua bao
# gio chay THAT tren du lieu bang chung. tie_break ghi log moi chuyen nhung
# luon la 'no_tie' -> ghi log moi chuyen KHONG co nghia la nhanh re da chay.
# Day la nhan biet, khong phai chan doan: chan doan rieng o tests/kiem21_tiebreak.py
# (goi match() truc tiep, KHONG dung mock_data.json). Muc j luon FAIL cho toi
# khi Bach quyet co dua hoa thuc vao du lieu mac dinh hay khong.
tie_reasons = collections.Counter()
for o in rows('matching'):
    if o.get('event') == 'tie_break':
        tie_reasons[o.get('reason')] += 1
co_hoa_that = bool(tie_reasons) and set(tie_reasons) != {'no_tie'}
if not co_hoa_that:
    bad.append('j')
print('  [%s] j. %-55s %s'
      % ('PASS' if co_hoa_that else 'FAIL',
         'nhanh pha hoa trong match() co hoa THAT (SPEC_A.md:32)',
         dict(tie_reasons) or '(khong co dong tie_break)'))
if not co_hoa_that:
    print('       -> chan doan rieng: tests/kiem21_tiebreak.py (goi match() truc tiep,')
    print('          KHONG dung mock_data.json) da xac nhan code DUNG khi bi buoc hoa.')
    print('          Muc nay FAIL vi so lan hoa THAT tren du lieu mac dinh van la 0.')
    print('          Dua hoa thuc vao du lieu la quyet dinh cua Bach, khong phai lead tu lam.')

if bad:
    FAIL += 1
    print('\n  => KIEM 19 FAIL o muc: %s' % ', '.join(bad))
else:
    print('\n  => KIEM 19 PASS: moi nhanh quyet dinh da chay it nhat mot lan')

# ---------------- manifest du 4 truong tai lap ----------------
print('\n=== MANIFEST — dieu kien (b) cua Bach: commit, seed, lenh, run_id ===')
def git(*a):
    return subprocess.run(('git',) + a, capture_output=True, text=True).stdout.strip()

# pm bat dung: truong `commit` cu ghi commit luc VIET manifest, khong phai luc CHAY.
# Lan chay 081010446 xay ra khi HEAD con la 91513cc; a79bdcf la commit XOA bao cao.
# Vo hai do may (product/ khong doi), nhung lan sau se NOI SAI ma van trong hop le.
commit_now = git('rev-parse', 'HEAD')
commit_run = git('rev-parse', COMMIT_AT_RUN) if COMMIT_AT_RUN else commit_now
dirty = git('status', '--porcelain')
# Hash cay cua rieng product/ — chi doi khi product/ that su doi, nen commit chi
# sua docs/ khong lam nhieu bang chung.
tree_now = git('rev-parse', commit_now + ':product')
tree_run = git('rev-parse', commit_run + ':product')
seed = json.load(io.open('product/config/mock_data.json', encoding='utf-8')).get('seed')
logs = sorted(glob.glob('logs/*_%s.jsonl' % EV))
man = {
    'schema_version': '0.3',
    'note': 'Manifest log cua lan chay bang chung. logs/*.jsonl va reports/product_run_*.json '
            'KHONG vao git (DECISIONS Q12, Q20). File nay la bang chung kiem chung duoc cho ban '
            'sao luu ngoai repo. Bang chung dang log khong kem @commit — ngoai le da chuan thuan '
            'trong Quy uoc MATRIX_v0.',
    'run_id': EV,
    'commit_at_run': commit_run,
    'commit_at_manifest': commit_now,
    'product_tree_at_run': tree_run,
    'product_tree_at_manifest': tree_now,
    'product_unchanged_since_run': tree_run == tree_now and tree_run != '',
    'worktree_clean': dirty == '',
    'command': 'python product/run_product.py',
    'seed': seed,
    'files': [],
}
for p in logs:
    n = sum(1 for ln in io.open(p, encoding='utf-8') if ln.strip())
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    man['files'].append({'path': p.replace('\\', '/'), 'lines': n,
                         'bytes': os.path.getsize(p), 'sha256': h.hexdigest()})
man['total_lines'] = sum(x['lines'] for x in man['files'])
man['total_bytes'] = sum(x['bytes'] for x in man['files'])
mp = 'reports/logs_manifest_%s.json' % EV
io.open(mp, 'w', encoding='utf-8', newline='\n').write(json.dumps(man, ensure_ascii=False, indent=2) + '\n')
if not man['product_unchanged_since_run']:
    FAIL += 1
    print('  [FAIL] product/ da doi giua luc chay va luc viet manifest: %s -> %s'
          % (tree_run[:12], tree_now[:12]))
else:
    print('  [PASS] product/ khong doi giua luc chay va luc viet manifest (%s)' % tree_run[:12])
for k in ('run_id', 'commit_at_run', 'commit_at_manifest', 'product_tree_at_run',
          'product_unchanged_since_run', 'worktree_clean', 'command', 'seed'):
    print('  %-15s %s' % (k, man[k]))
print('  %-15s %d file, %d dong, %.1f MB' % ('files', len(man['files']), man['total_lines'], man['total_bytes'] / 1e6))
print('  -> %s' % mp)

# ---------------- kiem 18 ----------------
print('\n=== KIEM 18 — manifest khop ban sao luu ngoai repo ===')
bad18 = []
for x in man['files']:
    b = os.path.join(BACKUP, os.path.basename(x['path']))
    if not os.path.exists(b):
        bad18.append('thieu ' + os.path.basename(x['path'])); continue
    h = hashlib.sha256()
    with open(b, 'rb') as fh:
        for c in iter(lambda: fh.read(1 << 20), b''):
            h.update(c)
    if h.hexdigest() != x['sha256']:
        bad18.append('lech ' + os.path.basename(x['path']))
if bad18:
    FAIL += 1
    print('  [FAIL] %s' % '; '.join(bad18))
else:
    print('  [PASS] %d/%d file khop sha256' % (len(man['files']), len(man['files'])))

print('\n' + '=' * 70)
print('KET QUA: %d nhom FAIL' % FAIL)
sys.exit(1 if FAIL else 0)
