code = """import json, pandas as pd

eligible = pd.DataFrame(var_call_WgKuC0Y2K5exQqoO7w21o7ZM)
eligible['first_date'] = pd.to_datetime(eligible['first_date'], dayfirst=True)
start = pd.Timestamp('2000-01-01')
idxs = eligible.loc[eligible['first_date']<=start, 'Index'].tolist()

path = var_call_3MpHtGNePlLzJywnCLGjtSoO
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Index'].isin(idxs)]

monthly_nav = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    g = g[g['Date']>=start]
    if g.empty:
        continue
    g['YearMonth'] = g['Date'].dt.to_period('M')
    monthly = g.groupby('YearMonth').first().reset_index()
    monthly = monthly.sort_values('YearMonth')
    contrib = 100.0
    units = 0.0
    nav = 0.0
    for _, row in monthly.iterrows():
        price = float(row['Adj Close'])
        units += contrib/price
        nav = units*price
    monthly_nav.append({'Index': idx, 'final_nav': nav, 'months': len(monthly)})

res = pd.DataFrame(monthly_nav)
res = res.sort_values('final_nav', ascending=False).head(5)
result = res.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WgKuC0Y2K5exQqoO7w21o7ZM': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_3MpHtGNePlLzJywnCLGjtSoO': 'file_storage/call_3MpHtGNePlLzJywnCLGjtSoO.json', 'var_call_cPKCsYNQyNPQwOVBGsoZys7a': ['index_info']}

exec(code, env_args)
