code = """import json
import re
import pandas as pd

# Load the large JSON results
with open(locals()['var_function-call-14958088041472959322'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-14958088041472958953'], 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Ensure numeric revenue
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Merge
# Note: track_id might be int or str in source, let's normalize to str
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization function
def normalize_string(s):
    if not isinstance(s, str):
        return ""
    # Lowercase, replace special chars with space, strip
    s = s.lower()
    # Remove things in brackets like (acoustic), [live], etc? 
    # Maybe too aggressive, "Try (acoustic)" is different from "Try"?
    # User asks for "Which song", usually implies the composition. 
    # "Bohemian Rhapsody" and "Bohemian Rhapsody (Remastered)" are the same song.
    # "Try (acoustic)" vs "Try" might be debatable, but usually same song revenue should be combined.
    # Let's remove text inside parentheses/brackets for grouping?
    s = re.sub(r'[\(\[\{].*?[\)\]\}]', '', s) 
    # Remove non-alphanumeric
    s = re.sub(r'[^a-z0-9]', ' ', s)
    # Collapse spaces
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def get_entity_key(row):
    title = row['title']
    artist = row['artist']
    
    # Handle missing artist or "None" string
    if not isinstance(artist, str) or artist.lower() in ['none', 'unknown', '[unknown]']:
        artist = ""
        # Try to extract from title if " - " exists
        if isinstance(title, str) and " - " in title:
            parts = title.split(" - ", 1)
            # This is heuristic. "Artist - Title" or "Title - Artist"? 
            # Track 1: "Daniel Balavoine - L'enfant..." (Artist - Title)
            # But usually it's hard to guess. 
            # Let's just use the whole title if artist is missing.
            pass
    
    norm_title = normalize_string(title)
    norm_artist = normalize_string(artist)
    
    return (norm_title, norm_artist)

# Apply normalization
# We only care about rows with revenue, which are in df (left join from sales)
df['entity_key'] = df.apply(get_entity_key, axis=1)

# Group by entity_key and sum revenue
grouped = df.groupby('entity_key')['total_revenue'].sum().reset_index()

# Sort
top_songs = grouped.sort_values(by='total_revenue', ascending=False).head(10)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-14958088041472959322': 'file_storage/function-call-14958088041472959322.json', 'var_function-call-14958088041472958953': 'file_storage/function-call-14958088041472958953.json'}

exec(code, env_args)
