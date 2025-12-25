code = """import pandas as pd
import json

# Load sales data
sales_path = locals()['var_function-call-11167553081244031459']
with open(sales_path, 'r') as f:
    sales_data = json.load(f)
df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])

# Load tracks data
tracks_path = locals()['var_function-call-13338430571201753838']
with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)
df_tracks = pd.DataFrame(tracks_data)

df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

def clean_str(s):
    if s is None:
        return ""
    s = str(s).strip()
    if s.lower() == 'none':
        return ""
    return s.lower()

def resolve_artist_title(row):
    title = row['title']
    artist = row['artist']
    
    # Normalize
    artist_clean = clean_str(artist)
    title_clean = clean_str(title)
    
    # If artist is missing, try to extract from title
    # Pattern: "Artist - Title"
    if artist_clean == "" and " - " in title_clean:
        parts = title_clean.split(" - ", 1)
        artist_clean = parts[0].strip()
        title_clean = parts[1].strip()
        
    return artist_clean, title_clean

df_merged['clean_artist'], df_merged['clean_title'] = zip(*df_merged.apply(resolve_artist_title, axis=1))

# Group
df_grouped = df_merged.groupby(['clean_artist', 'clean_title'])['revenue_usd'].sum().reset_index()

# Sort
top_songs = df_grouped.sort_values('revenue_usd', ascending=False).head(20)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-11167553081244031459': 'file_storage/function-call-11167553081244031459.json', 'var_function-call-13338430571201753838': 'file_storage/function-call-13338430571201753838.json', 'var_function-call-8108861843005645843': {'clean_artist': '', 'clean_title': 'none', 'revenue': 14647.52, 'sample_title': 'None', 'sample_artist': 'None'}}

exec(code, env_args)
