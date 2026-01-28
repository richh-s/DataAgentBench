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
# For performance, stream publication records and process incrementally to avoid heavy memory or CPU
pubs_path = var_call_LMp5SOyHe8AwHSpUSmIGT84e

level5_symbols = set(r.get('symbol') for r in level5 if r.get('symbol'))

counts = defaultdict(lambda: defaultdict(int))
all_years = set()

# Process publications line by line from JSON list to avoid building huge python objects
with open(pubs_path, 'r', encoding='utf-8') as f:
    # load as list but iterate
    data = json.load(f)
    for rec in data:
        cpc_field = rec.get('cpc')
        pub_date = rec.get('publication_date','')
        m = re.search(r'(19|20)\d{2}', pub_date)
        if not m:
            continue
        year = int(m.group(0))
        all_years.add(year)
        try:
            codes = json.loads(cpc_field)
        except Exception:
            continue
        matched = set()
        for entry in codes:
            code = entry.get('code','')
            if not code:
                continue
            code = code.strip()
            # check prefixes only up to length of symbol
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
        series = [counts[sym].get(y, 0) for y in full_years]
        if all(v==0 for v in series):
            continue
        ema = series[0]
        best_ema = ema
        best_year = full_years[0]
        for i, x in enumerate(series[1:], start=1):
            ema = alpha * x + (1-alpha) * ema
            if ema > best_ema:
                best_ema = ema
                best_year = full_years[i]
        best_year_by_sym[sym] = best_year

    result = [sym for sym, y in best_year_by_sym.items() if y == 2022]
    result.sort()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WvFEO3Gp7bdwatI3S9dzT688': 'file_storage/call_WvFEO3Gp7bdwatI3S9dzT688.json', 'var_call_LMp5SOyHe8AwHSpUSmIGT84e': 'file_storage/call_LMp5SOyHe8AwHSpUSmIGT84e.json'}

exec(code, env_args)
