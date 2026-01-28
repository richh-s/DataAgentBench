code = """import json
import re
from collections import defaultdict

# Load level5 symbols
with open(var_call_WvFEO3Gp7bdwatI3S9dzT688, 'r', encoding='utf-8') as f:
    level5 = json.load(f)
level5_symbols = set(r.get('symbol') for r in level5 if r.get('symbol'))

# We'll stream publications and process, but to avoid timeouts, process in chunks
pubs_path = var_call_LMp5SOyHe8AwHSpUSmIGT84e

counts = defaultdict(lambda: defaultdict(int))
all_years = set()

# Define helper to check prefixes efficiently by grouping symbols by first 3 chars
from collections import defaultdict
sym_groups = defaultdict(list)
for s in level5_symbols:
    key = s[:3]
    sym_groups[key].append(s)

with open(pubs_path, 'r', encoding='utf-8') as f:
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
            key = code[:3]
            # check candidate symbols
            for sym in sym_groups.get(key, []):
                if code.startswith(sym):
                    matched.add(sym)
        for sym in matched:
            counts[sym][year] += 1

# Prepare years
if not all_years:
    result = []
else:
    years = sorted(all_years)
    full_years = list(range(years[0], years[-1]+1))
    alpha = 0.2
    best_year_by_sym = {}
    for sym in level5_symbols:
        series = [counts[sym].get(y,0) for y in full_years]
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
    result = sorted([s for s,y in best_year_by_sym.items() if y==2022])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WvFEO3Gp7bdwatI3S9dzT688': 'file_storage/call_WvFEO3Gp7bdwatI3S9dzT688.json', 'var_call_LMp5SOyHe8AwHSpUSmIGT84e': 'file_storage/call_LMp5SOyHe8AwHSpUSmIGT84e.json', 'var_call_RFnsNau9P8ASEXsENc83Ywzk': {'num_level5': 677, 'sample_symbols': ['A62B', 'A63G', 'A63K', 'A63B', 'A63J', 'A63C', 'A63D', 'A63F', 'C25D', 'A63H', 'A99Z', 'B01J', 'B01B', 'B01D', 'B01L', 'B01F', 'B02C', 'B02B', 'B03B', 'B03D']}}

exec(code, env_args)
