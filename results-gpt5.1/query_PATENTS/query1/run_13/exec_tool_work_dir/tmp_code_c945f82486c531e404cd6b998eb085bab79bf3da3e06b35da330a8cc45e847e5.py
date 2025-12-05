code = """import json, pandas as pd, re, datetime as dt
from collections import defaultdict

# Load full datasets from files
with open(var_call_h7RZUIvddPqBsJyE2emAmLSc, 'r') as f:
    level5_symbols = json.load(f)

with open(var_call_aQ1diYcQyf0Jdp0sCLoYfewo, 'r') as f:
    pub_rows = json.load(f)

level5_set = {row['symbol'] for row in level5_symbols}

# helper to parse natural language date to year
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(date_str):
    if not date_str:
        return None
    # expect like "Aug 3rd, 2021" or "March 15th, 2020"
    try:
        parts = date_str.replace(',', '').split()
        if len(parts) < 3:
            return None
        # month could be full or abbreviated; take first 3 letters
        mon = parts[0][:3]
        year = int(parts[-1])
        return year
    except Exception:
        return None

# count patents per (symbol, year)
counts = defaultdict(int)

for row in pub_rows:
    year = parse_year(row.get('publication_date'))
    if year is None:
        continue
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        # level-5 group code: up to group (e.g. H01M10/0565) -- in definition table symbol is that full string
        group = code.strip()
        if group in level5_set:
            counts[(group, year)] += 1

# organize years per symbol
per_symbol_years = defaultdict(dict)
for (sym, year), cnt in counts.items():
    per_symbol_years[sym][year] = cnt

alpha = 0.2

best_year_2022_symbols = []

for sym, year_counts in per_symbol_years.items():
    years = sorted(year_counts.keys())
    ema_by_year = {}
    ema = None
    for y in years:
        x = year_counts[y]
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1-alpha) * ema
        ema_by_year[y] = ema
    # find year with highest EMA
    max_ema = max(ema_by_year.values())
    best_years = [y for y, v in ema_by_year.items() if v == max_ema]
    # if multiple, take latest
    best_year = max(best_years)
    if best_year == 2022:
        best_year_2022_symbols.append(sym)

best_year_2022_symbols_sorted = sorted(best_year_2022_symbols)

import json as _json
result = _json.dumps(best_year_2022_symbols_sorted)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_h7RZUIvddPqBsJyE2emAmLSc': 'file_storage/call_h7RZUIvddPqBsJyE2emAmLSc.json', 'var_call_aQ1diYcQyf0Jdp0sCLoYfewo': 'file_storage/call_aQ1diYcQyf0Jdp0sCLoYfewo.json', 'var_call_QZjO9pOb8msw6Nvd35ea4B8a': [{'?column?': '1'}]}

exec(code, env_args)
