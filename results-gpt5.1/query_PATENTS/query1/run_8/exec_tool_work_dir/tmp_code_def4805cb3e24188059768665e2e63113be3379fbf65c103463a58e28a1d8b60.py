code = """import json, pandas as pd, re, datetime as dt
from collections import defaultdict

# Load full publication data
with open(var_call_MY5FYip4PYzne88uQx57VvAw, 'r') as f:
    pubs = json.load(f)

# Build set of level-5 CPC symbols
with open(var_call_qxDDIaBrxcbHYpxl1oTs7l6X, 'r') as f:
    level5 = {row['symbol'] for row in json.load(f)}

alpha = 0.2

# Helper to parse year from natural-language date like "Aug 3rd, 2021"
months = {m:i for i,m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(d):
    if not d:
        return None
    try:
        # extract year as last 4-digit number
        m = re.search(r'(19|20)\d{2}', d)
        if m:
            return int(m.group(0))
    except Exception:
        return None
    return None

# Count filings per CPC symbol per year
counts = defaultdict(lambda: defaultdict(int))

for rec in pubs:
    year = parse_year(rec.get('publication_date'))
    if year is None:
        continue
    cpc_raw = rec.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    codes = {entry.get('code') for entry in cpc_list if isinstance(entry, dict) and entry.get('code')}
    for code in codes:
        if code in level5:
            counts[code][year] += 1

# For each symbol, compute EMA over years in chronological order
results = []
for code, year_counts in counts.items():
    years = sorted(year_counts)
    ema = None
    best_year = None
    best_ema = None
    for y in years:
        x = year_counts[y]
        if ema is None:
            ema = x
        else:
            ema = alpha * x + (1-alpha) * ema
        if best_ema is None or ema > best_ema:
            best_ema = ema
            best_year = y
    if best_year == 2022:
        results.append(code)

# Deduplicate and sort
results = sorted(set(results))

import json as _json
out = _json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_hkZqODwxOGZtt0QVcTT5UUxl': [], 'var_call_MY5FYip4PYzne88uQx57VvAw': 'file_storage/call_MY5FYip4PYzne88uQx57VvAw.json', 'var_call_ZmhuRNLu2TvP0ZGMj7l0AceU': [{'?column?': '1'}], 'var_call_mIMuFPHKMJKa4RZmH2BljCtH': ['cpc_definition'], 'var_call_qxDDIaBrxcbHYpxl1oTs7l6X': 'file_storage/call_qxDDIaBrxcbHYpxl1oTs7l6X.json'}

exec(code, env_args)
