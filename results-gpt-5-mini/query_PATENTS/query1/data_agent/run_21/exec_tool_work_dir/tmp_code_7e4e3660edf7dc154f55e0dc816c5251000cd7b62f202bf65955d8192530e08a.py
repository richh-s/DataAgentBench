code = """import json
import re
from collections import defaultdict

# Load data from previous tool results
# var_call_V2gCHH28bzSWsjWbVn7af0RN and var_call_oRaElq9eLcB6f4jdmAD8KhEN are file paths
with open(var_call_V2gCHH28bzSWsjWbVn7af0RN, 'r', encoding='utf-8') as f:
    cpc_def = json.load(f)
with open(var_call_oRaElq9eLcB6f4jdmAD8KhEN, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

# Build set of level-5 symbols
level5_symbols = set()
for rec in cpc_def:
    sym = rec.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Count filings per symbol per year
counts = defaultdict(int)
years_set = set()

def extract_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

for rec in pubs:
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None:
        continue
    years_set.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field is a JSON-like string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # skip malformed
        continue
    # For each code, map to level-5 symbol (first 4 chars of the part before slash)
    seen_symbols = set()
    for entry in cpcs:
        code = entry.get('code')
        if not code: continue
        left = code.split('/')[0]
        sym = left[:4]
        if not sym: continue
        # Only consider symbols that exist in level5 set
        if sym in level5_symbols:
            # Avoid counting duplicate symbols within same publication multiple times
            if sym in seen_symbols:
                continue
            seen_symbols.add(sym)
            counts[(sym, year)] += 1

if not years_set:
    result = []
else:
    years = sorted(years_set)
    # Build per-symbol time series
    symbols = sorted({k[0] for k in counts.keys()})
    symbol_series = {}
    for sym in symbols:
        series = [counts.get((sym, y), 0) for y in years]
        symbol_series[sym] = series

    # Compute EMA with alpha=0.2 for each symbol across years
    alpha = 0.2
    best_year_for_sym = {}
    for sym, series in symbol_series.items():
        ema = series[0]
        ema_by_year = {years[0]: ema}
        for i in range(1, len(years)):
            ema = alpha * series[i] + (1 - alpha) * ema
            ema_by_year[years[i]] = ema
        # Find the year with highest EMA (if multiple, choose the latest year among them)
        max_ema = max(ema_by_year.values())
        best_years = [y for y, v in ema_by_year.items() if v == max_ema]
        best_year = max(best_years)
        best_year_for_sym[sym] = best_year

    # Filter symbols whose best year is 2022
    result = sorted([sym for sym, y in best_year_for_sym.items() if y == 2022])

# Print result according to required format
import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_V2gCHH28bzSWsjWbVn7af0RN': 'file_storage/call_V2gCHH28bzSWsjWbVn7af0RN.json', 'var_call_oRaElq9eLcB6f4jdmAD8KhEN': 'file_storage/call_oRaElq9eLcB6f4jdmAD8KhEN.json'}

exec(code, env_args)
