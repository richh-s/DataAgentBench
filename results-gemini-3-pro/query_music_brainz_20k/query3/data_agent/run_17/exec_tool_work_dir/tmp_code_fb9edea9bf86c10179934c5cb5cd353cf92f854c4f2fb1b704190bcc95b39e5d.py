code = """import pandas as pd
import json

# Access file paths from locals()
sales_file_path = locals()['var_function-call-17358517250979617377']
tracks_file_path = locals()['var_function-call-17358517250979616604']

# Load sales aggregation
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

# Load tracks
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Basic cleaning function
def clean_string(s):
    if pd.isna(s): return ""
    return str(s).lower().strip()

df['clean_title'] = df['title'].apply(clean_string)
df['clean_artist'] = df['artist'].apply(clean_string)

# Group by exact title/artist first
grouped = df.groupby(['clean_title', 'clean_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print('__RESULT__:')
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-17358517250979617377': 'file_storage/function-call-17358517250979617377.json', 'var_function-call-17358517250979616604': 'file_storage/function-call-17358517250979616604.json'}

exec(code, env_args)
