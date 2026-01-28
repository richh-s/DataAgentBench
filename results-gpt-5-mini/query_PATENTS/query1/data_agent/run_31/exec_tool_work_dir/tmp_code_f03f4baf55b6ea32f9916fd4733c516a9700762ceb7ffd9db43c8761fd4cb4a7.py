code = """import json
import re
from collections import defaultdict

# Load query results from storage variables
# var_call_XVJDQgV7Lq135SV2qo0jDHC1 and var_call_wK7WsskEZwVdX45SUSqyk6WM

# Helper to load data whether it's inline list or a filepath
def load_var(v):
    if isinstance(v, str):
        # assume file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

records = load_var(var_call_XVJDQgV7Lq135SV2qo0jDHC1)
level5_rows = load_var(var_call_wK7WsskEZwVdX45SUSqyk6WM)

# Extract list of level-5 symbols
level5_symbols = [r.get('symbol') for r in level5_rows if r.get('symbol')]
# Sort by length descending to prefer longest match
level5_symbols_sorted = sorted(level5_symbols, key=lambda s: len(s), reverse=True)

# Function to extract year from filing_date text
def extract_year(text):
    if not text or not isinstance(text, str):
        return None
    # find 4-digit year
    years = re.findall(r'(20\d{2}|19\d{2})', text)
    if years:
        return int(years[-1])
    return None

# We'll process records in a streaming manner to avoid heavy memory and time
counts = defaultdict(lambda: defaultdict(int))  # counts[symbol][year] = count

for i, rec in enumerate(records):
    if i % 5000 == 0:
        pass
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None:
        continue
    # parse cpc_field which is JSON-like string
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    # collect mapped level5 symbols for this patent (deduplicate per patent)
    mapped = set()
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        code = code.strip()
        # Find longest matching level5 symbol prefix
        for sym in level5_symbols_sorted:
            if code.startswith(sym):
                mapped.add(sym)
                break
    for sym in mapped:
        counts[sym][year] += 1

# For each symbol, build sorted year series and compute EMA with alpha=0.2
alpha = 0.2
best_year_by_symbol = {}

for sym, year_counts in counts.items():
    # get chronological years
    years = sorted(year_counts.keys())
    if not years:
        continue
    emas = {}
    prev_ema = None
    for y in years:
        x = year_counts[y]
        if prev_ema is None:
            ema = x
        else:
            ema = alpha * x + (1 - alpha) * prev_ema
        emas[y] = ema
        prev_ema = ema
    # find year of max ema
    best_year = max(emas.items(), key=lambda kv: (kv[1], kv[0]))[0]
    best_year_by_symbol[sym] = best_year

# Collect symbols whose best year is 2022
result_symbols = sorted([s for s, y in best_year_by_symbol.items() if y == 2022])

import json as _json
print("__RESULT__:")
print(_json.dumps(result_symbols))"""

env_args = {'var_call_XVJDQgV7Lq135SV2qo0jDHC1': 'file_storage/call_XVJDQgV7Lq135SV2qo0jDHC1.json', 'var_call_wK7WsskEZwVdX45SUSqyk6WM': 'file_storage/call_wK7WsskEZwVdX45SUSqyk6WM.json'}

exec(code, env_args)
