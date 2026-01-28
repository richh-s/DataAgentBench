code = """import json, pandas as pd, re

# Load full trade data
path = var_call_OOqpO1xYComPUAiHw0dHte1q
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse date
import pandas as pd

def parse_date_series(s):
    s = s.astype(str)
    s = s.str.replace(r"\s+at\s+\d{1,2}:\d{2}\s+[AP]M$", "", regex=True)
    s = s.str.replace(r",\s*\d{2}:\d{2}$", "", regex=True)
    # try pandas general parse
    dt = pd.to_datetime(s, errors='coerce', infer_datetime_format=True)
    # some formats like '31 Dec 1986, 00:00' may not infer; handle explicitly for remaining
    mask = dt.isna()
    if mask.any():
        dt2 = pd.to_datetime(s[mask].str.replace(", 00:00","", regex=False), errors='coerce', format='%d %b %Y')
        dt.loc[mask] = dt2
    return dt

df['dt'] = parse_date_series(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['dt','CloseUSD'])

# Filter since 2000-01-01
start = pd.Timestamp('2000-01-01')
df = df[df['dt'] >= start].copy()

# Monthly investment simulation: invest 1 unit USD at first available trading day of each month
# shares added = 1 / price_on_invest_day
# final value = total_shares * last_price

df = df.sort_values(['Index','dt'])
# month period
_df = df.copy()
_df['month'] = _df['dt'].dt.to_period('M')

# first trading day per index-month
firsts = _df.groupby(['Index','month'], as_index=False).first()[['Index','month','CloseUSD','dt']]
firsts = firsts.rename(columns={'CloseUSD':'price_invest'})
firsts['shares'] = 1.0 / firsts['price_invest']

# total shares per index
shares = firsts.groupby('Index', as_index=False)['shares'].sum()
months_n = firsts.groupby('Index', as_index=False).size().rename(columns={'size':'n_months'})

# last available price per index
lasts = _df.groupby('Index', as_index=False).last()[['Index','CloseUSD','dt']].rename(columns={'CloseUSD':'last_price','dt':'last_dt'})

res = shares.merge(months_n, on='Index').merge(lasts, on='Index')
res['total_invested'] = res['n_months'] * 1.0
res['final_value'] = res['shares'] * res['last_price']
res['multiple'] = res['final_value'] / res['total_invested']
res = res.sort_values('multiple', ascending=False)

# Map index to exchange/country (manual mapping for indices present)
idx_country = {
    'NYA': ('New York Stock Exchange','United States'),
    'IXIC': ('NASDAQ','United States'),
    'HSI': ('Hong Kong Stock Exchange','Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange','China'),
    '399001.SZ': ('Shenzhen Stock Exchange','China'),
    'N225': ('Tokyo Stock Exchange','Japan'),
    'N100': ('Euronext','Multi-country Europe'),
    'GSPTSE': ('Toronto Stock Exchange','Canada'),
    'NSEI': ('National Stock Exchange of India','India'),
    'GDAXI': ('Frankfurt Stock Exchange','Germany'),
    'SSMI': ('SIX Swiss Exchange','Switzerland'),
    'TWII': ('Taiwan Stock Exchange','Taiwan'),
    'J203.JO': ('Johannesburg Stock Exchange','South Africa'),
}
res['Exchange'] = res['Index'].map(lambda x: idx_country.get(x,(None,None))[0])
res['Country'] = res['Index'].map(lambda x: idx_country.get(x,(None,None))[1])

top5 = res.head(5)[['Index','Country','multiple','total_invested','final_value','n_months','last_dt']]
# round
out = top5.copy()
out['multiple'] = out['multiple'].astype(float).round(4)
out['final_value'] = out['final_value'].astype(float).round(4)

print('__RESULT__:')
print(out.to_json(orient='records', date_format='iso'))"""

env_args = {'var_call_IPrUJXbJ0Rv3sNMRI7W96rYp': ['index_trade'], 'var_call_XGJ2iM3oMOFoXJyGBSDD4Ikq': ['index_info'], 'var_call_SQYvS4Wf4oX4BIq1xVszh5EC': [{'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n_rows': '104224', 'n_indices': '13'}], 'var_call_U9UQ8PN66xH14CfnOSMKpLtY': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_konmcszwMtTDjMZs1aWQrecK': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'CloseUSD': '319.865'}], 'var_call_TL2Y85f3p9N4LlqrtbuaKTR9': [{'raw': '31 Dec 1986, 00:00', 'parsed': '1986-12-31'}, {'raw': 'January 02, 1987 at 12:00 AM', 'parsed': '1987-01-02'}, {'raw': 'January 15, 1987 at 12:00 AM', 'parsed': '1987-01-15'}, {'raw': 'January 16, 1987 at 12:00 AM', 'parsed': '1987-01-16'}, {'raw': 'January 19, 1987 at 12:00 AM', 'parsed': '1987-01-19'}], 'var_call_OOqpO1xYComPUAiHw0dHte1q': 'file_storage/call_OOqpO1xYComPUAiHw0dHte1q.json', 'var_call_aZrGu5j1dRK1lbRzQaCBm7Mr': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
