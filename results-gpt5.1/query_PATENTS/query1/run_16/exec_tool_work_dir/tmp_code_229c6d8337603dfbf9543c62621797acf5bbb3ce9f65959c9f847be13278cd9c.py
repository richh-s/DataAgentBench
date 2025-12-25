code = """import json, pandas as pd, datetime
from datetime import datetime

# Load full results from files
with open(var_call_QiGMp4zCoMytshwFKJmVqejm, 'r') as f:
    cpc_defs = json.load(f)
with open(var_call_beONgOU1n20kZCLNdw4LzVOg, 'r') as f:
    pubs = json.load(f)

# Get set of level-5 CPC symbols
level5_symbols = set(d['symbol'] for d in cpc_defs)

# Helper to parse year from natural language date; return None if fails
def parse_year(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip(), '%b %dth, %Y').year
    except Exception:
        try:
            return datetime.strptime(date_str.strip(), '%B %dth, %Y').year
        except Exception:
            # Try removing ordinal suffixes
            try:
                parts = date_str.replace('st', '').replace('nd', '').replace('rd', '').replace('th', '')
                for fmt in ['%b %d, %Y', '%B %d, %Y']:
                    try:
                        return datetime.strptime(parts.strip(), fmt).year
                    except Exception:
                        continue
            except Exception:
                return None
    return None

records = []
for row in pubs:
    year = parse_year(row.get('publication_date'))
    if year is None:
        continue
    cpc_raw = row.get('cpc')
    if not cpc_raw:
        continue
    try:
        entries = json.loads(cpc_raw)
    except Exception:
        continue
    for e in entries:
        code = e.get('code')
        if not code:
            continue
        # Normalize to group level 5: assume that's the full symbol as in definition table
        group = code.replace(' ', '')
        if group in level5_symbols:
            records.append({'symbol': group, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    # Count filings per symbol per year
    counts = df.groupby(['symbol', 'year']).size().reset_index(name='count')
    # Ensure years are sorted for EMA
    counts = counts.sort_values(['symbol', 'year'])

    alpha = 0.2
    ema_rows = []
    for sym, grp in counts.groupby('symbol'):
        ema = None
        for _, r in grp.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha * c + (1 - alpha) * ema
            ema_rows.append({'symbol': sym, 'year': int(r['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_rows)
    # For each year, find symbol(s) with highest EMA
    result_rows = []
    for year, grp in ema_df.groupby('year'):
        max_ema = grp['ema'].max()
        top_syms = grp[grp['ema'] == max_ema]['symbol'].tolist()
        for s in top_syms:
            result_rows.append({'year': int(year), 'symbol': s, 'ema': float(max_ema)})
    result_df = pd.DataFrame(result_rows)

    # Filter to best year 2022 for each symbol
    # First find each symbol's best year (max EMA)
    best_idx = ema_df.groupby('symbol')['ema'].idxmax()
    best_df = ema_df.loc[best_idx].reset_index(drop=True)
    best_2022 = best_df[best_df['year'] == 2022]

    # Intersect with symbols that are top in their year ("technology areas with highest EMA each year")
    top_syms_per_year = set(result_df['symbol'])
    best_2022 = best_2022[best_2022['symbol'].isin(top_syms_per_year)]

    result = sorted(best_2022['symbol'].unique().tolist())

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_QiGMp4zCoMytshwFKJmVqejm': 'file_storage/call_QiGMp4zCoMytshwFKJmVqejm.json', 'var_call_beONgOU1n20kZCLNdw4LzVOg': 'file_storage/call_beONgOU1n20kZCLNdw4LzVOg.json', 'var_call_tszBdicI7GkW7YeqKUisjVrK': [{'?column?': '1'}], 'var_call_BrUdol0KVRqgNLkm9vB3Uvij': [{'1': '1'}]}

exec(code, env_args)
