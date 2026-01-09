code = """import json, pandas as pd

# Load large trade data
path = var_call_5pS1LrXb6sukRniDgvzXZ0tP
with open(path, 'r') as f:
    trades = json.load(f)

df = pd.DataFrame(trades)
# Parse
df['dt'] = pd.to_datetime(df['dt'])
df['adj_close_usd'] = pd.to_numeric(df['adj_close_usd'], errors='coerce')
df = df.dropna(subset=['adj_close_usd'])

# Monthly DCA: buy 1 unit of currency each month at first available trading day of month
# Shares bought = 1 / price
# Final value = total_shares * last_price
# Total invested = number_of_months

df['month'] = df['dt'].dt.to_period('M')

# first trading day per index per month
firsts = (df.sort_values(['idx','dt'])
            .groupby(['idx','month'], as_index=False)
            .first()[['idx','month','adj_close_usd']]
            .rename(columns={'adj_close_usd':'buy_price'}))

# last available price per index (overall)
lasts = (df.sort_values(['idx','dt'])
           .groupby('idx', as_index=False)
           .last()[['idx','adj_close_usd']]
           .rename(columns={'adj_close_usd':'last_price'}))

# compute
firsts['shares'] = 1.0 / firsts['buy_price']
agg = firsts.groupby('idx').agg(months=('month','count'), total_shares=('shares','sum')).reset_index()
agg = agg.merge(lasts, on='idx', how='left')
agg['total_invested'] = agg['months'].astype(float)
agg['final_value'] = agg['total_shares'] * agg['last_price']
agg['multiple'] = agg['final_value'] / agg['total_invested']
agg['return_pct'] = (agg['multiple'] - 1.0) * 100.0

# Choose top 5 by return multiple
agg_top = agg.sort_values('multiple', ascending=False).head(5).copy()

# Map index symbol to exchange/country (inferred)
idx_to_exchange_country = {
    'NYA': ('New York Stock Exchange','United States'),
    'IXIC': ('NASDAQ','United States'),
    'HSI': ('Hong Kong Stock Exchange','Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange','China'),
    '399001.SZ': ('Shenzhen Stock Exchange','China'),
    'N225': ('Tokyo Stock Exchange','Japan'),
    'N100': ('Euronext','Europe (multi-country)'),
    'GSPTSE': ('Toronto Stock Exchange','Canada'),
    'NSEI': ('National Stock Exchange of India','India'),
    'GDAXI': ('Frankfurt Stock Exchange','Germany'),
    'SSMI': ('SIX Swiss Exchange','Switzerland'),
    'TWII': ('Taiwan Stock Exchange','Taiwan'),
    'J203.JO': ('Johannesburg Stock Exchange','South Africa'),
}

agg_top['exchange'] = agg_top['idx'].map(lambda x: idx_to_exchange_country.get(x,(None,None))[0])
agg_top['country'] = agg_top['idx'].map(lambda x: idx_to_exchange_country.get(x,(None,None))[1])

out = agg_top[['idx','country','return_pct','multiple','months']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5pS1LrXb6sukRniDgvzXZ0tP': 'file_storage/call_5pS1LrXb6sukRniDgvzXZ0tP.json', 'var_call_vjL7liPhTDZE3FEsFHNyWdu5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_4H5oCG6YwzM70EqtB30EA4X5': [{'idx': 'J203.JO'}, {'idx': 'IXIC'}, {'idx': 'N225'}, {'idx': 'GSPTSE'}, {'idx': 'NSEI'}, {'idx': 'GDAXI'}, {'idx': 'HSI'}, {'idx': '000001.SS'}, {'idx': 'SSMI'}, {'idx': 'TWII'}, {'idx': 'NYA'}, {'idx': 'N100'}, {'idx': '399001.SZ'}]}

exec(code, env_args)
