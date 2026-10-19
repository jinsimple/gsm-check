# -*- coding: utf-8 -*-
"""T07 vong 2 — chay lai sau T09b. Da va 2 diem mu cua ban truoc:
   - kiem 14 chi quet matching.py + pricing.py -> gio quet HET product/**/*.py,
     va bo so 2 khoi danh sach vo hai.
   - kiem 9 thieu ca 0 km -> da them.
   Them kiem 15 (nhanh no_driver_in_radius) va kiem 16 (sha256 du lieu trong log).
   Moi kiem theo tung run_id, khong quet gop nhieu lan chay."""
import ast, glob, hashlib, importlib.util, io, json, os, re, subprocess, sys

ROOT = sys.argv[1]
os.chdir(ROOT)
PY = sys.executable
R = []

def rec(n, name, ok, detail):
    R.append((str(n), name, ok, detail))
    print('[%s] kiem %-3s %s — %s' % ('PASS' if ok else 'FAIL', n, name, detail), flush=True)

def sh(*cmd):
    p = subprocess.run([PY] + list(cmd), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return p.returncode, (p.stdout or '') + (p.stderr or '')

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m

PAT = re.compile(r'^logs[/\\](\w+)_([0-9A-Za-z]+)\.jsonl$')
def runs():
    d = {}
    for p in sorted(glob.glob('logs/*.jsonl')):
        m = PAT.match(p.replace('\\', '/'))
        if m:
            d.setdefault(m.group(2), []).append(p)
    return d

def lines_of(paths):
    for p in paths:
        with io.open(p, encoding='utf-8') as f:
            for i, ln in enumerate(f, 1):
                ln = ln.strip()
                if ln:
                    yield p, i, ln

# ---------- don sach roi chay 1 lan lam BANG CHUNG ----------
for f in glob.glob('logs/*.jsonl'):
    os.remove(f)
for f in glob.glob('reports/product_run_*.json'):
    os.remove(f)

rc, out = sh('product/run_product.py')
m = re.search(r'run_id=(\S+)', out)
EV = m.group(1) if m else None
rec(1, 'chay mot lenh', rc == 0 and EV, 'exit=%d | run_id bang chung = %s' % (rc, EV))
EVF = runs().get(EV, [])

# ---------- kiem 2 ----------
files3 = ['product/data/drivers.json', 'product/data/customers.json', 'product/data/rides.json']
before = [sha(f) for f in files3]
rc1, _ = sh('product/data/gen_mock.py'); h1 = [sha(f) for f in files3]
rc2, _ = sh('product/data/gen_mock.py'); h2 = [sha(f) for f in files3]
rec(2, 'seed 42 xac dinh', rc1 == 0 and rc2 == 0 and h1 == h2 == before,
    '2 lan sinh lai ra hash giong nhau VA giong file dang dung: %s' % ', '.join(x[:8] for x in h1))

# ---------- kiem 4: dieu kien tien quyet + 9 truong ----------
named = [p for p in glob.glob('logs/*.jsonl') if PAT.match(p.replace('\\', '/'))]
pre = len(EVF) > 0 and len(named) == len(glob.glob('logs/*.jsonl'))
F9 = ['ts', 'run_id', 'module', 'func', 'event', 'inputs', 'outputs', 'decision', 'reason']
bad, total = [], 0
for p, i, ln in lines_of(EVF):
    total += 1
    o = json.loads(ln, object_pairs_hook=lambda kv: kv)
    if [k for k, _ in o] != F9:
        bad.append('%s:%d' % (p, i))
    if len(bad) > 3:
        break
rec(4, 'log du 9 truong', pre and not bad,
    'tien quyet %s | %d dong, %d dong sai' % ('dat' if pre else 'KHONG DAT', total, len(bad)))

# ---------- kiem 5, 6, 13, 16 trong mot luot, CHI run_id bang chung ----------
ev, cand, reasons, noreason = {}, {}, {}, []
data_sha_logged, mock_ver_logged = None, None
for p, i, ln in lines_of(EVF):
    o = json.loads(ln)
    e = o.get('event'); ev[e] = ev.get(e, 0) + 1
    if o.get('decision') is not None and not (o.get('reason') or '').strip():
        noreason.append('%s:%d' % (p, i))
    if e == 'candidate_eval':
        rid = (o.get('inputs') or {}).get('ride_id')
        cand[rid] = cand.get(rid, 0) + 1
        reasons[o.get('reason')] = reasons.get(o.get('reason'), 0) + 1
    if e == 'data_loaded':
        blob = json.dumps(o, ensure_ascii=False)
        data_sha_logged = [x for x in re.findall(r'[0-9a-f]{64}', blob)]
        mock_ver_logged = 'mock_data' in blob
rec(5, 'quyet dinh co reason', not noreason, '%d quyet dinh thieu reason' % len(noreason))
nd = ev.get('match_result', 0) + ev.get('fare_result', 0)
rec(6, 'so quyet dinh = 2000', nd == 2000,
    'match_result=%d + fare_result=%d = %d' % (ev.get('match_result', 0), ev.get('fare_result', 0), nd))
ndrv = len(json.load(io.open('product/data/drivers.json', encoding='utf-8')))
vals = sorted(set(cand.values()))
rec(13, 'log du ung vien bi loai', len(cand) == 1000 and vals == [ndrv],
    '%d chuyen, %s dong/chuyen (drivers=%d) | %s' % (len(cand), vals, ndrv, reasons))
ok16 = data_sha_logged is not None and len(set(data_sha_logged)) >= 3 and set(data_sha_logged) >= set(h1)
rec(16, 'log data_loaded co sha256 du lieu', ok16,
    '%d sha256 trong log, khop hash 3 file du lieu: %s | co mock_data version: %s'
    % (len(data_sha_logged or []), set(data_sha_logged or []) >= set(h1), mock_ver_logged))

# ---------- kiem 7 ----------
cfgs = sorted(glob.glob('product/config/*.json'))
vers, miss = {}, []
for c in cfgs:
    d = json.load(io.open(c, encoding='utf-8'))
    (vers.__setitem__(os.path.basename(c), d['version']) if 'version' in d else miss.append(c))
rec(7, 'config co version', cfgs and not miss, '%d file: %s' % (len(cfgs), vers))

# ---------- kiem 8 ----------
pyf = sorted(glob.glob('product/**/*.py', recursive=True))
local = {os.path.splitext(os.path.basename(f))[0] for f in pyf}
imp = set()
for f in pyf:
    for n in ast.walk(ast.parse(io.open(f, encoding='utf-8').read(), filename=f)):
        if isinstance(n, ast.Import):
            imp |= {a.name.split('.')[0] for a in n.names}
        elif isinstance(n, ast.ImportFrom) and n.level == 0 and n.module:
            imp.add(n.module.split('.')[0])
out8 = sorted(imp - set(sys.stdlib_module_names) - local)
rec(8, 'chi stdlib', not out8, 'import %s | ngoai stdlib: %s' % (sorted(imp), out8 or 'khong co'))

# ---------- kiem 9: 24 ca, DA THEM 0 km ----------
load('logger', 'product/logger.py')
pricing = load('pricing', 'product/pricing.py')
pc = pricing.load_config()
EXPECT = [
    (0.0, 14, 30000),
    (1.5, 3, 27000), (1.5, 8, 36000), (1.5, 14, 30000),
    (8, 3, 108000), (8, 8, 144000), (8, 14, 120000),
    (30, 3, 380000), (30, 8, 507000), (30, 14, 422000),
    (2.0, 14, 30000), (2.1, 14, 32000), (12.0, 14, 180000),
    (12.1, 14, 182000), (25.0, 14, 362000), (25.1, 14, 364000),
    (8, 0, 108000), (8, 6, 108000), (8, 7, 144000), (8, 9, 144000),
    (8, 17, 144000), (8, 19, 144000), (8, 20, 120000), (8, 23, 120000),
]
f9 = []
for d, h, want in EXPECT:
    got = pricing.fare(d, '2026-10-19T%02d:30:00+07:00' % h, pc)['fare_vnd']
    if got != want:
        f9.append('d=%s h=%d mong %d duoc %d' % (d, h, want, got))
rec(9, 'pricing 24 ca ke ca 0 km', not f9,
    '%d/%d khop' % (len(EXPECT) - len(f9), len(EXPECT)) + ('' if not f9 else ' | ' + '; '.join(f9[:3])))

# ---------- kiem 10 ----------
def attrs(p):
    t = io.open(p, encoding='utf-8').read().split('DANH SÁCH THUỘC TÍNH ĐƯỢC PHÉP', 1)[1]
    return re.findall(r'^\|\s*`([a-z_]+\.[a-z_]+|distance_km|requested_at)`\s*\|', t, re.M)
ad, ai = attrs('docs/DECISIONS.md'), attrs('docs/INTERFACE.md')
rec(10, 'INTERFACE khop Q02', ad == ai and len(ad) == 12, 'DECISIONS %d, INTERFACE %d, khop=%s' % (len(ad), len(ai), ad == ai))

# ---------- kiem 11 ----------
b = sum(os.path.getsize(p) for p in EVF)
tl = sum(1 for _ in lines_of(EVF))
rec(11, 'dung luong log that', True,
    '%d dong | %.1f MB (%.1f MiB) | nguong Q12 = 100 MB -> %s'
    % (tl, b / 1e6, b / 2**20, 'VUOT' if b / 1e6 > 100 else 'khong vuot'))

# ---------- kiem 14: QUET HET product/**/*.py ----------
# Khong whitelist mu. Moi hang so duoc loai tru phai khop CA BA: ten file,
# gia tri, VA chuoi ngu canh tren dong do — kem ly do. In ra moi lan chay.
MIEN = [
    # (duoi ten file, gia tri, chuoi phai co tren dong, ly do)
    (None,              0.0,       None,              'chi so / so sanh zero'),
    (None,              1.0,       None,              'chi so / don vi'),
    ('matching.py',     2.0,       'math.',           'so 2 trong cong thuc haversine (nua goc / binh phuong) — moi dong deu goi math.*'),
    ('matching.py',     6371.0088, None,              'ban kinh Trai Dat, hang toan hoc'),
    ('pricing.py',      1e-09,     None,              'sai so lam tron so thuc, co comment'),
    ('gen_mock.py',     24.0,      '_SECONDS_PER_DAY','quy doi don vi: gio/ngay — KHONG phai tham so nghiep vu'),
    ('gen_mock.py',     60.0,      '_SECONDS_PER_DAY','quy doi don vi: phut/gio va giay/phut'),
    ('run_product.py',  65536.0,   'fh.read',         'co bo dem doc file cho sha256 — hang so ky thuat'),
    ('logger.py',       3.0,       '_RUN_ID_MS_DIGITS',    'so chu so milli giay trong run_id — hang so ky thuat'),
    ('logger.py',       0.001,     '_RUN_ID_RETRY_SLEEP_S','thoi gian nghi khi run_id trung — hang so ky thuat'),
    ('logger.py',       1000.0,    'microsecond',          'quy doi micro -> milli giay'),
    ('pricing.py',      6.0,       '_FLOAT_DECIMALS',      'so chu so lam tron float — hang so ky thuat'),
    ('gen_mock.py',     2.0,       'indent=',              'do thut le khi ghi JSON — hang so ky thuat'),
    ('run_product.py',  2.0,       'indent=',              'do thut le khi ghi JSON — hang so ky thuat'),
]
cfgn = set()
def wn(o):
    if isinstance(o, bool): return
    if isinstance(o, (int, float)): cfgn.add(float(o))
    elif isinstance(o, dict):
        for v in o.values(): wn(v)
    elif isinstance(o, list):
        for v in o: wn(v)
for c in cfgs: wn(json.load(io.open(c, encoding='utf-8')))

def mien_vi(f, v, ctx):
    for suf, val, need, _ly in MIEN:
        if suf and not f.replace('\\', '/').endswith(suf):
            continue
        if abs(val - v) > 1e-12:
            continue
        if need and need not in ctx:
            continue
        return _ly
    return None

left, da_mien = [], []
for f in pyf:
    src = io.open(f, encoding='utf-8').read()
    srcl = src.split('\n')
    for n in ast.walk(ast.parse(src, filename=f)):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            v = float(n.value)
            ctx = srcl[n.lineno - 1].strip()
            # KHONG con bo qua hang so chi vi no trung mot gia tri nao do trong
            # config. Dong cu (`if v in cfgn: continue`) whitelist am tham 20 so
            # nguyen nho — qua danh sach gio [0..6] va [7,8,9,17,18,19] — gom ca
            # 12/13/25/26 la bien bac gia va 17/18/19 la gio cao diem. Mot hang so
            # nghiep vu bi cam vao dung nhung gia tri do se LOT. Va no chay TRUOC
            # MIEN, nen muc mien cho _RUN_ID_MS_DIGITS la code khong bao gio chay:
            # nhin vao thi tuong da sua, that ra chua. Nay moi hang so phai co
            # nguon goc tuong minh trong MIEN.
            ly = mien_vi(f, v, ctx)
            if ly:
                da_mien.append('%s:%d %r (%s)' % (f, n.lineno, n.value, ly))
                continue
            left.append('%s:%d %r  <-- %s' % (f, n.lineno, n.value, ctx[:60]))
rec(14, 'khong hardcode (quet HET product/)', not left,
    '%d file quet | hang so nghiep vu con lai: %s' % (len(pyf), left or 'khong co'))
print('     danh sach mien, co nguon goc (%d chỗ):' % len(da_mien))
for x in sorted(set(da_mien)):
    print('       - %s' % x)

# ---------- kiem 15: nhanh no_driver_in_radius ----------
matching = load('matching', 'product/matching.py')
lg = sys.modules['logger']
mc = dict(matching.load_config())
mc['radius_km'] = 0.0001
rides = json.load(io.open('product/data/rides.json', encoding='utf-8'))
drivers = json.load(io.open('product/data/drivers.json', encoding='utf-8'))
k15id = 'K15DIAG'
for f in glob.glob('logs/*_%s.jsonl' % k15id):
    os.remove(f)
k15log = lg.JsonlLogger('matching', k15id)
res = matching.match(rides[0], drivers, mc, k15log)
k15log.close()
k15lines = [json.loads(l) for _, _, l in lines_of(glob.glob('logs/matching_%s.jsonl' % k15id))]
dec = [l for l in k15lines if l.get('decision') is not None]
ok15 = (res.get('driver_id') is None and 'no_driver_in_radius' in (res.get('reason') or '')
        and len(dec) == 1 and 'no_driver_in_radius' in json.dumps(dec[0], ensure_ascii=False))
rec(15, 'nhanh no_driver_in_radius co log that', ok15,
    'match() -> %s | %d dong log, %d dong quyet dinh, reason=%r'
    % (res, len(k15lines), len(dec), dec[0].get('reason') if dec else None))

# ---------- kiem +: REQUIRED_FIELDS co chiu luc that khong ----------
src = io.open('product/logger.py', encoding='utf-8').read()
used = src.count('REQUIRED_FIELDS')
rec('+', 'REQUIRED_FIELDS chiu luc', used >= 2, 'xuat hien %d lan trong logger.py (1 = hang so chet)' % used)

print('\n' + '=' * 74)
nf = [r for r in R if not r[2]]
print('TONG: %d kiem may, %d FAIL' % (len(R), len(nf)))
for r in nf:
    print('  FAIL kiem %s: %s — %s' % (r[0], r[1], r[3]))
print('RUN_ID BANG CHUNG: %s' % EV)
print('Con kiem 12 (doc INTERFACE.md bang mat) lead lam rieng.')
sys.exit(1 if nf else 0)
