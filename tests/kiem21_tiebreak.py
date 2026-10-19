# -*- coding: utf-8 -*-
"""Kiem 21 — nhanh pha hoa chua bao gio chay (pm phat hien, dung hinh dang voi
   hai bac gia da sua). tie_break ghi 960/960 "no_tie" tren bang chung hien tai
   -- SPEC_A.md:32 noi quy tac pha hoa ton tai "de ket qua xac dinh", nhung
   chua kiem duoc tren du lieu nay.

   Giong tien le kiem 15 (radius_km=0.0001) va kiem 20 (config trong bo nho):
   goi match() TRUC TIEP voi du lieu tai xe dung MOT PHAN, trong run_id chan
   doan rieng. KHONG doi mock_data.json, KHONG doi du lieu mac dinh, KHONG
   commit lam baseline."""
import copy, io, json, os, sys

ROOT = sys.argv[1]
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, 'product'))
import logger as L
import matching as M

RUN = 'K21DIAG'
lg = L.JsonlLogger('matching', RUN, autoflush=True)
cfg = json.load(io.open('product/config/matching.json', encoding='utf-8'))

ride = {
    "ride_id": "RDIAG", "vehicle_type": "car",
    "pickup_lat": 21.04, "pickup_lon": 105.83,
}

def driver(did, trips_today, lat=21.04, lon=105.83):
    # Dat CUNG toa do diem don -> khoang cach haversine bang nhau TUYET DOI,
    # khong phu thuoc may rui float gan-bang.
    return {"driver_id": did, "status": "idle", "vehicle_type": "car",
            "lat": lat, "lon": lon, "trips_today": trips_today,
            "acceptance_rate": 0.9}

print('=== KIEM 21 — nhanh pha hoa trong match() (SPEC_A.md:32) ===')

# Ca 1: hoa khoang cach, trips_today KHAC nhau -> phai chon trips_today thap hon.
drivers1 = [driver("D9002", trips_today=5), driver("D9001", trips_today=2)]
out1 = M.match(ride, drivers1, cfg, logger=lg)
ok1 = out1["driver_id"] == "D9001"
print('  Ca 1 (trips_today khac: D9002=5, D9001=2) -> driver_id=%s  [%s]'
      % (out1["driver_id"], 'PASS' if ok1 else 'FAIL'))

# Ca 2: hoa khoang cach VA hoa trips_today -> phai chon driver_id nho hon.
drivers2 = [driver("D9004", trips_today=3), driver("D9003", trips_today=3)]
out2 = M.match(ride, drivers2, cfg, logger=lg)
ok2 = out2["driver_id"] == "D9003"
print('  Ca 2 (trips_today bang: D9004=3, D9003=3) -> driver_id=%s  [%s]'
      % (out2["driver_id"], 'PASS' if ok2 else 'FAIL'))

lines = [json.loads(x) for x in io.open('logs/matching_%s.jsonl' % RUN, encoding='utf-8') if x.strip()]
ties = [o for o in lines if o.get('event') == 'tie_break']
reasons = {o.get('reason') for o in ties}
ok3 = 'tie_break' in {o.get('event') for o in lines} and len(reasons) >= 1 and reasons != {'no_tie'}
print('  Log tie_break trong run chan doan: %s' % ([o.get('reason') for o in ties]))
print('  [%s] log tie_break ghi nhan hoa THAT (khong chi "no_tie")' % ('PASS' if ok3 else 'FAIL'))

bad = sum(0 if x else 1 for x in (ok1, ok2, ok3))
print()
print('  log chan doan: logs/matching_%s.jsonl (KHONG phai run_id bang chung)' % RUN)
if bad:
    print('KET QUA: %d FAIL — quy tac pha hoa SAI hoac khong ghi log khi hoa' % bad)
else:
    print('KET QUA: PASS — quy tac pha hoa dung ca hai ca, va co log hoa that')
    print('  [Chua xac minh tren du lieu mac dinh] Nhanh nay van la nhanh CHET tren')
    print('  rides.json hien tai (960/960 no_tie). Chan doan nay CHI chung minh')
    print('  code dung khi bi buoc phai hoa, KHONG thay doi so lan chay thuc te = 0.')
sys.exit(1 if bad else 0)
