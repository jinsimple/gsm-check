# -*- coding: utf-8 -*-
"""Kiem 20 — nhanh TRAN he so gio (`min(raw_coef, max_time_coef)` chon ve PHAI).

Xung dot Q13 <-> Q19: Q19 doi moi nhanh phai chay, nhung de tran 1.3 rang buoc
thi phai THEM mot khung gio he so > 1.3 vao config — ma Q13 cam them thu SPEC_A
khong co. pm go bang tien le cua chinh lead: kiem 15 goi match() truc tiep voi
radius_km=0.0001 trong mot logger chan doan rieng, khong doi config mac dinh,
khong commit lam baseline — Bach da chap nhan.

Lam y nhu vay: goi fare() voi mot BAN SAO TRONG BO NHO cua pricing.json co
max_time_coef thap hon he so khung gio cao diem. product/config/pricing.json
KHONG bi sua, nen khong cham Q13. Chay trong run_id chan doan K20DIAG, khong
phai run_id bang chung."""
import copy, io, json, os, sys

ROOT = sys.argv[1]
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, 'product'))
import logger as L
import pricing as P

RUN = 'K20DIAG'
lg = L.JsonlLogger('pricing', RUN, autoflush=True)

cfg = json.load(io.open('product/config/pricing.json', encoding='utf-8'))
raw_peak = max(w['coef'] for w in cfg['time_coefficients'])
assert raw_peak > 1.0, raw_peak

# Ban sao trong bo nho: tran bi ha xuong duoi he so cao diem -> `min()` buoc phai
# chon ve max_time_coef. File config tren dia KHONG doi.
diag = copy.deepcopy(cfg)
diag['max_time_coef'] = 1.0
peak_hour = [w for w in cfg['time_coefficients'] if w['coef'] == raw_peak][0]['hours'][0]
ts = '2026-10-19T%02d:30:00' % peak_hour

print('=== KIEM 20 — nhanh tran he so gio bi rang buoc ===')
print('  he so khung cao diem   : %.1f (gio %d)' % (raw_peak, peak_hour))
print('  max_time_coef mac dinh : %.1f  -> min() chon ve raw, tran KHONG rang buoc'
      % cfg['max_time_coef'])
print('  max_time_coef chan doan: %.1f  -> min() PHAI chon ve tran' % diag['max_time_coef'])

out_capped = P.fare(8.0, ts, diag, logger=lg)
out_normal = P.fare(8.0, ts, cfg, logger=lg)
lg.close() if hasattr(lg, 'close') else None

lines = [json.loads(x) for x in io.open('logs/pricing_%s.jsonl' % RUN, encoding='utf-8')
         if x.strip()]
caps = [o for o in lines if o.get('event') == 'time_coef_cap']

ok = []
ok.append(('tran rang buoc -> time_coef = max_time_coef',
           abs(out_capped['time_coef'] - diag['max_time_coef']) < 1e-9,
           'time_coef = %s' % out_capped['time_coef']))
ok.append(('tran khong rang buoc -> time_coef = he so khung',
           abs(out_normal['time_coef'] - raw_peak) < 1e-9,
           'time_coef = %s' % out_normal['time_coef']))
ok.append(('gia khi bi tran < gia khi khong tran',
           out_capped['fare_vnd'] < out_normal['fare_vnd'],
           '%d < %d VND' % (out_capped['fare_vnd'], out_normal['fare_vnd'])))
ok.append(('log co ca hai nhanh cap_applied va cap_not_binding',
           {'cap_applied', 'cap_not_binding'} <= {o.get('reason') for o in caps},
           ' '.join(sorted({o.get('reason') for o in caps}))))
ok.append(('product/config/pricing.json KHONG bi sua (Q13)',
           json.load(io.open('product/config/pricing.json', encoding='utf-8')) == cfg,
           'max_time_coef con %.1f' % json.load(
               io.open('product/config/pricing.json', encoding='utf-8'))['max_time_coef']))

bad = 0
for name, good, detail in ok:
    if not good:
        bad += 1
    print('  [%s] %-52s %s' % ('PASS' if good else 'FAIL', name, detail))

print('\n  log chan doan: logs/pricing_%s.jsonl (%d dong, KHONG phai run_id bang chung)'
      % (RUN, len(lines)))
print('KET QUA: %s' % ('%d FAIL' % bad if bad else 'PASS — nhanh tran da chay that, Q19 thoa, Q13 khong bi cham'))
sys.exit(1 if bad else 0)
