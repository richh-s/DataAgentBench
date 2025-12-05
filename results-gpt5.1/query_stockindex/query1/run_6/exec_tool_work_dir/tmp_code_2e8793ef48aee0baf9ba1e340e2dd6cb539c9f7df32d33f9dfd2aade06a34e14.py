code = """import json, pandas as pd
import os

path = var_call_k20AEvSnyaGmR3H9ve1Q9Vht
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric types
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates with errors coerced, then filter since 2020-01-01
# Dates appear in multiple textual formats, so let pandas infer
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
mask = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
df = df[mask].dropna(subset=['Open','High','Low'])

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

result_series = df.groupby('Index')['vol'].mean().sort_values(ascending=False)

result = {"ranked_indices": result_series.index.tolist(),
          "avg_vol": result_series.values.tolist(),
          "top_index": result_series.index[0] if len(result_series)>0 else None,
          "top_avg_vol": float(result_series.iloc[0]) if len(result_series)>0 else None}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4914CCCT8ojSE8x7sELIRbjg': ['index_info'], 'var_call_vyocvVs7DlTTEZUxJIRc2p0w': ['index_trade'], 'var_call_U1PR7Aorhu96xtF2ry8rj2Kq': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_vzmKuR61dKH6HhondX7sVftU': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_call_NsZBAhEwym1UASCGVqngM6O7': {'asia_indices': ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']}, 'var_call_k20AEvSnyaGmR3H9ve1Q9Vht': 'file_storage/call_k20AEvSnyaGmR3H9ve1Q9Vht.json'}

exec(code, env_args)
