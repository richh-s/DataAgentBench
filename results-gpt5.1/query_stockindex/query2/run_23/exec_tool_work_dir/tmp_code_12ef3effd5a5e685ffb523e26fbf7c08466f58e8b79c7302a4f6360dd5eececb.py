code = """import json, pandas as pd
from pathlib import Path

# Load 2018 index trade data
file_path = Path(var_call_CynC4Paf70mPLXzhlYDaDLlM)
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Identify North American indices using knowledge of symbols
# NYA - NYSE Composite (New York, USA)
# IXIC - NASDAQ Composite (USA)
# GSPTSE - S&P/TSX Composite (Canada)
na_indices = ['NYA', 'IXIC', 'GSPTSE']

na_df = df[df['Index'].isin(na_indices)].copy()

# Classify up and down days
na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary[summary['more_up_than_down']][['Index', 'up_days', 'down_days']].to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_PwMDj88KbHYopqkAuxQULG4z': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_FLUKlzEFduHU3vHqd0x39Tq6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_CynC4Paf70mPLXzhlYDaDLlM': 'file_storage/call_CynC4Paf70mPLXzhlYDaDLlM.json'}

exec(code, env_args)
