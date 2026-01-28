code = """import json
import pandas as pd
from collections import defaultdict

# Read the full data from the file
file_path = locals()['var_functions.query_db:8'] if 'var_functions.query_db:8' in locals() else None
if file_path and isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    # If it's not a file path, assume it's the data directly
    data = locals().get('var_functions.query_db:8', [])

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime and Close to float
df['Date'] = pd.to_datetime(df['Date'])
df['Close'] = pd.to_numeric(df['Close'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter from 2000-01-01 onwards
df_filtered = df[df['Date'] >= '2000-01-01'].copy()

# Group by index and prepare for dollar-cost averaging analysis
indices = df_filtered['Index'].unique()
print('__RESULT__:')
print(json.dumps({
    'status': 'Data loaded successfully',
    'total_records': len(df_filtered),
    'num_indices': len(indices),
    'indices': sorted(list(indices))
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
