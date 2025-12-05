code = """import json, pandas as pd
from datetime import datetime

# Load full results from files
with open(var_call_ycwM8dbXCmOzNay1RgbtBQrc, 'r') as f:
    cpc_level5 = json.load(f)
with open(var_call_fZuoN6rksAhTGNcC5noPmcUm, 'r') as f:
    pubs = json.load(f)

level5_symbols = set(row['symbol'] for row in cpc_level5)

records = []
for row in pubs:
    cpc_str = row['cpc']
    pub_date_str = row['publication_date']
    try:
        year = datetime.strptime(pub_date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%b %d, %Y').year
    except Exception:
        try:
            year = datetime.strptime(pub_date_str.replace('st','').replace('nd','').replace('rd','').replace('th',''), '%B %d, %Y').year
        except Exception:
            continue
    try:
        cpc_list = json.loads(cpc_str)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        base = code.split()[0]
        if base in level5_symbols:
            records.append({'symbol': base, 'year': year})

if not records:
    result = []
else:
    df = pd.DataFrame(records)
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')
    years = sorted(counts['year'].unique())
    alpha = 0.2
    ema_rows = []
    for sym, grp in counts.groupby('symbol'):
        grp = grp.set_index('year').reindex(years, fill_value=0)
        ema = None
        for y in years:
            c = grp.loc[y, 'count']
            ema = c if ema is None else alpha*c + (1-alpha)*ema
            ema_rows.append({'symbol': sym, 'year': y, 'ema': ema})
    ema_df = pd.DataFrame(ema_rows)
    best_year = ema_df.loc[ema_df.groupby('symbol')['ema'].idxmax()][['symbol','year','ema']]
    best_2022 = best_year[best_year['year'] == 2022]
    result = sorted(best_2022['symbol'].unique().tolist())

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ycwM8dbXCmOzNay1RgbtBQrc': 'file_storage/call_ycwM8dbXCmOzNay1RgbtBQrc.json', 'var_call_fZuoN6rksAhTGNcC5noPmcUm': 'file_storage/call_fZuoN6rksAhTGNcC5noPmcUm.json'}

exec(code, env_args)
