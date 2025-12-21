code = """import json
import pandas as pd

# Load sales data
with open(locals()['var_function-call-13586711412280274277'], 'r') as f:
    sales_data = json.load(f)
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Load tracks data
with open(locals()['var_function-call-15404616828467795232'], 'r') as f:
    tracks_data = json.load(f)
df_tracks = pd.DataFrame(tracks_data)

# Merge
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Sort by revenue to see the top ones
df_top = df_merged.sort_values(by='total_revenue', ascending=False).head(30)

print("__RESULT__:")
print(df_top[['track_id', 'total_revenue', 'title', 'artist', 'album']].to_json(orient='records'))"""

env_args = {'var_function-call-13586711412280274277': 'file_storage/function-call-13586711412280274277.json', 'var_function-call-15404616828467795232': 'file_storage/function-call-15404616828467795232.json'}

exec(code, env_args)
