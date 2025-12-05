code = """import json, pandas as pd

# Load full publication data
with open(var_call_lPPdoOZJMqS7jn79c3TBQ1wR, 'r') as f:
    pub_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
def parse_year(date_str):
    if not isinstance(date_str, str) or not date_str.strip():
        return None
    parts = date_str.strip().split()
    for p in reversed(parts):
        p = p.strip(',')
        if p.isdigit() and len(p) == 4:
            return int(p)
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])

# Extract CPC codes from JSON-like string
codes = []
for _, row in pub_df.iterrows():
    cpc_raw = row['cpc']
    try:
        cpc_list = json.loads(cpc_raw) if isinstance(cpc_raw, str) else []
    except Exception:
        try:
            cpc_list = json.loads(cpc_raw.replace("'", '"')) if isinstance(cpc_raw, str) else []
        except Exception:
            cpc_list = []
    year = int(row['year'])
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if code:
            codes.append({'symbol': code, 'year': year})

codes_df = pd.DataFrame(codes)

# Count filings per symbol per year
counts = codes_df.groupby(['symbol', 'year']).size().reset_index(name='count')

# Compute EMA (alpha=0.2) per symbol over years in ascending order
alpha = 0.2
ema_rows = []
for symbol, grp in counts.sort_values(['symbol', 'year']).groupby('symbol'):
    ema = None
    for _, r in grp.iterrows():
        c = r['count']
        y = int(r['year'])
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_rows.append({'symbol': symbol, 'year': y, 'ema': float(ema)})

ema_df = pd.DataFrame(ema_rows)

# Restrict to level-5 CPC symbols
with open(var_call_FFt9OqKuNXt5wJl5itjn6qhJ, 'r') as f:
    level5_data = json.load(f)
level5_df = pd.DataFrame(level5_data)
level5_symbols = set(level5_df['symbol'].astype(str))
ema_df = ema_df[ema_df['symbol'].isin(level5_symbols)]

# For each symbol, find the year with highest EMA
best = ema_df.sort_values(['symbol', 'ema', 'year'], ascending=[True, False, True]).groupby('symbol').first().reset_index()

# Keep only those whose best year is 2022
best_2022 = best[best['year'] == 2022]

result_list = sorted(best_2022['symbol'].astype(str).unique().tolist())

import json as _json
out = _json.dumps(result_list)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_lPPdoOZJMqS7jn79c3TBQ1wR': 'file_storage/call_lPPdoOZJMqS7jn79c3TBQ1wR.json', 'var_call_FFt9OqKuNXt5wJl5itjn6qhJ': 'file_storage/call_FFt9OqKuNXt5wJl5itjn6qhJ.json'}

exec(code, env_args)
