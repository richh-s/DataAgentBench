code = """import json
import re
from collections import defaultdict

# Load level-5 symbols
path_level5 = var_call_VJGJPUCCQvr2dsweZPkbJr5L
if isinstance(path_level5, str):
    with open(path_level5, 'r') as f:
        level5_rows = json.load(f)
else:
    level5_rows = path_level5
level5_symbols = set(r.get('symbol') for r in level5_rows if 'symbol' in r)

# Load publication records
path_pubs = var_call_shmIxgMRXOSCv75GQReWMkpM
if isinstance(path_pubs, str):
    with open(path_pubs, 'r') as f:
        pubs = json.load(f)
else:
    pubs = path_pubs

# Initialize counts per group per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pubs:
    cpc_field = rec.get('cpc')
    filing_date = rec.get('filing_date','') or ''
    m = re.search(r"(19|20)\d{2}", filing_date)
    if not m:
        continue
    year = int(m.group(0))
    all_years.add(year)
    # parse cpc JSON
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # skip malformed
        continue
    groups_in_rec = set()
    for item in cpcs:
        code = item.get('code') if isinstance(item, dict) else None
        if not code or not isinstance(code, str):
            continue
        code = code.replace(' ', '')
        if len(code) >= 4:
            group = code[:4]
        else:
            group = code
        if group in level5_symbols:
            groups_in_rec.add(group)
    for g in groups_in_rec:
        counts[g][year] += 1

if not all_years:
    result = []
else:
    min_year = min(all_years)
    max_year = max(all_years)
    alpha = 0.2
    groups_best_year = {}
    for g, year_counts in counts.items():
        ema_prev = None
        year_to_ema = {}
        for y in range(min_year, max_year+1):
            c = year_counts.get(y, 0)
            if ema_prev is None:
                ema = float(c)
            else:
                ema = alpha * c + (1 - alpha) * ema_prev
            year_to_ema[y] = ema
            ema_prev = ema
        # find year with max EMA, tie-breaker: latest year
        best_year = max(sorted(year_to_ema.items(), key=lambda kv: (kv[1], kv[0])))
        # best_year is (year, ema) due to sorting, but max returns tuple; adjust
        # Actually above returns tuple (year, ema) due to sort key; we want year with max ema, tie by year
        # Let's compute properly:
        best = max(year_to_ema.items(), key=lambda kv: (kv[1], kv[0]))
        groups_best_year[g] = best[0]
    # select groups whose best year is 2022
    selected = sorted([g for g, y in groups_best_year.items() if y == 2022])
    result = selected

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_VJGJPUCCQvr2dsweZPkbJr5L': 'file_storage/call_VJGJPUCCQvr2dsweZPkbJr5L.json', 'var_call_shmIxgMRXOSCv75GQReWMkpM': 'file_storage/call_shmIxgMRXOSCv75GQReWMkpM.json'}

exec(code, env_args)
