code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-712639782687319237'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-712639782687319000'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

# Normalize
def normalize(s):
    if s is None: return ""
    return str(s).lower().strip()

df['title_norm'] = df['title'].apply(normalize)
df['artist_norm'] = df['artist'].apply(normalize)

# Group
grouped = df.groupby(['title_norm', 'artist_norm'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-712639782687319237': 'file_storage/function-call-712639782687319237.json', 'var_function-call-712639782687319000': 'file_storage/function-call-712639782687319000.json'}

exec(code, env_args)
