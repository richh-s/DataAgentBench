code = """import json, pandas as pd, re, datetime

# Load full publication data
with open(var_call_VtGcEQ4Dj6IOXvz6XKS4tYVd, 'r') as f:
    pub_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year from natural-language publication_date
def extract_year(date_str):
    if not isinstance(date_str, str):
        return None
    m = re.search(r'(19|20)\d{2}', date_str)
    return int(m.group(0)) if m else None

pub_df['year'] = pub_df['publication_date'].apply(extract_year)

# Filter years up to 2022
pub_df = pub_df[pub_df['year'].between(1900, 2022, inclusive='both')]

# Expand CPC JSON-like list
codes = []
for _, row in pub_df.iterrows():
    cpc_raw = row['cpc']
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    for entry in cpc_list:
        code = entry.get('code')
        if code:
            codes.append({'year': row['year'], 'code': code})

codes_df = pd.DataFrame(codes)

# Load level-5 CPC symbols
with open(var_call_fB6h4P3L1vp8wNw1ePTeq2nb, 'r') as f:
    cpc5_data = json.load(f)

cpc5_df = pd.DataFrame(cpc5_data)
level5_codes = set(cpc5_df['symbol'].dropna().unique())

# Keep only level-5 codes
codes_df = codes_df[codes_df['code'].isin(level5_codes)]

# Compute yearly counts per CPC code
counts = codes_df.groupby(['code', 'year']).size().reset_index(name='count')

# Ensure continuous years per code
all_years = sorted(counts['year'].unique())

full = []
for code, grp in counts.groupby('code'):
    grp = grp.set_index('year').reindex(all_years, fill_value=0)
    grp = grp.reset_index()
    grp['code'] = code
    full.append(grp)

full_df = pd.concat(full, ignore_index=True)

# Compute EMA with alpha=0.2 per code, in chronological order
alpha = 0.2

ema_values = []
for code, grp in full_df.groupby('code'):
    grp = grp.sort_values('year')
    ema = None
    for _, r in grp.iterrows():
        c = r['count']
        if ema is None:
            ema = c
        else:
            ema = alpha * c + (1 - alpha) * ema
        ema_values.append({'code': code, 'year': int(r['year']), 'ema': float(ema)})

ema_df = pd.DataFrame(ema_values)

# For each code, find year with max EMA
idx = ema_df.groupby('code')['ema'].idxmax()
best_df = ema_df.loc[idx].reset_index(drop=True)

# Keep only codes whose best year is 2022
best_2022 = best_df[best_df['year'] == 2022]

result_codes = sorted(best_2022['code'].tolist())

import json as _json
out = _json.dumps(result_codes)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VtGcEQ4Dj6IOXvz6XKS4tYVd': 'file_storage/call_VtGcEQ4Dj6IOXvz6XKS4tYVd.json', 'var_call_fB6h4P3L1vp8wNw1ePTeq2nb': 'file_storage/call_fB6h4P3L1vp8wNw1ePTeq2nb.json'}

exec(code, env_args)
