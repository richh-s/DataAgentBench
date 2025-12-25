code = """import json, pandas as pd, datetime as dt, re

# Load large query results from files
pub_path = var_call_z4PkV7FWRypH9YgYcVlPG11E
cpcdef_path = var_call_cLDtjpsBckPNwOfOX0LAhX3l

with open(pub_path, 'r') as f:
    pub_data = json.load(f)
with open(cpcdef_path, 'r') as f:
    cpcdef_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
month_map = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(s):
    if not isinstance(s, str) or not s.strip():
        return None
    # Extract year as 4 digits
    m = re.search(r'(19|20)\d{2}', s)
    if m:
        return int(m.group(0))
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)

# Drop rows without year
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Parse CPC JSON-like string
codes = []
for _, row in pub_df.iterrows():
    cpc_raw = row['cpc']
    year = row['year']
    if not isinstance(cpc_raw, str) or not cpc_raw.strip():
        continue
    try:
        lst = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in lst:
        code = entry.get('code')
        if not code:
            continue
        codes.append({'code': code, 'year': year})

code_df = pd.DataFrame(codes)

# Keep only CPC level 5 symbols
cpcdef_df = pd.DataFrame(cpcdef_data)
level5 = set(cpcdef_df['symbol'].astype(str).unique())
code_df = code_df[code_df['code'].isin(level5)]

# Count filings per code-year
counts = code_df.groupby(['code','year']).size().reset_index(name='count')

# Compute EMA per code over years (alpha=0.2)
alpha = 0.2

records = []
for code, grp in counts.groupby('code'):
    grp = grp.sort_values('year')
    ema = None
    for _, r in grp.iterrows():
        y = int(r['year'])
        c = r['count']
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1-alpha) * ema
        records.append({'code': code, 'year': y, 'ema': float(ema)})

ema_df = pd.DataFrame(records)

# For each code, find year with max EMA
best = ema_df.sort_values(['code','ema','year'], ascending=[True,False,True])\
             .groupby('code').head(1)

# Filter to best year == 2022
best_2022 = best[best['year'] == 2022]

result_codes = sorted(best_2022['code'].unique().tolist())

import json as _json
out = _json.dumps(result_codes)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_z4PkV7FWRypH9YgYcVlPG11E': 'file_storage/call_z4PkV7FWRypH9YgYcVlPG11E.json', 'var_call_cLDtjpsBckPNwOfOX0LAhX3l': 'file_storage/call_cLDtjpsBckPNwOfOX0LAhX3l.json'}

exec(code, env_args)
