code = """import json, pandas as pd, re, datetime
from collections import defaultdict

# Load large results from files
with open(var_call_br9ytR48Shoa3GqCnjS5hTmh, 'r') as f:
    pub_data = json.load(f)
with open(var_call_RkQyKqGrQfrH948hZ2zUYRoV, 'r') as f:
    level5_data = json.load(f)

# Helper to parse natural-language dates like 'Aug 3rd, 2021'
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_date_to_year(s):
    if not s or not isinstance(s, str):
        return None
    try:
        parts = s.replace(',', '').split()
        if len(parts) < 3:
            return None
        mon = parts[0][:3]
        year = int(parts[-1])
        if mon not in month_map:
            return None
        return year
    except Exception:
        return None

# Build set of level-5 symbols (prefixes)
level5_symbols = set([r['symbol'] for r in level5_data])

# Aggregate counts per year per CPC symbol
counts = defaultdict(lambda: defaultdict(int))

for rec in pub_data:
    year = parse_date_to_year(rec.get('publication_date'))
    if year is None:
        continue
    cpc_raw = rec.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        # normalize: strip spaces
        code_norm = code.strip()
        # Map to level-5 group: take first 4 characters (section+class+subclass) or up to first non alnum?
        # But level5_symbols look like 'A62B', 'B01J' etc, so we take prefix until first non-alphanumeric
        m = re.match(r'[A-Z]\d{2}[A-Z]', code_norm)
        if not m:
            continue
        prefix = m.group(0)
        if prefix not in level5_symbols:
            continue
        counts[prefix][year] += 1

# For each symbol, compute EMA per year with alpha=0.2
alpha = 0.2

ema_records = []  # list of (symbol, year, ema)

all_years = sorted({parse_date_to_year(r.get('publication_date')) for r in pub_data if parse_date_to_year(r.get('publication_date')) is not None})

for symbol, year_counts in counts.items():
    ema = None
    for y in sorted(all_years):
        c = year_counts.get(y, 0)
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1-alpha) * ema
        ema_records.append({'symbol': symbol, 'year': y, 'ema': ema})

# Convert to DataFrame
ema_df = pd.DataFrame(ema_records)

# For each symbol, find year with max EMA (best year)
best = ema_df.sort_values(['symbol','ema','year'], ascending=[True,False,True]).groupby('symbol').first().reset_index()

# Filter where best year is 2022
best_2022 = best[best['year'] == 2022]

# We only need CPC group codes (symbols)
result_symbols = sorted(best_2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result_symbols)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_br9ytR48Shoa3GqCnjS5hTmh': 'file_storage/call_br9ytR48Shoa3GqCnjS5hTmh.json', 'var_call_RkQyKqGrQfrH948hZ2zUYRoV': 'file_storage/call_RkQyKqGrQfrH948hZ2zUYRoV.json', 'var_call_ZuOGIqWZk1bXEjHnilsJOUJL': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_call_3F8IW1LKgHpdDq7VjHC4lGEn': ['publicationinfo']}

exec(code, env_args)
