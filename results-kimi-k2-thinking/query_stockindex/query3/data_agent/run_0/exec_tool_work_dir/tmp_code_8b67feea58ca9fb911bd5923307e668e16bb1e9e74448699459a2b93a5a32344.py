code = """import json
import pandas as pd

# Read the data from storage
data_file = locals()['var_functions.query_db:8']
with open(data_file, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Strip any whitespace from column names
df.columns = df.columns.str.strip()

# Convert Date to datetime with errors='coerce'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows with invalid dates or prices
df = df.dropna(subset=['Date', 'CloseUSD'])

# Check basic info
print('__RESULT__:')
print(json.dumps({
    'total_records': int(len(df)),
    'indices_count': int(df['Index'].nunique()),
    'indices': sorted(df['Index'].unique().tolist())
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'N225', 'count': '7979'}, {'Index': 'NYA', 'count': '7960'}, {'Index': 'IXIC', 'count': '7351'}, {'Index': 'GSPTSE', 'count': '6506'}, {'Index': 'HSI', 'count': '5604'}, {'Index': 'GDAXI', 'count': '5590'}, {'Index': 'SSMI', 'count': '5188'}, {'Index': 'TWII', 'count': '4385'}, {'Index': '399001.SZ', 'count': '4355'}, {'Index': '000001.SS', 'count': '4354'}, {'Index': 'N100', 'count': '4245'}, {'Index': 'NSEI', 'count': '2577'}, {'Index': 'J203.JO', 'count': '1854'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
