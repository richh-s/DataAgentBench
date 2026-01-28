code = """import json
import pandas as pd

# Load data from files
tracks_file = locals()['var_functions.query_db:2']
sales_file = locals()['var_functions.query_db:6']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Basic exploration
result = {
    'tracks_rows': len(tracks_df),
    'sales_rows': len(sales_df),
    'tracks_columns': list(tracks_df.columns),
    'sales_columns': list(sales_df.columns),
    'tracks_sample': tracks_df.head(2).to_dict('records'),
    'sales_sample': sales_df.head(2).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
