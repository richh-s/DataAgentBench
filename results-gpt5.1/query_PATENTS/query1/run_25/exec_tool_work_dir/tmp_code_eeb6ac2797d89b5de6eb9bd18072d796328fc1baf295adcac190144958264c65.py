code = """import json, pandas as pd

with open(var_call_uClG0tE5MLrn8jrG96iRy7dF, 'r') as f:
    pub_data = json.load(f)
with open(var_call_5wrFHkRrJehrps8VNqqW8XyI, 'r') as f:
    defs_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

def parse_year(d):
    if not isinstance(d,str):
        return None
    parts = d.replace(',','').split()
    for p in parts:
        if p.isdigit() and len(p)==4:
            return int(p)
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)

pub_df = pub_df[pub_df['year'].isin([2020,2021,2022])].copy()

records = []
for _, row in pub_df.iterrows():
    cpc_str = row['cpc']
    try:
        codes = json.loads(cpc_str)
    except Exception:
        continue
    for entry in codes:
        code = entry.get('code')
        if code:
            records.append({'year': row['year'], 'code': code})

cpc_df = pd.DataFrame(records)

# If no records or empty, return empty list
if cpc_df.empty:
    out = json.dumps([])
    print("__RESULT__:")
    print(out)
else:
    defs_df = pd.DataFrame(defs_data)
    level5_set = set(defs_df['symbol'].astype(str).unique())
    cpc_df = cpc_df[cpc_df['code'].isin(level5_set)].copy()

    counts = cpc_df.groupby(['code','year']).size().reset_index(name='count')

    all_years = [2020,2021,2022]
    idx = pd.MultiIndex.from_product([counts['code'].unique(), all_years], names=['code','year'])
    counts = counts.set_index(['code','year']).reindex(idx, fill_value=0).reset_index()

    alpha = 0.2
    ema_records = []
    for code, grp in counts.groupby('code'):
        grp = grp.sort_values('year')
        ema = None
        for _, r in grp.iterrows():
            c = r['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_records.append({'code': code, 'year': int(r['year']), 'ema': float(ema)})

    ema_df = pd.DataFrame(ema_records)

    result_rows = []
    for year, grp in ema_df.groupby('year'):
        max_ema = grp['ema'].max()
        top_codes = grp[grp['ema'] == max_ema]['code'].tolist()
        for code in top_codes:
            result_rows.append({'year': int(year), 'code': code, 'ema': float(max_ema)})

    result_df = pd.DataFrame(result_rows)

    best_years = ema_df.loc[ema_df.groupby('code')['ema'].idxmax()][['code','year']]
    best_years = best_years.rename(columns={'year':'best_year'})

    merged = pd.merge(result_df, best_years, on='code')
    final = merged[merged['best_year'] == 2022]

    final_codes = sorted(final['code'].unique().tolist())

    out = json.dumps(final_codes)
    print("__RESULT__:")
    print(out)"""

env_args = {'var_call_uClG0tE5MLrn8jrG96iRy7dF': 'file_storage/call_uClG0tE5MLrn8jrG96iRy7dF.json', 'var_call_5wrFHkRrJehrps8VNqqW8XyI': 'file_storage/call_5wrFHkRrJehrps8VNqqW8XyI.json'}

exec(code, env_args)
