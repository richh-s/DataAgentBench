code = """import json, pandas as pd
import os

path = var_call_2IFkUPlb1iRZ8SNcywh9WTn6
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['Open','Close']:
    df[col] = df[col].astype(float)

summary = df.groupby('Index').apply(lambda g: pd.Series({
    'up_days': int((g['Close'] > g['Open']).sum()),
    'down_days': int((g['Close'] < g['Open']).sum())
})).reset_index()

north_american = ['NYA','IXIC','GSPTSE']
result_indices = summary[(summary['Index'].isin(north_american)) & (summary['up_days'] > summary['down_days'])]['Index'].tolist()

result = json.dumps(result_indices)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_kVBEI9tpRc9xh1lBsswoKPN2': ['index_info'], 'var_call_z5Dkd1wLfL119b3kjLuyrq7V': ['index_trade'], 'var_call_1lhie2nyYFGvGsmOrSamlpWZ': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_WfAwoOhSBdxQg6pCJE2vpdKF': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_2IFkUPlb1iRZ8SNcywh9WTn6': 'file_storage/call_2IFkUPlb1iRZ8SNcywh9WTn6.json'}

exec(code, env_args)
