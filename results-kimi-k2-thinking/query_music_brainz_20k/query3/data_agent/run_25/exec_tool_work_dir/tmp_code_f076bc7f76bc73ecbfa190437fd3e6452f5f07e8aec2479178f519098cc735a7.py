code = """import json
import pandas as pd

# Load tracks data
tracks_file = var_functions.query_db_2
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

# Load sales data  
sales_file = var_functions.query_db_6
with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

print('Tracks shape:', tracks_df.shape)
print('Sales shape:', sales_df.shape)
print('\nTracks columns:', tracks_df.columns.tolist())
print('Sales columns:', sales_df.columns.tolist())

# Display sample data
print('\nTracks sample:')
print(tracks_df.head(3))
print('\nSales sample:')
print(sales_df.head(3))

result = {'tracks_shape': tracks_df.shape, 'sales_shape': sales_df.shape}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
