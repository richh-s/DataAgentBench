code = """import json
import pandas as pd
import numpy as np

# Load full sales data
sales_file = locals()['var_functions.query_db:5']
if isinstance(sales_file, str) and sales_file.endswith('.json'):
    with open(sales_file, 'r') as f:
        sales = json.load(f)
else:
    sales = sales_file

# Load full tracks data
tracks_file = locals()['var_functions.query_db:12']
if isinstance(tracks_file, str) and tracks_file.endswith('.json'):
    with open(tracks_file, 'r') as f:
        tracks = json.load(f)
else:
    tracks = tracks_file

df_sales = pd.DataFrame(sales)
df_tracks = pd.DataFrame(tracks)

# Convert data types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce')
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

print("__RESULT__:")
print(f"Loaded {df_tracks.shape[0]} tracks and {df_sales.shape[0]} sales records")
result = json.dumps({
    'total_sales_revenue': df_sales['revenue_usd'].sum(),
    'distinct_track_ids_in_sales': df_sales['track_id'].nunique(),
    'distinct_track_ids_in_tracks': df_tracks['track_id'].nunique()
})
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'tracks_shape': [100, 9], 'sales_shape': [58049, 6], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
