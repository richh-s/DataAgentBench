code = """import json, re
from collections import defaultdict

# Load data files produced by earlier queries
with open(var_call_pkjPqSxvvQTVbYqH88xTnOJI, 'r', encoding='utf-8') as f:
    level5_list = json.load(f)
with open(var_call_Qu1OO1VzIP91iYj6XT11aFcf, 'r', encoding='utf-8') as f:
    pub_records = json.load(f)

# Build set of level-5 CPC symbols
level5_symbols = set()
for it in level5_list:
    s = it.get('symbol')
    if s:
        level5_symbols.add(s.strip().upper())

# Prepare regex for year
year_re = re.compile(r"(19|20)\d{2}")

# Aggregate counts per group (first 4 chars) per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pub_records:
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date') or ''
    ym = year_re.search(filing)
    if not ym:
        continue
    year = int(ym.group(0))
    all_years.add(year)
    if not cpc_field:
        continue
    # parse CPC JSON-like field
    cpcs = None
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            # try cleaning common escape issues
            txt = cpc_field.replace('\n',' ').replace('\t',' ').strip()
            cpcs = json.loads(txt)
        except Exception:
            # skip record if cannot parse
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            code = None
        if not code or len(code) < 4:
            continue
        grp = code[:4].upper()
        if grp in level5_symbols:
            counts[grp][year] += 1

result = []
if all_years:
    years_sorted = sorted(all_years)
    alpha = 0.2
    for grp, year_counts in counts.items():
        ema = None
        ema_by_year = {}
        for y in years_sorted:
            cnt = year_counts.get(y, 0)
            if ema is None:
                ema = cnt
            else:
                ema = alpha * cnt + (1 - alpha) * ema
            ema_by_year[y] = ema
        # choose year with highest EMA; if tie pick the later year
        best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
        if best_year == 2022:
            result.append(grp)
    result = sorted(result)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pkjPqSxvvQTVbYqH88xTnOJI': 'file_storage/call_pkjPqSxvvQTVbYqH88xTnOJI.json', 'var_call_Qu1OO1VzIP91iYj6XT11aFcf': 'file_storage/call_Qu1OO1VzIP91iYj6XT11aFcf.json', 'var_call_yr6k7q5dFarSlQJCT8MYh85m': [], 'var_call_xz8iQJWAGhFg6qKtUVwSNHMU': {'level5_count': 677, 'pub_count': 277813}}

exec(code, env_args)
