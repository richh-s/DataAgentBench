code = """import json
import pandas as pd

# Load data (re-loading to ensure context)
with open(locals()['var_function-call-2511588746331634384'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-1045009178916472453'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def resolve_entity(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    if artist.lower() in ['none', 'null', '[unknown]', '']:
        artist = None
    
    # Heuristic: split by " - " if artist is missing
    if artist is None and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            artist = parts[0].strip()
            title = parts[1].strip()
            
    if artist is None:
        artist = "Unknown Artist"
        
    return pd.Series([title, artist])

df[['clean_title', 'clean_artist']] = df.apply(resolve_entity, axis=1)

df['norm_title'] = df['clean_title'].str.lower().str.strip()
df['norm_artist'] = df['clean_artist'].str.lower().str.strip()

# Filter out "none" titles if they seem like placeholders
# But keep them in the list to see
grouped = df.groupby(['norm_artist', 'norm_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-2511588746331634384': 'file_storage/function-call-2511588746331634384.json', 'var_function-call-1045009178916472453': 'file_storage/function-call-1045009178916472453.json', 'var_function-call-4121161695158870877': {'title': 'None', 'artist': 'Unknown Artist', 'total_revenue': 14647.52}}

exec(code, env_args)
