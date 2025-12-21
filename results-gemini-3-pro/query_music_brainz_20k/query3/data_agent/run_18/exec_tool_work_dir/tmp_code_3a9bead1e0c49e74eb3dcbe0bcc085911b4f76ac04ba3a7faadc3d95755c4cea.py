code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-9337511221425881705'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6125831079873594295'], 'r') as f:
    tracks_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Convert types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['total_revenue'], errors='coerce').fillna(0.0)
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

# Merge
merged_df = pd.merge(sales_df, tracks_df, on='track_id', how='left')

# Entity Resolution Helper
def clean_str(s):
    if not isinstance(s, str):
        return ""
    s = s.lower()
    # Remove things in brackets/parentheses? e.g. "(live)", "(remix)"? 
    # The prompt asks for "Which song", usually aggregating versions.
    # Let's remove content in parentheses to group versions.
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\[.*?\]', '', s)
    # Remove punctuation
    s = re.sub(r'[^\w\s]', '', s)
    # Remove extra spaces
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def resolve_artist_title(row):
    title = row['title']
    artist = row['artist']
    
    # Check for None strings
    if str(artist).lower() in ['none', 'unknown', '[unknown]', '']:
        artist = ""
    
    # If artist is empty, check if title contains " - "
    if artist == "" and title and " - " in title:
        parts = title.split(" - ", 1)
        if len(parts) == 2:
            pot_artist = parts[0].strip()
            pot_title = parts[1].strip()
            # Heuristic: if pot_artist looks like a name (not too long?)
            artist = pot_artist
            title = pot_title

    clean_t = clean_str(title)
    clean_a = clean_str(artist)
    
    # Handle "the " prefix in artist
    if clean_a.startswith("the "):
        clean_a = clean_a[4:]
        
    return pd.Series([clean_t, clean_a])

merged_df[['clean_title', 'clean_artist']] = merged_df.apply(resolve_artist_title, axis=1)

# Handle typo "En dless Love" -> "endless love"
# Maybe remove spaces for grouping key?
# "endless love" -> "endlesslove"
# "hweels of fire" -> "hweelsoffire" (still won't match "wheels of fire")
# Let's try to group by (clean_title, clean_artist) first.
# If I remove spaces in clean_title, "en dless love" becomes "endlesslove".
# "Endless Love" becomes "endlesslove". Match!
merged_df['key_title'] = merged_df['clean_title'].str.replace(' ', '')
merged_df['key_artist'] = merged_df['clean_artist'].str.replace(' ', '')

# Group by keys
grouped = merged_df.groupby(['key_title', 'key_artist'])['revenue_usd'].sum().reset_index()

# Sort
top_songs = grouped.sort_values('revenue_usd', ascending=False).head(10)

# Get original names for the top result
# We need to find one representative from merged_df for the top key
top_key_title = top_songs.iloc[0]['key_title']
top_key_artist = top_songs.iloc[0]['key_artist']
top_revenue = top_songs.iloc[0]['revenue_usd']

rep_row = merged_df[(merged_df['key_title'] == top_key_title) & (merged_df['key_artist'] == top_key_artist)].iloc[0]

result = {
    "clean_title": rep_row['clean_title'],
    "clean_artist": rep_row['clean_artist'],
    "original_title": rep_row['title'],
    "original_artist": rep_row['artist'],
    "total_revenue": top_revenue,
    "top_5": top_songs.to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9337511221425881705': 'file_storage/function-call-9337511221425881705.json', 'var_function-call-6125831079873594295': 'file_storage/function-call-6125831079873594295.json'}

exec(code, env_args)
