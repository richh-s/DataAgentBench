code = """import pandas as pd
import json
import re

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

# Merge
# Note: track_id in sales is likely string or int, need to match types.
# In preview, sales track_id is "1", tracks track_id is "1". Both strings.
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

# Entity Resolution Helper
def clean_str(s):
    if s is None:
        return ""
    s = str(s).lower().strip()
    return s

def resolve_artist_title(row):
    title = row['title']
    artist = row['artist']
    
    # Normalize nulls
    if artist is None or artist.lower() in ['none', '[unknown]', '']:
        artist = ""
    
    if title is None:
        title = ""
        
    # If artist is missing, try to extract from title
    if artist == "" and " - " in title:
        parts = title.split(" - ", 1)
        potential_artist = parts[0].strip()
        potential_title = parts[1].strip()
        # Heuristic: if title looks like "Artist - Song", use it.
        # But sometimes it might be just a title with a hyphen.
        # Given the dataset examples (source_id=2), this seems a valid pattern.
        artist = potential_artist
        title = potential_title
        
    return clean_str(artist), clean_str(title)

# Apply resolution
df_merged['clean_artist'], df_merged['clean_title'] = zip(*df_merged.apply(resolve_artist_title, axis=1))

# Group by clean artist and title
# We might want to keep the original Title/Artist for display from the most popular track variant
group_cols = ['clean_artist', 'clean_title']
df_grouped = df_merged.groupby(group_cols)['revenue_usd'].sum().reset_index()

# Find max
top_song = df_grouped.sort_values('revenue_usd', ascending=False).iloc[0]

# Retrieve a displayable name (e.g. from the first matching original row)
mask = (df_merged['clean_artist'] == top_song['clean_artist']) & (df_merged['clean_title'] == top_song['clean_title'])
sample_row = df_merged[mask].iloc[0]

result = {
    "clean_artist": top_song['clean_artist'],
    "clean_title": top_song['clean_title'],
    "revenue": top_song['revenue_usd'],
    "sample_title": sample_row['title'],
    "sample_artist": sample_row['artist']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11167553081244031459': 'file_storage/function-call-11167553081244031459.json', 'var_function-call-13338430571201753838': 'file_storage/function-call-13338430571201753838.json'}

exec(code, env_args)
