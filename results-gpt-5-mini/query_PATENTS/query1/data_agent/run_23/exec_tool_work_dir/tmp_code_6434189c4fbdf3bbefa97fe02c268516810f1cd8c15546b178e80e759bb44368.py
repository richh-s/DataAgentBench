code = """import json, re
from collections import defaultdict

# Load level-5 symbols list
with open(var_call_nBLGgHo9pCnYxC9OtqD74zAg, 'r') as f:
    level5_data = json.load(f)
level5_symbols = [d['symbol'] for d in level5_data]
# Sort by length desc to prefer longer prefix matches
level5_symbols_sorted = sorted(level5_symbols, key=lambda x: -len(x))

# Load publication records
with open(var_call_5hzjQP8iEKdspZOoj7EzNMso, 'r') as f:
    pubs = json.load(f)

# helper to extract year
year_re = re.compile(r'(19|20)\d{2}')

counts = defaultdict(int)
all_years = set()

for rec in pubs:
    filing = rec.get('filing_date')
    if not filing:
        continue
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group())
    all_years.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to sanitize and fallback to eval-like parsing
        try:
            import ast
            cpc_list = ast.literal_eval(cpc_field)
        except Exception:
            continue
    if not isinstance(cpc_list, list):
        continue
    for item in cpc_list:
        code = item.get('code') if isinstance(item, dict) else None
        if not code:
            continue
        code = code.strip()
        matched = None
        for sym in level5_symbols_sorted:
            if code.startswith(sym):
                matched = sym
                break
        if matched:
            counts[(matched, year)] += 1

if not all_years:
    result = []
else:
    years = sorted(all_years)
    alpha = 0.2
    symbol_best_year = {}

    # gather symbols that have any counts
    symbols_with_counts = sorted({k[0] for k in counts.keys()})

    for sym in symbols_with_counts:
        series = [counts.get((sym, y), 0) for y in years]
        # compute EMA
        ema = []
        if len(series) > 0:
            ema.append(series[0])
            for i in range(1, len(series)):
                ema.append(alpha * series[i] + (1 - alpha) * ema[-1])
        # find year(s) with max EMA, pick latest year in case of ties
        if ema:
            max_val = max(ema)
            max_idxs = [i for i, v in enumerate(ema) if v == max_val]
            best_idx = max(max_idxs)
            best_year = years[best_idx]
            symbol_best_year[sym] = best_year

    # select symbols where best_year == 2022
    result = sorted([s for s, y in symbol_best_year.items() if y == 2022])

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_nBLGgHo9pCnYxC9OtqD74zAg': 'file_storage/call_nBLGgHo9pCnYxC9OtqD74zAg.json', 'var_call_5hzjQP8iEKdspZOoj7EzNMso': 'file_storage/call_5hzjQP8iEKdspZOoj7EzNMso.json'}

exec(code, env_args)
