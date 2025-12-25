code = """import json, pandas as pd

# Load full data from file path
file_path = var_call_wD2OUO8RTh9R0euY7lC2v0vg
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric types
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Filter to North American indices: NYA (NYSE, US), IXIC (NASDAQ, US), GSPTSE (Toronto, Canada)
na_indices = ['NYA', 'IXIC', 'GSPTSE']
na_df = df[df['Index'].isin(na_indices)].copy()

# Classify days
na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_aBVH1cKGmy636Epu3AKqiwes': ['index_info'], 'var_call_VDWBktvckZE2aHGEd4g4b0oo': ['index_trade'], 'var_call_02qFcnibScl2GVUuEGY48x9X': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_a15lypBEflUor4DCO9auxj58': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_wD2OUO8RTh9R0euY7lC2v0vg': 'file_storage/call_wD2OUO8RTh9R0euY7lC2v0vg.json'}

exec(code, env_args)
