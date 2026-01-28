code = """import json
import pandas as pd

# Load tracks data
tracks_file = locals()['var_functions.query_db:0']
sales_file = locals()['var_functions.query_db:2']

# Read the full datasets
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

print('__RESULT__:')
print(json.dumps({
    'tracks_count': len(tracks_df),
    'sales_count': len(sales_df),
    'tracks_columns': list(tracks_df.columns),
    'sales_columns': list(sales_df.columns),
    'tracks_sample': tracks_df.head(5).to_dict('records'),
    'sales_sample': sales_df.head(5).to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
