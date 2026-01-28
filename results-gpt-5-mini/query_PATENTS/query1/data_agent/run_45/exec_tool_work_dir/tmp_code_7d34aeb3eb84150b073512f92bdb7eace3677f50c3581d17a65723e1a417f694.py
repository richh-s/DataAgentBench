code = """import json, re
from collections import defaultdict

# Load data from previous tool results
with open(var_call_pkjPqSxvvQTVbYqH88xTnOJI, 'r', encoding='utf-8') as f:
    level5_list = json.load(f)
with open(var_call_Qu1OO1VzIP91iYj6XT11aFcf, 'r', encoding='utf-8') as f:
    pub_records = json.load(f)

level5_symbols = set()
for item in level5_list:
    sym = item.get('symbol')
    if sym:
        level5_symbols.add(sym.strip().upper())

# Aggregate counts per level5 symbol per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pub_records:
    cpc_str = rec.get('cpc')
    filing = rec.get('filing_date') or ''
    # extract year
    year_match = re.search(r"(19|20)\d{2}", filing)
    if not year_match:
        continue
    year = int(year_match.group(0))
    all_years.add(year)
    if not cpc_str:
        continue
    # parse cpc field which is JSON-like
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        # try to fix common issues
        try:
            # remove newlines
            cpcs = json.loads(cpc_str.replace('\n', ''))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or len(code) < 4:
            continue
        grp = code[:4].upper()
        # consider only level5 symbols defined in cpc_definition
        if grp in level5_symbols:
            counts[grp][year] += 1

if not all_years:
    result = []
else:
    years_sorted = sorted(all_years)
    alpha = 0.2
    best_year_by_grp = {}
    for grp, year_counts in counts.items():
        # compute EMA across global year range
        ema = None
        ema_by_year = {}
        for y in years_sorted:
            cnt = year_counts.get(y, 0)
            if ema is None:
                ema = cnt
            else:
                ema = alpha * cnt + (1 - alpha) * ema
            ema_by_year[y] = ema
        # find year with max ema
        best_year = max(ema_by_year.items(), key=lambda x: (x[1], -x[0]))[0]
        best_year_by_grp[grp] = best_year
    # select groups whose best year is 2022
    selected = sorted([g for g, y in best_year_by_grp.items() if y == 2022])
    result = selected

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pkjPqSxvvQTVbYqH88xTnOJI': 'file_storage/call_pkjPqSxvvQTVbYqH88xTnOJI.json', 'var_call_Qu1OO1VzIP91iYj6XT11aFcf': 'file_storage/call_Qu1OO1VzIP91iYj6XT11aFcf.json'}

exec(code, env_args)
