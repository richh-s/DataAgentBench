code = """import json, pandas as pd

# Stream-load publication data to reduce memory
with open(var_call_X076QFpcvZuemVYnuz1mRNnD, 'r') as f:
    pub = json.load(f)

with open(var_call_i2NFJPXRMyTNmomOryoCsc6l, 'r') as f:
    defs = json.load(f)

pub_df = pd.DataFrame(pub, columns=['publication_date','cpc'])

months = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(d):
    if not isinstance(d,str) or not d.strip():
        return None
    parts = d.replace(',','').split()
    if len(parts) < 3:
        return None
    try:
        year = int(parts[2])
    except:
        return None
    return year

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

codes = []
for year, grp in pub_df.groupby('year'):
    if year > 2022:
        continue
    for _, row in grp.iterrows():
        try:
            lst = json.loads(row['cpc'])
        except Exception:
            continue
        for entry in lst:
            code = entry.get('code')
            if code:
                codes.append({'code': code, 'year': year})

codes_df = pd.DataFrame(codes)

counts = codes_df.groupby(['code','year']).size().reset_index(name='count')

min_year = counts['year'].min()
max_year = counts['year'].max()
all_years = list(range(min_year, max_year+1))

alpha = 0.2
records = []
for code, sub in counts.groupby('code'):
    sub = sub.set_index('year')['count']
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

best_idx = ema_df.groupby('year')['ema'].idxmax()
best_per_year = ema_df.loc[best_idx].copy()

best_2022 = best_per_year[best_per_year['year']==2022]

defs_df = pd.DataFrame(defs)
level5 = set(defs_df['symbol'])

best_2022_lvl5 = best_2022[best_2022['code'].isin(level5)]

result_codes = sorted(best_2022_lvl5['code'].unique())

out = json.dumps(result_codes)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_X076QFpcvZuemVYnuz1mRNnD': 'file_storage/call_X076QFpcvZuemVYnuz1mRNnD.json', 'var_call_i2NFJPXRMyTNmomOryoCsc6l': 'file_storage/call_i2NFJPXRMyTNmomOryoCsc6l.json'}

exec(code, env_args)
