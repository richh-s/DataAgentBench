code = """import json
import pandas as pd

# Read the full tracks data from the file
with open('/tmp/tmps8g3u4p8.json', 'r') as f:
    tracks_data = json.load(f)

# Read the full sales data from the file  
with open('/tmp/tmp0m8hoh8m.json', 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Show basic info about the data
print('__RESULT__:')
print(json.dumps({
    "tracks_count": len(tracks_df),
    "sales_count": len(sales_df),
    "sample_tracks": tracks_df.head(3).to_dict('records'),
    "sample_sales": sales_df.head(3).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['sales'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
