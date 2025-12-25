code = """import json, pandas as pd
from datetime import datetime

# Load full data from files
with open(var_call_tIJvqQWnxSu55MAfDeE4ua1K, 'r') as f:
    pub_data = json.load(f)
with open(var_call_wqHQTJaM2Rexv6C86cJ00r4Y, 'r') as f:
    lvl5_data = json.load(f)

# Prepare level 5 CPC symbols set
lvl5_symbols = {row['symbol'] for row in lvl5_data}

# Helper to parse year from natural language date
def parse_year(s):
    if not s:
        return None
    s = s.strip()
    for fmt in ['%b %dth, %Y', '%b %dst, %Y', '%b %dnd, %Y', '%b %drd, %Y', '%B %dth, %Y', '%B %dst, %Y', '%B %dnd, %Y', '%B %drd, %Y', '%B %d, %Y', '%b %d, %Y']:
        try:
            return datetime.strptime(s, fmt).year
        except Exception:
            continue
    # try to extract last 4-digit year
    for token in s.split():
        if len(token) == 4 and token.isdigit():
            return int(token)
    return None

records = []
for row in pub_data:
    year = parse_year(row.get('publication_date'))
    if not year:
        continue
    try:
        cpc_list = json.loads(row.get('cpc') or '[]')
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if not code:
            continue
        # map to group level (level 5) group code; assume truncate at subclass group with "/" part
        # CPC group code at level 5 approximated as up to first "/" plus following number as-is
        group_code = code
        if group_code not in lvl5_symbols:
            continue
        records.append({'year': year, 'symbol': group_code})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # count filings per symbol-year
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    # ensure continuous years per symbol
    all_years = sorted(counts['year'].unique())
    symbols = counts['symbol'].unique()
    rows = []
    for sym in symbols:
        sym_counts = counts[counts['symbol']==sym].set_index('year')['count']
        for y in all_years:
            rows.append({'symbol': sym, 'year': y, 'count': int(sym_counts.get(y, 0))})
    full = pd.DataFrame(rows).sort_values(['symbol','year'])

    alpha = 0.2
    emas = []
    for sym in symbols:
        sub = full[full['symbol']==sym].sort_values('year')
        ema = None
        for _, r in sub.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            emas.append({'symbol': sym, 'year': int(r['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(emas)

    # find best year per symbol
    best = ema_df.loc[ema_df.groupby('symbol')['ema'].idxmax()].reset_index(drop=True)
    # filter to best year == 2022
    best2022 = best[best['year']==2022]
    result = sorted(best2022['symbol'].unique().tolist())

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tIJvqQWnxSu55MAfDeE4ua1K': 'file_storage/call_tIJvqQWnxSu55MAfDeE4ua1K.json', 'var_call_wqHQTJaM2Rexv6C86cJ00r4Y': 'file_storage/call_wqHQTJaM2Rexv6C86cJ00r4Y.json'}

exec(code, env_args)
