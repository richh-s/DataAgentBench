code = """import json
import pandas as pd

# Get file paths from local variables
sales_file_path = locals()['var_function-call-3874821068292434244']
tracks_file_path = locals()['var_function-call-13479378208221018498']

# Load sales data
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

# Load tracks data
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization function
def normalize(text):
    if text is None:
        return ""
    return str(text).strip().lower()

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

# Group by normalized title and artist
grouped = df_merged.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()

# Sort by revenue descending
grouped_sorted = grouped.sort_values(by='total_revenue', ascending=False)

# Get top record
top_record = grouped_sorted.iloc[0]

# Retrieve a representative original title and artist for the top record
mask = (df_merged['norm_title'] == top_record['norm_title']) & (df_merged['norm_artist'] == top_record['norm_artist'])
representative = df_merged.loc[mask].iloc[0]

print("__RESULT__:")
print(json.dumps({
    "song": representative['title'],
    "artist": representative['artist'],
    "revenue": top_record['total_revenue']
}))"""

env_args = {'var_function-call-3874821068292434244': 'file_storage/function-call-3874821068292434244.json', 'var_function-call-13479378208221018498': 'file_storage/function-call-13479378208221018498.json'}

exec(code, env_args)
