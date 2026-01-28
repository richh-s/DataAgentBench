code = """import json
import pandas as pd

sales_file = locals()['var_functions.query_db:5']
tracks_file = locals()['var_functions.query_db:0']

if isinstance(sales_file, str) and sales_file.endswith('.json'):
    with open(sales_file, 'r') as f:
        sales = json.load(f)
else:
    sales = sales_file

if isinstance(tracks_file, str) and tracks_file.endswith('.json'):
    with open(tracks_file, 'r') as f:
        tracks = json.load(f)
else:
    tracks = tracks_file

df_sales = pd.DataFrame(sales)
df_tracks = pd.DataFrame(tracks)

print("__RESULT__:")
print(f"Tracks: {df_tracks.shape}, Sales: {df_sales.shape}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
