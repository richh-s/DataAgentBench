code = """import json, pandas as pd
from datetime import datetime

# Stream publication data file to avoid heavy memory/processing
with open(var_call_qgqDs0gu0pcwZOACJWIDU0ah, 'r') as f:
    pub_data = json.load(f)

rows = []
for rec in pub_data:
    date_str = rec.get('publication_date')
    cpc_str = rec.get('cpc')
    if not date_str or not cpc_str:
        continue
    try:
        year = datetime.strptime(date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%b %d, %Y').year
    except Exception:
        continue
    if year > 2022:
        continue
    try:
        codes = [e['code'] for e in json.loads(cpc_str)]
    except Exception:
        continue
    for code in codes:
        rows.append({'year': year, 'code': code})

if not rows:
    result = json.dumps([])
else:
    df = pd.DataFrame(rows)
    counts = df.groupby(['code','year']).size().reset_index(name='count')
    # Compute EMA per code directly in year order without full reindex across all years
    alpha = 0.2
    best_records = []  # to store best year per code
    for code, grp in counts.groupby('code'):
        grp = grp.sort_values('year')
        ema = None
        best_ema = None
        best_year = None
        last_year = None
        for _, row in grp.iterrows():
            year = row['year']
            count = row['count']
            # If there are gaps in years, we still apply EMA with zero counts for missing years
            if last_year is not None and year > last_year + 1:
                for y in range(last_year+1, year):
                    ema = count*0 if ema is None else (alpha*0 + (1-alpha)*ema)
                    if best_ema is None or ema > best_ema:
                        best_ema = ema
                        best_year = y
            if ema is None:
                ema = count
            else:
                ema = alpha*count + (1-alpha)*ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = year
            last_year = year
        best_records.append({'code': code, 'year': int(best_year), 'ema': float(best_ema)})

    best_df = pd.DataFrame(best_records)
    best_2022 = best_df[best_df['year'] == 2022]
    codes_2022 = best_2022['code'].tolist()

    with open(var_call_v5lkZzO6tWkJEvwfE6Fmp87d, 'r') as f:
        cpc_defs = json.load(f)
    lvl5 = pd.DataFrame(cpc_defs)
    lvl5_syms = set(lvl5['symbol'].astype(str).tolist())

    lvl5_codes_2022 = sorted([c for c in codes_2022 if c.split('/')[0] in lvl5_syms])
    result = json.dumps(lvl5_codes_2022)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_qgqDs0gu0pcwZOACJWIDU0ah': 'file_storage/call_qgqDs0gu0pcwZOACJWIDU0ah.json', 'var_call_v5lkZzO6tWkJEvwfE6Fmp87d': 'file_storage/call_v5lkZzO6tWkJEvwfE6Fmp87d.json'}

exec(code, env_args)
