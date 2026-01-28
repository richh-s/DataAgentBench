code = """import json
import re
from collections import defaultdict

# Load data from storage file paths
cpc_def_path = var_call_NZK8gMFRH4HXYS6XWz1H0NwT
pubs_path = var_call_TPDWK2Yf9jznugo6fm9cYgPB

with open(cpc_def_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)
with open(pubs_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

level5_symbols = set()
for r in cpc_defs:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Helper to extract year
year_re = re.compile(r'(19|20)\d{2}')

def extract_year(s):
    if not s or not isinstance(s, str):
        return None
    m = year_re.search(s)
    if m:
        try:
            return int(m.group(0))
        except:
            return None
    return None

# Counts per symbol per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pubs:
    cpc_field = rec.get('cpc')
    filing = rec.get('filing_date')
    year = extract_year(filing)
    if year is None:
        continue
    all_years.add(year)
    # parse cpc json-like string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix common issues
        try:
            cpcs = json.loads(cpc_field.replace("\n", "").replace('\"', '"'))
        except Exception:
            continue
    codes = set()
    for entry in cpcs:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or not isinstance(code, str):
            continue
        # derive level-5 symbol as first 4 characters (e.g., 'H01M')
        sym = code[:4]
        codes.add(sym)
    # For each unique symbol in this patent that is a level5 symbol, increment count once
    for sym in codes:
        if sym in level5_symbols:
            counts[sym][year] += 1

if not all_years:
    result = []
else:
    min_year = min(all_years)
    max_year = max(all_years)
    years_range = list(range(min_year, max_year+1))
    alpha = 0.2
    best_symbols = []
    for sym, year_counts in counts.items():
        # build count series for full range
        series = [year_counts.get(y, 0) for y in years_range]
        # compute EMA
        emas = {}
        if not series:
            continue
        ema_prev = series[0]
        emas[years_range[0]] = float(ema_prev)
        for i in range(1, len(series)):
            y = years_range[i]
            c = series[i]
            ema = alpha * c + (1 - alpha) * ema_prev
            emas[y] = float(ema)
            ema_prev = ema
        # find year with max EMA
        best_year = max(emas.items(), key=lambda kv: (kv[1], kv[0]))[0]
        if best_year == 2022:
            best_symbols.append(sym)
    # sort results
    result = sorted(best_symbols)

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_NZK8gMFRH4HXYS6XWz1H0NwT': 'file_storage/call_NZK8gMFRH4HXYS6XWz1H0NwT.json', 'var_call_TPDWK2Yf9jznugo6fm9cYgPB': 'file_storage/call_TPDWK2Yf9jznugo6fm9cYgPB.json'}

exec(code, env_args)
