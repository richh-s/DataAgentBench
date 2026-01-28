code = """import json
import re
from collections import defaultdict

# Load publication records
pub_path = var_call_uUxI4FSxZBoGRzxg3pk7FNpw
with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Load level-5 CPC symbols
lvl5_path = var_call_Roeo6GpyI8s2lSgKkZjSNopA
with open(lvl5_path, 'r', encoding='utf-8') as f:
    lvl5_rows = json.load(f)
level5_symbols = set(r['symbol'] for r in lvl5_rows if 'symbol' in r)

# Build counts per group per year
counts = defaultdict(lambda: defaultdict(int))
year_pattern = re.compile(r"(19|20)\d{2}")
grp_pattern = re.compile(r'^[A-Z]\d{2}[A-Z]')

for rec in pubs:
    pub_date = rec.get('publication_date') or ''
    m = year_pattern.search(pub_date)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # if already a list-like object
        cpcs = cpc_field if isinstance(cpc_field, list) else []
    for item in cpcs:
        if not item:
            continue
        code = None
        if isinstance(item, dict):
            code = item.get('code')
        elif isinstance(item, str):
            code = item
        if not code or not isinstance(code, str):
            continue
        code = code.strip()
        m2 = grp_pattern.match(code)
        if not m2:
            continue
        grp = m2.group(0)
        if grp in level5_symbols:
            counts[grp][year] += 1

# Compute EMA per group per year with alpha=0.2
alpha = 0.2
best_groups = []
results = {}
for grp, year_counts in counts.items():
    years = sorted(year_counts.keys())
    if not years:
        continue
    ema_by_year = {}
    ema = None
    for y in years:
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_by_year[y] = ema
    # find year with max EMA, tie-breaker: choose latest year
    max_ema = None
    max_year = None
    for y, e in ema_by_year.items():
        if (max_ema is None) or (e > max_ema) or (e == max_ema and y > max_year):
            max_ema = e
            max_year = y
    results[grp] = {"max_year": max_year, "max_ema": max_ema}
    if max_year == 2022:
        best_groups.append(grp)

best_groups_sorted = sorted(best_groups)

import json
print("__RESULT__:")
print(json.dumps(best_groups_sorted))"""

env_args = {'var_call_uUxI4FSxZBoGRzxg3pk7FNpw': 'file_storage/call_uUxI4FSxZBoGRzxg3pk7FNpw.json', 'var_call_Roeo6GpyI8s2lSgKkZjSNopA': 'file_storage/call_Roeo6GpyI8s2lSgKkZjSNopA.json'}

exec(code, env_args)
