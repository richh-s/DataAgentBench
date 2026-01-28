code = """import json, pandas as pd

# load trade records
path = var_call_rAU0WcZkEisz5o0QuhT1Sy29
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# numeric
for c in ['Open','Close']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
# date filtering robust
df['Date'] = pd.to_datetime(df['Date'])
df = df[(df['Date']>= '2018-01-01') & (df['Date']< '2019-01-01')]

# North America indices in this dataset inferred from exchanges: NYSE->NYA, NASDAQ->IXIC, Toronto->GSPTSE
north_america = {
    'NYA': 'New York Stock Exchange (NYSE Composite)',
    'IXIC': 'NASDAQ Composite',
    'GSPTSE': 'Toronto Stock Exchange (S&P/TSX Composite)'
}
ndf = df[df['Index'].isin(north_america.keys())].copy()

# up/down counts
ndf['up'] = ndf['Close'] > ndf['Open']
ndf['down'] = ndf['Close'] < ndf['Open']
summary = ndf.groupby('Index').agg(up_days=('up','sum'), down_days=('down','sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

res = summary[summary['more_up_than_down']].copy()
res['name'] = res['Index'].map(north_america)
res = res[['Index','name','up_days','down_days']].sort_values('Index')

print('__RESULT__:')
print(res.to_json(orient='records'))"""

env_args = {'var_call_UHY8j7WunpngbLsS5LmPfLot': ['index_info'], 'var_call_UEkhfeyvG9dW6Vvo1do4rgRH': ['index_trade'], 'var_call_G8HGngN6Eb5Zhvlpcwga1KdP': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_rAU0WcZkEisz5o0QuhT1Sy29': 'file_storage/call_rAU0WcZkEisz5o0QuhT1Sy29.json'}

exec(code, env_args)
