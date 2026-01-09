code = """import json, pandas as pd
from datetime import datetime

# Load trade data
path = var_call_fkaiF7JV4IeV1T321tMyZdoz
with open(path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# coerce
for c in ['CloseUSD']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

def parse_date(x):
    if x is None:
        return pd.NaT
    s = str(x)
    # try pandas parser
    try:
        return pd.to_datetime(s, errors='coerce', utc=False)
    except Exception:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)
# filter from 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['Date_parsed'].notna() & (df['Date_parsed'] >= start) & df['CloseUSD'].notna()]

# monthly DCA: invest 1 unit on first trading day of each month => shares = 1/price
# total invested = n_months; final value = sum(shares)*last_price

df['Month'] = df['Date_parsed'].dt.to_period('M')
# first trading day row per index-month
first_rows = df.sort_values(['Index','Date_parsed']).groupby(['Index','Month'], as_index=False).first()
first_rows['shares'] = 1.0 / first_rows['CloseUSD']
shares_sum = first_rows.groupby('Index', as_index=False)['shares'].sum().rename(columns={'shares':'total_shares'})

# last available price per index
last_price = df.sort_values(['Index','Date_parsed']).groupby('Index', as_index=False).last()[['Index','CloseUSD']].rename(columns={'CloseUSD':'last_price'})

res = shares_sum.merge(last_price, on='Index', how='inner')
# invested dollars = number of months contributed
months = first_rows.groupby('Index', as_index=False).size().rename(columns={'size':'n_months'})
res = res.merge(months, on='Index', how='inner')
res['final_value'] = res['total_shares'] * res['last_price']
res['total_invested'] = res['n_months'] * 1.0
res['multiple'] = res['final_value'] / res['total_invested']
res['return_pct'] = (res['multiple'] - 1.0) * 100.0

res_top5 = res.sort_values('multiple', ascending=False).head(5)

# map index to country manually using domain knowledge
country_map = {
    'IXIC': 'United States',
    'NYA': 'United States',
    'N225': 'Japan',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'SSMI': 'Switzerland',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N100': 'Eurozone (pan-European)',
    'TWII': 'Taiwan',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}
res_top5['Country'] = res_top5['Index'].map(country_map)

out = res_top5[['Index','Country','n_months','total_invested','last_price','final_value','multiple','return_pct']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vNeQ2TsMsf9KWhS9XjpuYhiS': ['index_info'], 'var_call_gioHogdQr1f8RGlOOePgYCRH': ['index_trade'], 'var_call_t1ZMyaCv1ixjNPzyLHSRSDG8': [{'Index': 'NYA', 'min_date_raw': '01 Apr 1969, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': 'N225', 'min_date_raw': '01 Apr 1971, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'IXIC', 'min_date_raw': '01 Apr 1974, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'GSPTSE', 'min_date_raw': '01 Apr 1981, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'GDAXI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'HSI', 'min_date_raw': '01 Apr 1992, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'SSMI', 'min_date_raw': '01 Apr 1996, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': '000001.SS', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': 'N100', 'min_date_raw': '01 Apr 2003, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': 'TWII', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': '399001.SZ', 'min_date_raw': '01 Apr 2004, 00:00', 'max_date_raw': 'September 30, 2015 at 12:00 AM', 'n': '5760'}, {'Index': 'NSEI', 'min_date_raw': '01 Apr 2014, 00:00', 'max_date_raw': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'J203.JO', 'min_date_raw': '01 Apr 2016, 00:00', 'max_date_raw': 'September 30, 2019 at 12:00 AM', 'n': '2346'}], 'var_call_fkaiF7JV4IeV1T321tMyZdoz': 'file_storage/call_fkaiF7JV4IeV1T321tMyZdoz.json'}

exec(code, env_args)
