code = """import json, pandas as pd

# Load full index_trade data from file path
file_path = var_call_YJTe5dkiz6oxRVD990YFDoRk
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric types
for col in ['Open', 'High', 'Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse date and filter since 2020-01-01
# Dates are messy strings; let pandas infer
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
mask = df['Date'] >= pd.Timestamp('2020-01-01')
df = df[mask].copy()

# Compute intraday volatility
df = df[df['Open'] > 0]
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Determine which indices are Asia based on known mappings of exchanges/regions
# From indexinfo_database exchanges list
exchanges = [row['Exchange'] for row in var_call_7oK7cTK5jq70lYtw66qllqb1]

# Map major index symbols to regions using geographic knowledge
asia_indices = set([
    'N225',   # Tokyo Stock Exchange, Japan
    'HSI',    # Hong Kong Stock Exchange, Hong Kong
    '000001.SS', # Shanghai Stock Exchange, China
    '399001.SZ', # Shenzhen Stock Exchange, China (if present)
    '399006.SZ', # ChiNext, Shenzhen (if present)
    '^BSESN',    # BSE Sensex (if present)
    '^NSEI',     # Nifty 50, National Stock Exchange of India (if present)
    '^KS11',     # KOSPI, Korea Exchange (if present)
    '^TWII'      # TAIEX, Taiwan Stock Exchange (if present)
])

asia_df = df[df['Index'].isin(asia_indices)].copy()

# Compute average intraday volatility per index
result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

# Prepare answer: index with highest avg volatility and its value
if not result.empty:
    top_index = result.index[0]
    top_vol = float(result.iloc[0])
    answer = {
        'top_index': top_index,
        'top_avg_intraday_volatility': top_vol,
        'all_asia_indices_ranked': result.reset_index().to_dict(orient='records')
    }
else:
    answer = {
        'error': 'No Asia indices found in data since 2020.'
    }

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7oK7cTK5jq70lYtw66qllqb1': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_YJTe5dkiz6oxRVD990YFDoRk': 'file_storage/call_YJTe5dkiz6oxRVD990YFDoRk.json'}

exec(code, env_args)
