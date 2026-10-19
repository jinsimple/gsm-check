# -*- coding: utf-8 -*-
"""Kiem 17 — canh ve THU HAI cua M04: moi duong thoat (return/raise) tren duong
   quyet dinh phai co loi goi log truoc do. reviewer tim ra run_product.py:46-47
   bang MAT; khong co lenh kiem nao giu no, ma product/ co 38 cau return/raise.

   Kiem 18 — canh chinh quy tac sao luu: manifest da commit, ban sao luu ngoai
   repo ton tai, va sha256 trong manifest KHOP ban sao luu."""
import ast, glob, hashlib, io, json, os, sys

ROOT, BACKUP, EV = sys.argv[1], sys.argv[2], sys.argv[3]
os.chdir(ROOT)
FAIL = 0

# ============ KIEM 17 ============
# Danh sach mien CO NGUON GOC, dung khuon kiem 14: khop ten file + ten ham + ly do.
MIEN17 = [
    # (duoi ten file, ten ham, ly do) — ham thuan hoac khong nam tren duong quyet dinh
    ('logger.py',     '_format_run_id',  'ham thuan dinh dang run_id'),
    ('logger.py',     'make_run_id',     'sinh run_id; log chua ton tai o thoi diem nay'),
    ('logger.py',     'process_run_id',  'tra run_id dung chung cho tien trinh'),
    ('logger.py',     'make_fallback_logger', 'tao logger du phong'),
    ('logger.py',     'default_logger',  'tra logger du phong cua module logger (them o T09d)'),
    ('logger.py',     '_merge_context',  'ham thuan tron dict context'),
    ('logger.py',     '_now_iso',        'ham thuan lay thoi diem'),
    ('logger.py',     'rel',             'ham thuan doi duong dan'),
    ('logger.py',     '__enter__',       'giao thuc context manager'),
    ('logger.py',     '__exit__',        'giao thuc context manager'),
    ('matching.py',   'default_logger',  'tra logger du phong cua module'),
    ('matching.py',   'haversine_km',    'ham toan hoc thuan'),
    ('matching.py',   'load_config',     'doc config; nhanh thieu version thuoc load_json_config'),
    ('pricing.py',    'default_logger',  'tra logger du phong cua module'),
    ('pricing.py',    '_hour_of',        'ham thuan lay gio tu chuoi ISO'),
    ('pricing.py',    'load_config',     'doc config; nhanh thieu version thuoc load_json_config'),
    ('run_product.py','_read_json',      'ham thuan doc file JSON'),
    ('run_product.py','_sha256',         'ham thuan bam file'),
    ('run_product.py','_iso_now',        'ham thuan lay thoi diem'),
    ('run_product.py','main',            'vo boc CLI, tra ma thoat'),
    ('gen_mock.py',   '_make_id',        'ham thuan dinh dang ma'),
    ('gen_mock.py',   '_coord',          'ham thuan sinh toa do'),
    ('gen_mock.py',   '_weighted',       'ham thuan chon theo trong so'),
    ('gen_mock.py',   '_rand_coord',     'ham thuan sinh toa do'),
    ('gen_mock.py',   '_destination',    'ham thuan: toa do dich tu khoang cach + huong'),
]

# Mien CHI cho Return, KHONG mien Raise — vi raise la quyet dinh ve du lieu
# nghiep vu doc tu config, con return la tra gia tri da duoc log o tang goi.
MIEN17_RETURN = [
    # Mien CHI cho Return, KHONG mien Raise — tang goi ghi clearance_check voi
    # chinh con so nay, nen gia tri tra ve co bang chung; con `raise` thi la quyet
    # dinh ve du lieu nen van phai co log rieng.
    ('gen_mock.py', '_min_distance_to_drivers', 'return gia tri do: tang goi ghi clearance_check voi con so nay'),
    ('logger.py',  'load_json_config',   'return thanh cong: tang goi ghi config_loaded'),
    ('pricing.py', '_round_to_multiple', 'return gia tri: fare() ghi fare_rounding voi gia truoc/sau'),
]

def mien17_return(f, fn):
    ff = f.replace(os.sep, '/')
    for sf, sfn, ly in MIEN17_RETURN:
        if ff.endswith(sf) and fn == sfn:
            return ly
    return None


def has_log(node):
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Attribute) and f.attr == 'log':
                return True
    return False

def mien17(f, fn):
    ff = f.replace('\\', '/')
    for sf, sfn, ly in MIEN17:
        if ff.endswith(sf.split('/')[-1]) and fn == sfn:
            return ly
    return None

flagged, exempt = [], []

