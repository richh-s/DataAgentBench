code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-1289187297188193352']) as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-912133559032777454']) as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
# Convert revenue to float
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Normalization function
def normalize(s):
    if not isinstance(s, str):
        return ""
    # Normalize unicode characters to ascii if needed? 
    # For now, just keep alphanumeric including unicode letters if any, or strip.
    # The data seems to have unicode (e.g. í). 
    # Let's just remove anything that isn't a letter or number.
    # Using \w includes [a-zA-Z0-9_] and unicode alphanumerics in Python 3 re.
    return "".join(c for c in s.lower() if c.isalnum())

def get_key(row):
    title = row.get('title', '')
    artist = row.get('artist', '')
    # Handle None/NaN
    if pd.isna(title): title = ""
    if pd.isna(artist): artist = ""
    title = str(title)
    artist = str(artist)
    
    t_lower = title.lower()
    a_lower = artist.lower()
    
    # Check for invalid artist
    invalid_artists = ['none', '[unknown]', 'unknown', '', 'null', 'nan']
    
    eff_artist = a_lower
    eff_title = t_lower
    
    if a_lower in invalid_artists:
        # Try to extract from title
        if ' - ' in title: 
            parts = title.split(' - ', 1)
            eff_artist = parts[0].lower()
            eff_title = parts[1].lower()
        else:
            eff_artist = ""
            eff_title = t_lower
            
    return normalize(eff_artist) + normalize(eff_title)

df_tracks['resolution_key'] = df_tracks.apply(get_key, axis=1)

# Merge
df_merged = df_sales.merge(df_tracks[['track_id', 'resolution_key', 'title', 'artist']], on='track_id', how='left')

# Group
grouped = df_merged.groupby('resolution_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_5 = grouped.head(5).to_dict(orient='records')

# Get representative info for top 5
final_results = []
for item in top_5:
    key = item['resolution_key']
    rev = item['total_revenue']
    # Get all tracks with this key
    matches = df_merged[df_merged['resolution_key'] == key]
    # Pick the one with the most complete metadata, or just the first
    rep = matches.iloc[0]
    final_results.append({
        "key": key,
        "revenue": rev,
        "title": rep['title'],
        "artist": rep['artist']
    })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-1289187297188193352': 'file_storage/function-call-1289187297188193352.json', 'var_function-call-912133559032777454': 'file_storage/function-call-912133559032777454.json'}

exec(code, env_args)
