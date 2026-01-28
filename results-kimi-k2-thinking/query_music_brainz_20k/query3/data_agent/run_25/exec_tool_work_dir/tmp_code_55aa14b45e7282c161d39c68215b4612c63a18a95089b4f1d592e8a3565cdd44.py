code = """import json
import pandas as pd

# Load the data from file paths
tracks_path = 'var_functions.query_db_2'
sales_path = 'var_functions.query_db_6'

with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)

with open(sales_path, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Basic info
print('Tracks shape:', tracks_df.shape)
print('Sales shape:', sales_df.shape)

print('\nTracks columns:', list(tracks_df.columns))
print('Sales columns:', list(sales_df.columns))

# Show first few rows
print('\nFirst 3 tracks:')
for i, row in tracks_df.head(3).iterrows():
    print(f"ID: {row['track_id']}, Title: {row['title']}, Artist: {row['artist']}")

print('\nFirst 3 sales:')
for i, row in sales_df.head(3).iterrows():
    print(f"Sale ID: {row['sale_id']}, Track ID: {row['track_id']}, Revenue: ${row['revenue_usd']}")

result = 'Data loaded successfully'
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
