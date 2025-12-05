code = """import json, pandas as pd, os

path = var_call_8CLwInRFT1CL7VndpSQbSMfG
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure numeric
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates flexibly, then filter since 2020-01-01
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
mask = df['Date_parsed'] >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# Compute intraday volatility
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Focus on Asian indices using mapping from previous step
asia_indices = {"N225","HSI","000001.SS","399001.SZ","NSEI","TWII"}

asia_df = df[df['Index'].isin(list(asia_indices))].copy()

result_series = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)
result = {
    'by_index': result_series.to_dict(),
    'max_index': result_series.idxmax() if not result_series.empty else None,
    'max_value': float(result_series.max()) if not result_series.empty else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4GHR255VWY41xrmTC8kVAANp': ['index_info'], 'var_call_G9t572CzGWpDVaLO8U18NTJC': ['index_trade'], 'var_call_Q3hnhvVNTkCDTB3Xm7cTojYo': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_FCjCiruIRzmtD5mHIATCqnWE': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_js0zNsOTvkQDMdtRNZ709ASB': {'Tokyo Stock Exchange': 'N225', 'Hong Kong Stock Exchange': 'HSI', 'Shanghai Stock Exchange': '000001.SS', 'Shenzhen Stock Exchange': '399001.SZ', 'National Stock Exchange of India': 'NSEI', 'Korea Exchange': None, 'Taiwan Stock Exchange': 'TWII'}, 'var_call_8CLwInRFT1CL7VndpSQbSMfG': 'file_storage/call_8CLwInRFT1CL7VndpSQbSMfG.json'}

exec(code, env_args)
