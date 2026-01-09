code = """import json, pandas as pd
from datetime import datetime

# Load large trade data
path = var_call_cdYJK8YU4jTSi0V78wDLkN4r
with open(path, 'r') as f:
    trades = json.load(f)

df = pd.DataFrame(trades)
# Parse types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Create month period and month-end close (last available trading day in month)
df['Month'] = df['Date'].dt.to_period('M')
df = df.sort_values(['Index','Date'])
month_end = df.groupby(['Index','Month'], as_index=False).tail(1)
month_end = month_end[['Index','Month','CloseUSD']].rename(columns={'CloseUSD':'P'})

# Compute monthly returns per index: r_t = P_t/P_{t-1} - 1
month_end = month_end.sort_values(['Index','Month'])
month_end['P_prev'] = month_end.groupby('Index')['P'].shift(1)
month_end['r'] = month_end['P']/month_end['P_prev'] - 1
# For first month, set return 0 so a contribution at first month grows from then on
month_end.loc[month_end['P_prev'].isna(), 'r'] = 0.0

# DCA growth of $1 each month at month-end: V_t = (V_{t-1}+1)*(1+r_t)
month_end['V'] = 0.0
for idx, grp in month_end.groupby('Index', sort=False):
    V = 0.0
    Vs = []
    for r in grp['r'].tolist():
        V = (V + 1.0) * (1.0 + float(r))
        Vs.append(V)
    month_end.loc[grp.index, 'V'] = Vs

final = month_end.groupby('Index').agg(
    final_value=('V','last'),
    months=('Month','nunique')
).reset_index()
final['total_contributed'] = final['months'].astype(float)
final['multiple'] = final['final_value'] / final['total_contributed']

# Map Index to Exchange/Country via known major index symbols
index_to_exchange_country = {
    'NYA': ('New York Stock Exchange', 'United States'),
    'IXIC': ('NASDAQ', 'United States'),
    'HSI': ('Hong Kong Stock Exchange', 'Hong Kong'),
    '000001.SS': ('Shanghai Stock Exchange', 'China'),
    '399001.SZ': ('Shenzhen Stock Exchange', 'China'),
    'N225': ('Tokyo Stock Exchange', 'Japan'),
    'N100': ('Euronext', 'Europe (Euronext)'),
    'GSPTSE': ('Toronto Stock Exchange', 'Canada'),
    'NSEI': ('National Stock Exchange of India', 'India'),
    'GDAXI': ('Frankfurt Stock Exchange', 'Germany'),
    'SSMI': ('SIX Swiss Exchange', 'Switzerland'),
    'TWII': ('Taiwan Stock Exchange', 'Taiwan'),
    'J203.JO': ('Johannesburg Stock Exchange', 'South Africa')
}
final['Exchange'] = final['Index'].map(lambda x: index_to_exchange_country.get(x,(None,None))[0])
final['Country'] = final['Index'].map(lambda x: index_to_exchange_country.get(x,(None,None))[1])

# Rank by final_value (overall DCA ending value for $1/mo)
top5 = final.sort_values('final_value', ascending=False).head(5)
# Round for display
out = top5[['Index','Country','final_value','months','total_contributed','multiple']].copy()
out['final_value'] = out['final_value'].round(2)
out['multiple'] = out['multiple'].round(2)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cdYJK8YU4jTSi0V78wDLkN4r': 'file_storage/call_cdYJK8YU4jTSi0V78wDLkN4r.json', 'var_call_2oKMb0PaA2ngdMphCZCkEv5f': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_FJWTtNrY3koii8MvAYeLaIwT': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
