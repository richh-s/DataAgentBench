code = """import json, pandas as pd

path = var_call_Xtt957nr5Hr6ckdPRSAL9lqg
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# dates seem like '2000-01-04 00:00:00'
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

idx_results = {}
for idx, g in df.groupby('Index'):
    g = g.sort_values('Date')
    g['YearMonth'] = g['Date'].dt.to_period('M')
    last_per_month = g.groupby('YearMonth').tail(1)
    units = (1 / last_per_month['CloseUSD']).sum()
    final_price = g.iloc[-1]['CloseUSD']
    final_value = units * final_price
    total_invested = len(last_per_month)
    idx_results[idx] = {'final_value': float(final_value), 'total_invested': int(total_invested)}

res = sorted(idx_results.items(), key=lambda x: x[1]['final_value'], reverse=True)

top5 = [{"Index": i, "final_value": v['final_value'], "total_invested": v['total_invested']} for i, v in res[:5]]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_hLW5qrHLPGpQCI8OIF2VxqAU': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}], 'var_call_GLxfrhWvhYGCppliHsOnny4R': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_dOnutghQJTdkJ4CsNPtoFLXk': ['index_info'], 'var_call_Xtt957nr5Hr6ckdPRSAL9lqg': 'file_storage/call_Xtt957nr5Hr6ckdPRSAL9lqg.json'}

exec(code, env_args)
