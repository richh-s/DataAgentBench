code = """import json, pandas as pd
import os

path = var_call_WmP9jiRNjcmxb4xoiv7LXMEg
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# assume $1 invested at the close of each month starting Jan 2000 (or first available month) to latest
monthly = df.sort_values(['Index','Date']).groupby(['Index', df['Date'].dt.to_period('M')]).tail(1)
monthly['month_index'] = monthly.groupby('Index').cumcount()
monthly['units_bought'] = 1.0 / monthly['Adj Close']
monthly['cum_units'] = monthly.groupby('Index')['units_bought'].cumsum()
# portfolio value at last available price
latest = df.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']].set_index('Index')
final_values = monthly.groupby('Index').tail(1).set_index('Index')['cum_units'] * latest['Adj Close']
final_values = final_values.reset_index().rename(columns={0:'final_value'})

# rank and get top 5
final_values = final_values.sort_values(0 if 0 in final_values.columns else 'cum_units' if 'cum_units' in final_values.columns else final_values.columns[-1], ascending=False)

result = final_values.head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hJyi8zpCFsmhh3IRJiglF9Tq': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_oBynURMhGvtkOzpFCABBqZoL': [{'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_cwmyffPB81JJ1ZdI3Lo7pQFm': ['index_info'], 'var_call_WmP9jiRNjcmxb4xoiv7LXMEg': 'file_storage/call_WmP9jiRNjcmxb4xoiv7LXMEg.json'}

exec(code, env_args)
