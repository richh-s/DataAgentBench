code = """import json
import re
from collections import defaultdict

# Load stored results
# var_call_WvFEO3Gp7bdwatI3S9dzT688 and var_call_LMp5SOyHe8AwHSpUSmIGT84e are available

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

level5 = load_var(var_call_WvFEO3Gp7bdwatI3S9dzT688)
pubs = load_var(var_call_LMp5SOyHe8AwHSpUSmIGT84e)

# Extract level5 symbols
level5_symbols = set()
for r in level5:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Prepare counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pubs:
    cpc_field = rec.get('cpc')
    pub_date = rec.get('publication_date','')
    # extract year
    m = re.search(r'(19|20)\d{2}', pub_date)
    if not m:
        continue
    year = int(m.group(0))
    all_years.add(year)
    # parse cpc JSON-like
    try:
        codes = json.loads(cpc_field)
    except Exception:
        # skip if cannot parse
        continue
    matched = set()
    for entry in codes:
        code = entry.get('code','')
        if not code:
            continue
        code = code.strip()
        # find level5 symbols that the code starts with
        for sym in level5_symbols:
            if code.startswith(sym):
                matched.add(sym)
    for sym in matched:
        counts[sym][year] += 1

if not all_years:
    result = []
else:
    years = sorted(all_years)
    min_year = years[0]
    max_year = years[-1]
    full_years = list(range(min_year, max_year+1))

    alpha = 0.2
    best_year_by_sym = {}

    for sym in level5_symbols:
        # build time series of counts for full_years
        series = [counts[sym].get(y, 0) for y in full_years]
        if all(v==0 for v in series):
            continue
        # compute EMA
        emas = []
        ema = series[0]
        emas.append(ema)
        for x in series[1:]:
            ema = alpha * x + (1-alpha) * ema
            emas.append(ema)
        # find year of max EMA (choose earliest year of max)
        max_idx = max(range(len(emas)), key=lambda i: emas[i])
        best_year = full_years[max_idx]
        best_year_by_sym[sym] = best_year

    # collect symbols whose best year is 2022
    result = [sym for sym, y in best_year_by_sym.items() if y == 2022]
    result.sort()

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WvFEO3Gp7bdwatI3S9dzT688': 'file_storage/call_WvFEO3Gp7bdwatI3S9dzT688.json', 'var_call_LMp5SOyHe8AwHSpUSmIGT84e': 'file_storage/call_LMp5SOyHe8AwHSpUSmIGT84e.json'}

exec(code, env_args)
