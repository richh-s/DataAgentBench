code = """import json, pandas as pd
from datetime import datetime

# Load full trade data
data_path = var_call_uN9ktB0YqzJfT8wtDj1KWI7B
with open(data_path, 'r') as f:
    trades = json.load(f)

df = pd.DataFrame(trades)

# Ensure numeric types
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse date to year
def get_year(s):
    try:
        return pd.to_datetime(s, errors='coerce').year
    except Exception:
        return None

df['Year'] = pd.to_datetime(df['Date'], errors='coerce').dt.year

# Filter since 2020
df = df[df['Year'] >= 2020]

# Compute intraday volatility
df = df[df['Open'] > 0]
df['intraday_vol'] = (df['High'] - df['Low']) / df['Open']

# Map indices to regions (Asia vs others) using known major indices
asia_indices = set(['N225','HSI','000001.SS','399001.SZ','^BSESN','^NSEI','KS11','TWII'])

asia_df = df[df['Index'].isin(asia_indices)].copy()

# Compute average intraday volatility per index
result = asia_df.groupby('Index')['intraday_vol'].mean().sort_values(ascending=False)

result_dict = result.to_dict()

# Identify highest
if len(result_dict) > 0:
    highest_index = max(result_dict, key=result_dict.get)
    highest_value = result_dict[highest_index]
    answer = {
        'highest_index': highest_index,
        'highest_avg_intraday_volatility': highest_value,
        'all_asia_index_avg_vol': result_dict
    }
else:
    answer = {
        'error': 'No Asia indices found in data since 2020'
    }

out = json.dumps(answer)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_sIrGpvf8u0iEHBBSeTkzVOhs': ['index_info'], 'var_call_hGsXOh52i03wmsoRJ0tDDNs6': ['index_trade'], 'var_call_Gpag6vSOGEVVzRyHo9gvuXzc': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_uN9ktB0YqzJfT8wtDj1KWI7B': 'file_storage/call_uN9ktB0YqzJfT8wtDj1KWI7B.json'}

exec(code, env_args)
