code = """import json
import pandas as pd

# Read tracks data
with open(var_functions.query_db:5, 'r') as f:
    tracks_data = json.load(f)

# Read sales data
with open(var_functions.query_db:6, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Preview the data structure
print('__RESULT__:')
print(json.dumps({
    'tracks_columns': list(tracks_df.columns),
    'tracks_rows': len(tracks_df),
    'sales_columns': list(sales_df.columns),
    'sales_rows': len(sales_df),
    'tracks_sample': tracks_df[['track_id', 'title', 'artist', 'album', 'year']].head().to_dict('records'),
    'sales_sample': sales_df.head().to_dict('records')
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
