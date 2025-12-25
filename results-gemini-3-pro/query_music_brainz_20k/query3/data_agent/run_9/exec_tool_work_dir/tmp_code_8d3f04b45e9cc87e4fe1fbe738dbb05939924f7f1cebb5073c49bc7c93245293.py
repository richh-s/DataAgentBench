code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-2511588746331634384'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-1045009178916472453'], 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Ensure numeric types
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution Function
def resolve_entity(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    # Handle missing or placeholder artists
    if artist.lower() in ['none', 'null', '[unknown]', '']:
        artist = None
    
    # Try to extract artist from title if artist is missing
    if artist is None and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            artist = parts[0].strip()
            title = parts[1].strip()
    
    # Fallback if still None
    if artist is None:
        artist = "Unknown Artist"
        
    return pd.Series([title, artist])

# Apply resolution
df[['clean_title', 'clean_artist']] = df.apply(resolve_entity, axis=1)

# Normalize for grouping
df['norm_title'] = df['clean_title'].str.lower().str.strip()
df['norm_artist'] = df['clean_artist'].str.lower().str.strip()

# Aggregate revenue
grouped = df.groupby(['norm_artist', 'norm_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Get top result details
top_record = grouped.iloc[0]
top_revenue = top_record['total_revenue']
top_artist = top_record['norm_artist']
top_title = top_record['norm_title']

# Retrieve original casing from one of the records
original_record = df[(df['norm_artist'] == top_artist) & (df['norm_title'] == top_title)].iloc[0]
final_title = original_record['clean_title']
final_artist = original_record['clean_artist']

result = {
    "title": final_title,
    "artist": final_artist,
    "total_revenue": top_revenue
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2511588746331634384': 'file_storage/function-call-2511588746331634384.json', 'var_function-call-1045009178916472453': 'file_storage/function-call-1045009178916472453.json'}

exec(code, env_args)
