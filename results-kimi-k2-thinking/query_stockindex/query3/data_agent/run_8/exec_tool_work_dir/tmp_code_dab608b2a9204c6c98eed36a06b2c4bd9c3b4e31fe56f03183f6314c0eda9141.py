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

# Convert Date to datetime and other fields to numeric - handle errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
for col in ['Close', 'CloseUSD']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Filter from 2000-01-01 onwards
df_filtered = df[df['Date'] >= '2000-01-01'].copy()

# Get unique indices
indices = sorted(df_filtered['Index'].unique().tolist())

# Group by Index and calculate metrics
results = []

# Index to exchange/country mapping (based on known symbols)
index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GDAXI': 'Germany',
    'N100': 'Netherlands',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa',
    'NSEI': 'India',
    'GSPTSE': 'Canada'
}

# Check data availability
print('__RESULT__:')
print(json.dumps({
    'status': 'Data loaded successfully',
    'total_records': int(len(df_filtered)),
    'num_indices': int(len(indices)),
    'indices': indices,
    'date_range': {
        'start': str(df_filtered['Date'].min()),
        'end': str(df_filtered['Date'].max())
    }
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
