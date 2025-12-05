code = """import json, pandas as pd, datetime

# Load large query results from files
with open(var_call_WiZ7MmQlExKgMj0SgoOZGq19, 'r') as f:
    pubs = json.load(f)
with open(var_call_VnUtSBGSVXgericiNFm86tmy, 'r') as f:
    cpc_defs = json.load(f)

# Build set of level-5 CPC symbols
level5 = {row['symbol'] for row in cpc_defs}

# Helper to parse year from natural-language date like "Aug 3rd, 2021"
import re
months = {m:i for i,m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(d):
    if not d:
        return None
    try:
        # assume formats like 'Aug 3rd, 2021'
        m = re.match(r"([A-Za-z]+)\s+\d{1,2}(?:st|nd|rd|th)?,\s*(\d{4})", d)
        if m:
            return int(m.group(2))
        # fallback: last 4-digit year
        m = re.search(r"(19|20)\d{2}", d)
        if m:
            return int(m.group(0))
    except Exception:
        return None
    return None

# Count filings per (year, CPC symbol) considering only level-5 symbols
counts = {}
for row in pubs:
    year = parse_year(row.get('publication_date'))
    if year is None:
        continue
    try:
        cpc_list = json.loads(row.get('cpc') or '[]')
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        # normalise code to CPC group at level 5: use full symbol up to 4 digits and optional slash+2-4 digits
        # Here we assume DB symbols (like 'H01M10/0565') match codes directly, so use full code
        if code not in level5:
            continue
        key = (code, year)
        counts[key] = counts.get(key, 0) + 1

# Transform to DataFrame
rows = [{'symbol': s, 'year': y, 'count': c} for (s,y), c in counts.items()]
df = pd.DataFrame(rows)
if df.empty:
    result = []
else:
    # compute EMA per symbol sorted by year
    dfs = []
    for sym, g in df.groupby('symbol'):
        g = g.sort_values('year')
        # reindex to continuous years range
        years = range(g['year'].min(), g['year'].max()+1)
        g2 = g.set_index('year').reindex(years, fill_value=0).rename_axis('year').reset_index()
        # EMA with alpha=0.2
        g2['ema'] = g2['count'].ewm(alpha=0.2, adjust=False).mean()
        g2['symbol'] = sym
        dfs.append(g2)
    ema_df = pd.concat(dfs, ignore_index=True)

    # best year (max EMA) per symbol
    best = ema_df.loc[ema_df.groupby('symbol')['ema'].idxmax()][['symbol','year','ema']]

    # filter where best year is 2022
    best2022 = best[best['year'] == 2022]

    # We only need CPC group codes (symbols) for which best year is 2022
    result = sorted(best2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_WiZ7MmQlExKgMj0SgoOZGq19': 'file_storage/call_WiZ7MmQlExKgMj0SgoOZGq19.json', 'var_call_VnUtSBGSVXgericiNFm86tmy': 'file_storage/call_VnUtSBGSVXgericiNFm86tmy.json'}

exec(code, env_args)
