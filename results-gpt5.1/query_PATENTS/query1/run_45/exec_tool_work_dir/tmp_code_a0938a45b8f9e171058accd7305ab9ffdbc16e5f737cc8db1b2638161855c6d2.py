code = """import json, pandas as pd
from datetime import datetime

# Load full results from files
with open(var_call_PgA3c8fQF9XDFZFG6I7qYTTk, 'r') as f:
    pub_data = json.load(f)
with open(var_call_bcXZx3gzajJbOIZswKgfgpfN, 'r') as f:
    cpc5_data = json.load(f)

# Create DataFrame for publication data
df_pub = pd.DataFrame(pub_data)

# Parse year from natural language publication_date
months = {m: i for i, m in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], start=1)}

def parse_year(date_str):
    if not isinstance(date_str, str):
        return None
    parts = date_str.replace(',', '').split()
    for p in parts:
        if p.isdigit() and len(p) == 4:
            return int(p)
    # fallback: last token
    try:
        return int(parts[-1])
    except:
        return None


df_pub['year'] = df_pub['publication_date'].apply(parse_year)

# Filter for years up to 2022 (inclusive) and >= 2013 as queried
df_pub = df_pub[(df_pub['year']>=2013) & (df_pub['year']<=2022)]

# Extract CPC codes from JSON-like string

def extract_codes(cpc_str):
    if not isinstance(cpc_str, str) or cpc_str.strip()=="":
        return []
    try:
        return [entry.get('code') for entry in json.loads(cpc_str) if isinstance(entry, dict) and 'code' in entry]
    except Exception:
        try:
            fixed = cpc_str.replace("'", '"')
            return [entry.get('code') for entry in json.loads(fixed) if isinstance(entry, dict) and 'code' in entry]
        except Exception:
            return []


# explode CPC codes
codes_series = df_pub['cpc'].apply(extract_codes)
df_exp = df_pub[['year']].copy()
df_exp['code_list'] = codes_series

# explode lists
df_exp = df_exp.explode('code_list').dropna(subset=['code_list'])

# Keep only level-5 CPC symbols
cpc5_df = pd.DataFrame(cpc5_data)
level5_codes = set(cpc5_df['symbol'].astype(str).unique())

# CPC symbols in publication data may include subgroup (e.g., H01M10/0565). For level 5 group code, we map to the nearest symbol in level5 list using prefix matching.

# Pre-compute mapping by taking the longest matching level5 symbol that is a prefix of the full code

unique_codes = df_exp['code_list'].astype(str).unique()

mapped = {}
for code in unique_codes:
    candidates = [s for s in level5_codes if code.startswith(s)]
    if candidates:
        mapped[code] = max(candidates, key=len)
    else:
        mapped[code] = None


df_exp['group5'] = df_exp['code_list'].map(mapped)

# Drop rows without level5 mapping
df_exp = df_exp.dropna(subset=['group5'])

# Count filings per year per group5
counts = df_exp.groupby(['group5','year']).size().reset_index(name='count')

# For each group, compute EMA across years in chronological order with alpha=0.2
alpha = 0.2

records = []
for group, gdf in counts.groupby('group5'):
    gdf = gdf.sort_values('year')
    ema = None
    for _, row in gdf.iterrows():
        year = int(row['year'])
        c = row['count']
        if ema is None:
            ema = c
        else:
            ema = alpha*c + (1-alpha)*ema
        records.append({'group5': group, 'year': year, 'ema': ema})

ema_df = pd.DataFrame(records)

# For each year, find group5 with highest EMA
idx = ema_df.groupby('year')['ema'].idxmax()
best_per_year = ema_df.loc[idx].reset_index(drop=True)

# Keep only rows where best year is 2022 for each group
# Determine best year per group (year with max EMA)
best_year_per_group = ema_df.loc[ema_df.groupby('group5')['ema'].idxmax()][['group5','year']]

best_year_2022_groups = set(best_year_per_group[best_year_per_group['year']==2022]['group5'])

# We need CPC group codes at level 5 whose best year is 2022 AND are best in 2022 among all groups
result_groups = best_per_year[(best_per_year['year']==2022) & (best_per_year['group5'].isin(best_year_2022_groups))]['group5'].unique().tolist()

import json as _json
out = _json.dumps(result_groups)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PgA3c8fQF9XDFZFG6I7qYTTk': 'file_storage/call_PgA3c8fQF9XDFZFG6I7qYTTk.json', 'var_call_bcXZx3gzajJbOIZswKgfgpfN': 'file_storage/call_bcXZx3gzajJbOIZswKgfgpfN.json'}

exec(code, env_args)
