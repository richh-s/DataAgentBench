code = """import json
import pandas as pd
import re

# Load sales data
sales_path = locals()['var_function-call-571140759892803866']
with open(sales_path, 'r') as f:
    sales_data = json.load(f)
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Load tracks data
tracks_path = locals()['var_function-call-7555422285547670374']
with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)
df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Basic cleaning for inspection
df['title_clean'] = df['title'].fillna('').astype(str)
df['artist_clean'] = df['artist'].fillna('').astype(str)

# Sort by revenue to see top contenders
top_tracks = df.sort_values('total_revenue', ascending=False).head(50)

print("__RESULT__:")
print(top_tracks.to_json(orient='records'))"""

env_args = {'var_function-call-571140759892803866': 'file_storage/function-call-571140759892803866.json', 'var_function-call-7555422285547670374': 'file_storage/function-call-7555422285547670374.json'}

exec(code, env_args)
