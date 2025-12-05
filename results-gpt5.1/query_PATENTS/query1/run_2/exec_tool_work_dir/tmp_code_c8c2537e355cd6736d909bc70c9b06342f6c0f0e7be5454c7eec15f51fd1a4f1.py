code = """import json, pandas as pd, datetime as dt

# Load large results from files
with open(var_call_X076QFpcvZuemVYnuz1mRNnD, 'r') as f:
    pub = json.load(f)
with open(var_call_i2NFJPXRMyTNmomOryoCsc6l, 'r') as f:
    defs = json.load(f)

pub_df = pd.DataFrame(pub)

# Parse year from natural-language publication_date
months = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(d):
    if not isinstance(d,str) or not d.strip():
        return None
    parts = d.replace(',','').split()
    if len(parts) < 3:
        return None
    mon = parts[0][:3]
    try:
        year = int(parts[2])
    except:
        return None
    return year

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Expand CPC JSON-like field
codes = []
for _, row in pub_df.iterrows():
    cpc_str = row['cpc']
    try:
        lst = json.loads(cpc_str)
    except Exception:
        continue
    for entry in lst:
        code = entry.get('code')
        if not code:
            continue
        codes.append({'code': code, 'year': row['year']})

codes_df = pd.DataFrame(codes)

# Keep only years up to 2022
codes_df = codes_df[codes_df['year'] <= 2022]

# Compute counts per code per year
counts = codes_df.groupby(['code','year']).size().reset_index(name='count')

# Build all years range per code
min_year = counts['year'].min()
max_year = counts['year'].max()
all_years = list(range(min_year, max_year+1))

codes_list = counts['code'].unique()
records = []
alpha = 0.2
for code in codes_list:
    sub = counts[counts['code']==code].set_index('year')['count']
    ema_prev = None
    for y in all_years:
        c = sub.get(y, 0)
        if ema_prev is None:
            ema = c
        else:
            ema = alpha*c + (1-alpha)*ema_prev
        ema_prev = ema
        records.append({'code': code, 'year': y, 'ema': float(ema)})

ema_df = pd.DataFrame(records)

# For each year, find max EMA and corresponding codes
best_per_year = ema_df.loc[ema_df.groupby('year')['ema'].idxmax()].copy()

# Filter best year 2022
best_2022 = best_per_year[best_per_year['year']==2022]

# Now filter codes to level 5 symbols
defs_df = pd.DataFrame(defs)
level5 = set(defs_df['symbol'])

best_2022_lvl5 = best_2022[best_2022['code'].isin(level5)]

result_codes = sorted(best_2022_lvl5['code'].unique())

import json as _json
out = _json.dumps(result_codes)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_X076QFpcvZuemVYnuz1mRNnD': 'file_storage/call_X076QFpcvZuemVYnuz1mRNnD.json', 'var_call_i2NFJPXRMyTNmomOryoCsc6l': 'file_storage/call_i2NFJPXRMyTNmomOryoCsc6l.json'}

exec(code, env_args)