def scan(stmts, logged, f, fn):
    for st in stmts:
        if isinstance(st, (ast.Return, ast.Raise)):
            if not logged and not has_log(st):
                ly = mien17_return(f, fn) if isinstance(st, ast.Return) else None
                if ly:
                    exempt.append('%s::%s return dong %d — %s' % (f, fn, st.lineno, ly))
                else:
                    flagged.append((f, st.lineno, fn, type(st).__name__))
            continue
        if has_log(st) and not isinstance(st, (ast.If, ast.For, ast.While)):
            # Try.body / With.body: neu khong nem loi thi log da chay -> phu cho cau sau.
            # If / For / While: co dieu kien hoac co the khong lap -> KHONG phu.
            logged = True
        for fld in ('body', 'orelse', 'finalbody'):
            sub = getattr(st, fld, None)
            if isinstance(sub, list):
                scan(sub, logged, f, fn)
        for h in getattr(st, 'handlers', []) or []:
            scan(h.body, logged, f, fn)
        if isinstance(st, (ast.If, ast.For, ast.While, ast.Try, ast.With)) and has_log(st):
            pass  # log trong nhanh con KHONG tinh la da log cho cac cau sau

for f in sorted(glob.glob('product/**/*.py', recursive=True)):
    tree = ast.parse(io.open(f, encoding='utf-8').read(), filename=f)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            ly = mien17(f, node.name)
            n_exit = sum(1 for n in ast.walk(node) if isinstance(n, (ast.Return, ast.Raise)))
            if ly:
                if n_exit:
                    exempt.append('%s::%s (%d duong thoat) — %s' % (f, node.name, n_exit, ly))
                continue
            scan(node.body, False, f, node.name)

tong_exit = 0
for f in sorted(glob.glob('product/**/*.py', recursive=True)):
    tree = ast.parse(io.open(f, encoding='utf-8').read(), filename=f)
    tong_exit += sum(1 for n in ast.walk(tree) if isinstance(n, (ast.Return, ast.Raise)))

print('=== KIEM 17 — duong thoat khong co log truoc do (ve 2 cua M04) ===')
print('  Tong return/raise trong product/**/*.py : %d' % tong_exit)
print('  Ham duoc mien (co nguon goc)            : %d' % len(exempt))
for x in exempt:
    print('      - %s' % x)
if flagged:
    FAIL += 1
    print('  [FAIL] %d duong thoat KHONG co log truoc do:' % len(flagged))
    for f, ln, fn, kind in flagged:
        src = io.open(f, encoding='utf-8').read().split('\n')[ln - 1].strip()
        print('      %s:%d  %s trong %s()  <-- %s' % (f, ln, kind, fn, src[:58]))
else:
    print('  [PASS] moi duong thoat tren duong quyet dinh deu co log truoc do')

# ============ MANIFEST ============
# DA BO. Truoc day khoi nay sinh manifest schema_version 0.1 va GHI DE manifest
# 0.3 tot ma kiem19_manifest.py vua tao cho cung run_id — mot lenh kiem tu pha
# bang chung cua lenh kiem khac. Nay kiem 18 doc manifest da co tren dia.
_mp = 'reports/logs_manifest_%s.json' % EV
if not os.path.exists(_mp):
    print('\n=== KIEM 18 ===')
    print('  [FAIL] chua co %s — chay tests/kiem19_manifest.py truoc' % _mp)
    print('\n' + '=' * 70)
    print('KET QUA: %d FAIL' % (FAIL + 1))
    sys.exit(1)
man = json.load(io.open(_mp, encoding='utf-8'))

# ============ KIEM 18 ============
print('\n=== KIEM 18 — manifest khop ban sao luu ngoai repo ===')
bad18 = []
# Quet 0 file thi bao PASS la dung loai loi reviewer da bat o kiem 14: mot lenh
# kiem khong co gi de kiem thi phai FAIL, khong phai PASS.
if not man.get('files'):
    bad18.append('manifest khong liet ke file nao — khong co gi de doi chieu')
for x in man.get('files', []):
    b = os.path.join(BACKUP, os.path.basename(x['path']))
    if not os.path.exists(b):
        bad18.append('thieu ban sao luu: %s' % os.path.basename(x['path'])); continue
    h = hashlib.sha256()
    with open(b, 'rb') as fh:
        for c in iter(lambda: fh.read(1 << 20), b''):
            h.update(c)
    if h.hexdigest() != x['sha256']:
        bad18.append('sha256 LECH: %s' % os.path.basename(x['path']))
    else:
        print('  OK  %-40s sha256 khop (%d dong)' % (os.path.basename(x['path']), x['lines']))
if bad18:
    FAIL += 1
    print('  [FAIL] %s' % '; '.join(bad18))
else:
    print('  [PASS] ca %d file log bang chung co ban sao luu ngoai repo, sha256 khop tung file' % len(man['files']))

print('\n' + '=' * 70)
print('KET QUA: %d FAIL' % FAIL)
sys.exit(1 if FAIL else 0)
