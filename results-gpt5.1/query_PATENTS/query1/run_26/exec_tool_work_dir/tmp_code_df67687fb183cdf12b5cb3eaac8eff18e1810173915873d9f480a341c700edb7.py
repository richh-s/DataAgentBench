code = """import json, pandas as pd
from datetime import datetime

# load full large results
with open(var_call_JHeEfRq46LvnhXDOKyREh6k9, 'r') as f:
    pub_data = json.load(f)
with open(var_call_y7yN6J1VoIHOvsHBTncQ4xc4, 'r') as f:
    cpc_lvl5 = json.load(f)

# build dataframe of level-5 CPC symbols
cpc5_set = {r['symbol'] for r in cpc_lvl5}

# helper to parse natural language dates -> year
months = {m: i for i, m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], start=1)}

def parse_year(d):
    if not d or not isinstance(d,str):
        return None
    try:
        parts = d.replace(',', '').split()
        # expect formats like "Aug 3rd, 2021" or "August 3rd, 2021"
        mon = parts[0][:3]
        year = int(parts[-1])
        if mon in months:
            return year
    except Exception:
        return None
    return year

rows = []
for r in pub_data:
    y = parse_year(r.get('publication_date'))
    if not y:
        continue
    try:
        cpc_list = json.loads(r.get('cpc') or '[]')
    except Exception:
        continue
    for e in cpc_list:
        code = e.get('code')
        if code in cpc5_set:
            rows.append({'year': y, 'symbol': code})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # yearly counts per symbol
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    # compute EMA per symbol sorted by year
    alpha = 0.2
    ema_records = []
    for sym, grp in counts.sort_values('year').groupby('symbol'):
        ema = None
        for _, row in grp.iterrows():
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_records.append({'symbol': sym, 'year': int(row['year']), 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_records)
    # determine best year (max EMA) per symbol
    idx = ema_df.groupby('symbol')['ema'].idxmax()
    best = ema_df.loc[idx]
    # filter where best year is 2022
    best2022 = best[best['year']==2022]
    result = sorted(best2022['symbol'].unique().tolist())

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_JHeEfRq46LvnhXDOKyREh6k9': 'file_storage/call_JHeEfRq46LvnhXDOKyREh6k9.json', 'var_call_y7yN6J1VoIHOvsHBTncQ4xc4': 'file_storage/call_y7yN6J1VoIHOvsHBTncQ4xc4.json'}

exec(code, env_args)
