code = """import json, pandas as pd, os

path = var_call_hO475OvXsyxqoRpBquTIe5KE
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Map indices to regions using knowledge
north_american_indices = {'NYA', 'IXIC', 'GSPTSE'}  # NYSE Composite, Nasdaq, S&P/TSX Composite

na_df = df[df['Index'].isin(north_american_indices)].copy()

up_down = na_df.groupby('Index').apply(lambda x: pd.Series({
    'up_days': (x['Close'] > x['Open']).sum(),
    'down_days': (x['Close'] < x['Open']).sum()
})).reset_index()

more_up = up_down[up_down['up_days'] > up_down['down_days']]['Index'].tolist()

result = json.dumps({'indices_with_more_up_than_down_2018_North_America': more_up})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_QVu5YBV9FD85mdVIFGwhG8fM': ['index_info'], 'var_call_hk8PcFrdQWJTFofnjRHHdDWs': ['index_trade'], 'var_call_0rK0lqgbOgcWuqXUt4Qk6kF0': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_jubBvPNOfnIrgovUqnRtarm4': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_call_hO475OvXsyxqoRpBquTIe5KE': 'file_storage/call_hO475OvXsyxqoRpBquTIe5KE.json'}

exec(code, env_args)
