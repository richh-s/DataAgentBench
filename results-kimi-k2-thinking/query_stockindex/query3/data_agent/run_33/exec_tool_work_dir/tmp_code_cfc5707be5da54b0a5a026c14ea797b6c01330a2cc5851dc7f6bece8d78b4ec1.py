code = """import json
import pandas as pd
from datetime import datetime

# Read the query result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Get unique indices
unique_indices = df['Index'].unique().tolist()
print('__RESULT__:')
print(json.dumps({
    'total_records': len(df),
    'unique_indices_count': len(unique_indices),
    'sample_indices': unique_indices[:20],
    'date_range': {
        'min': str(df['Date'].min()),
        'max': str(df['Date'].max())
    }
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
