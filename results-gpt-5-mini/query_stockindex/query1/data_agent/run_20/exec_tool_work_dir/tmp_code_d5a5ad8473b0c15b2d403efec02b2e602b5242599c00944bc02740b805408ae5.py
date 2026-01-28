code = """import pandas as pd
import json

# Load the large query result from the provided storage file path
fp = var_call_7iJIvMeyYKTKdc3tk4zD3ec9
with open(fp, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure numeric columns
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates robustly
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# Filter for dates since 2020-01-01
df = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')]

# Drop invalid/missing prices and avoid division by zero
df = df.dropna(subset=['Open','High','Low'])
df = df[df['Open'] != 0]

# Compute intraday volatility
df['volatility'] = (df['High'] - df['Low']) / df['Open']

# Aggregate by index
grp = df.groupby('Index').agg(mean_volatility=('volatility','mean'), days=('volatility','count')).reset_index()

# Prepare result
if grp.empty:
    result = {'error': 'No valid data since 2020 for the selected Asian indices.'}
else:
    # Find the index with highest average volatility
    top = grp.loc[grp['mean_volatility'].idxmax()]
    result = {
        'index': str(top['Index']),
        'average_intraday_volatility': float(top['mean_volatility']),
        'volatility_unit': 'fraction_of_open',
        'days_counted': int(top['days']),
        'region': 'Asia'
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_s3pmaLCztPPPbMM2jWCjBOJ8': ['index_trade'], 'var_call_B0gF3mFh1b6CCoEQLS8QdDgL': ['index_info'], 'var_call_0g5j5weqccYhwLStHxUMVhiO': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_7iJIvMeyYKTKdc3tk4zD3ec9': 'file_storage/call_7iJIvMeyYKTKdc3tk4zD3ec9.json'}

exec(code, env_args)
