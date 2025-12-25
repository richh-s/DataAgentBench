code = """import pandas as pd, json
from datetime import datetime

# load full large result
path = var_call_KgUTIN0a71v4nsGLkllewCuM
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# coerce numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# parse dates leniently and filter since 2020-01-01
# dates are mixed formats, let pandas infer
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
cutoff = pd.Timestamp('2020-01-01')
df = df[df['Date'] >= cutoff]

# compute intraday volatility
df = df[df['Open'] > 0]
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# map Asia indices based on knowledge
asia_indices = {'N225': 'Tokyo Stock Exchange',
                'HSI': 'Hong Kong Stock Exchange',
                '000001.SS': 'Shanghai Stock Exchange',
                '399001.SZ': 'Shenzhen Stock Exchange',
                'NSEI': 'National Stock Exchange of India',
                'TWII': 'Taiwan Stock Exchange',
                'KS11': 'Korea Exchange'}

asia_df = df[df['Index'].isin(asia_indices.keys())]

result = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False).reset_index()

answer = {
    'asia_intraday_vol_rank': result.to_dict(orient='records')
}

import json as _json
out = _json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_eykqSZHFfcR9b52OcZcpuGGH': ['index_info'], 'var_call_XQXT9XiJbf9dwEQPpDxTmvi9': ['index_trade'], 'var_call_EKLtCnT2z4A5Z5InhKzYtYEj': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_9q2kfhxHlZxyJcU6ULweyMSU': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}, {'Index': 'IXIC'}], 'var_call_KgUTIN0a71v4nsGLkllewCuM': 'file_storage/call_KgUTIN0a71v4nsGLkllewCuM.json'}

exec(code, env_args)
