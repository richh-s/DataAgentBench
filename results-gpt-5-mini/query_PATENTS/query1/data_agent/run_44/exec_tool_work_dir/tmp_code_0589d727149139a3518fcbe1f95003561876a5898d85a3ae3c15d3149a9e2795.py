code = """import json
import re
import pandas as pd

# Load data from storage paths
with open(var_call_yGiteBIGqwnae6aP6Ia0pify, 'r') as f:
    pubs = json.load(f)
with open(var_call_5NFLnPUVy8p48uE48CoarhLC, 'r') as f:
    lvl5 = json.load(f)

lvl5_symbols = set([item['symbol'] for item in lvl5])

counts = {}
years_set = set()

for r in pubs:
    fd = r.get('filing_date') or ''
    m = re.search(r'(19|20)\d{2}', fd)
    if not m:
        continue
    year = int(m.group(0))
    years_set.add(year)
    cpc_field = r.get('cpc') or ''
    # parse cpc field which is a JSON-like string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # fallback: if it's already a list
        if isinstance(cpc_field, list):
            cpcs = cpc_field
        else:
            cpcs = []
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            code = None
        if not code or len(code) < 4:
            continue
        group = code[:4]
        if group not in lvl5_symbols:
            continue
        counts[(group, year)] = counts.get((group, year), 0) + 1

if not counts:
    result = []
else:
    min_year = min(years_set)
    max_year = max(years_set)
    max_year = max(max_year, 2022)
    years = list(range(min_year, max_year + 1))
    alpha = 0.2
    # compute EMA per group per year
    groups = sorted(set(k[0] for k in counts.keys()))
    ema_per_group = {g: {} for g in groups}
    for g in groups:
        ema_prev = None
        for y in years:
            cnt = counts.get((g, y), 0)
            if ema_prev is None:
                ema = cnt
            else:
                ema = alpha * cnt + (1 - alpha) * ema_prev
            ema_per_group[g][y] = ema
            ema_prev = ema
    # determine best year per group (year with max EMA; if tie choose latest year)
    result = []
    for g in groups:
        series = ema_per_group[g]
        max_ema = max(series.values())
        years_with_max = [y for y, v in series.items() if v == max_ema]
        best_year = max(years_with_max)
        if best_year == 2022:
            result.append(g)
    result = sorted(result)

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_KAzuZTpQ5nMh185eQfoJCner': ['publicationinfo'], 'var_call_EK9IP98Z0ib5izO3Q3mhqJoN': ['cpc_definition'], 'var_call_yGiteBIGqwnae6aP6Ia0pify': 'file_storage/call_yGiteBIGqwnae6aP6Ia0pify.json', 'var_call_5NFLnPUVy8p48uE48CoarhLC': 'file_storage/call_5NFLnPUVy8p48uE48CoarhLC.json'}

exec(code, env_args)
