code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_GaDNdFrYtziSJ8v5gYMjcpUn, 'r') as f:
    pub_data = json.load(f)
with open(var_call_yy3osBbzdTcLKxcNlIKXBgSU, 'r') as f:
    cpc_defs = json.load(f)

# Filter to Germany using country_code in Patents_info
def get_country(info):
    m = re.search(r'\b([A-Z]{2})\b', info)
    return m.group(1) if m else None

for rec in pub_data:
    rec['country'] = get_country(rec.get('Patents_info',''))

de_pub = [r for r in pub_data if r.get('country') == 'DE']

# Parse grant year and keep for all years (we'll need per-year counts)
months = { 'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
           'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

def parse_year(date_str):
    if not date_str:
        return None
    m = re.search(r'(19|20)\d{2}', date_str)
    return int(m.group(0)) if m else None

for rec in de_pub:
    rec['year'] = parse_year(rec.get('grant_date',''))

# Extract CPC codes (full symbols) from JSON-like cpc field
for rec in de_pub:
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        cpc_list = []
    rec['cpc_codes'] = list({c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('code')})

# Build annual counts per CPC symbol
rows = []
for rec in de_pub:
    y = rec.get('year')
    if not y:
        continue
    for code in rec['cpc_codes']:
        rows.append({'symbol': code, 'year': y, 'count':1})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    grp = df.groupby(['symbol','year'])['count'].sum().reset_index()

    # For EMA we need continuous years range per symbol
    alpha = 0.1
    records = []
    for sym, g in grp.groupby('symbol'):
        g = g.sort_values('year')
        years_full = list(range(g['year'].min(), g['year'].max()+1))
        counts_map = dict(zip(g['year'], g['count']))
        ema_prev = None
        for y in years_full:
            c = counts_map.get(y, 0)
            if ema_prev is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema_prev
            ema_prev = ema
            records.append({'symbol': sym, 'year': y, 'ema': float(ema)})

    ema_df = pd.DataFrame(records)

    # Determine best year (max EMA) per symbol
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best_df = ema_df.loc[idx].reset_index(drop=True)

    # Map to level-4 group codes: take first 4 characters of symbol, then match to cpc_definition where symbol equals that
    best_df['group4'] = best_df['symbol'].str[:3]

    cpc_df = pd.DataFrame(cpc_defs)
    cpc_df = cpc_df[cpc_df['level'].astype(float) == 4.0][['symbol','titleFull']].rename(columns={'symbol':'group4'})

    merged = best_df.merge(cpc_df, on='group4', how='left')

    # Keep top CPC technology areas by EMA value
    merged = merged.sort_values('ema', ascending=False)
    out = merged[['group4','titleFull','year','ema']].head(20)
    result = out.to_dict(orient='records')

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_GaDNdFrYtziSJ8v5gYMjcpUn': 'file_storage/call_GaDNdFrYtziSJ8v5gYMjcpUn.json', 'var_call_yy3osBbzdTcLKxcNlIKXBgSU': 'file_storage/call_yy3osBbzdTcLKxcNlIKXBgSU.json'}

exec(code, env_args)
