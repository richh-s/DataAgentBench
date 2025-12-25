code = """import json, pandas as pd, re, datetime

# Load symbols (may be file path or list)
from pathlib import Path

symbols_src = var_call_prM9qLaQB1S5HtS7gIO8Des3
if isinstance(symbols_src, str) and Path(symbols_src).suffix == '.json':
    with open(symbols_src, 'r') as f:
        symbols = json.load(f)
else:
    symbols = symbols_src

pub_src = var_call_3Q0YEn7M6ISMiyv7MezLTMWE
if isinstance(pub_src, str) and Path(pub_src).suffix == '.json':
    with open(pub_src, 'r') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

symbols_set = {s['symbol'] for s in symbols}

# Helper to parse dates like "Aug 3rd, 2021"
months = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(d):
    if not d or not isinstance(d,str):
        return None
    m = re.match(r'([A-Za-z]+)\s+\d{1,2}(st|nd|rd|th)?,\s*(\d{4})', d.strip())
    if not m:
        return None
    try:
        return int(m.group(3))
    except:
        return None

# Count filings per CPC symbol per year
counts = {}
for row in pubs:
    y = parse_year(row.get('publication_date'))
    if y is None:
        continue
    if not row.get('cpc'):
        continue
    try:
        cpc_list = json.loads(row['cpc'])
    except Exception:
        continue
    # deduplicate codes within a patent
    codes = {e.get('code') for e in cpc_list if isinstance(e, dict) and e.get('code')}
    for code in codes:
        # level 5 group code: assume up to subclass/group like "H01M4/1315" etc.
        # Match against available level-5 symbols by prefix: if the symbol equals the part before space
        base = code.split(' ')[0]
        if base in symbols_set:
            counts.setdefault(base, {}).setdefault(y, 0)
            counts[base][y] += 1

# For each symbol, compute yearly EMA with alpha=0.2 over sorted years
alpha = 0.2
symbol_year_ema = {}

for sym, year_counts in counts.items():
    years = sorted(year_counts)
    ema_prev = None
    for y in years:
        val = year_counts[y]
        if ema_prev is None:
            ema = val
        else:
            ema = alpha*val + (1-alpha)*ema_prev
        ema_prev = ema
        symbol_year_ema.setdefault(sym, {})[y] = ema

# For each symbol, find year with max EMA
best_year = {}
for sym, ydict in symbol_year_ema.items():
    max_year = max(ydict.items(), key=lambda kv: kv[1])[0]
    best_year[sym] = max_year

# Filter symbols whose best year is 2022
result_symbols = sorted([sym for sym, y in best_year.items() if y == 2022])

import json as _json
out = _json.dumps(result_symbols)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_prM9qLaQB1S5HtS7gIO8Des3': 'file_storage/call_prM9qLaQB1S5HtS7gIO8Des3.json', 'var_call_3Q0YEn7M6ISMiyv7MezLTMWE': 'file_storage/call_3Q0YEn7M6ISMiyv7MezLTMWE.json', 'var_call_J4b2WmqGhE1mSx0WaS1rZ4Hx': [{'?column?': '1'}], 'var_call_lNfQWelWKSO1h9AHqYqFeFBt': [{'1': '1'}]}

exec(code, env_args)
