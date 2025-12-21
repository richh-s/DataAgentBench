code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-3835480464136415484'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6188791716186405650'], 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Helper for normalization
def normalize_text(text):
    if not text:
        return ""
    # Lowercase
    text = str(text).lower()
    # Remove special chars (keep alphanumeric and spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Collapse spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_track_info(row):
    title = row['title']
    artist = row['artist']
    
    # Check for invalid artist
    invalid_artists = ['none', 'unknown', '[unknown]', '']
    normalized_artist_check = str(artist).lower().strip()
    
    artist_missing = normalized_artist_check in invalid_artists
    
    # Try to extract artist from title if missing
    if artist_missing and title and '-' in title:
        parts = title.split('-', 1)
        if len(parts) == 2:
            possible_artist = parts[0].strip()
            possible_title = parts[1].strip()
            # simple heuristic: if artist part is not too long or looks like real text
            if len(possible_artist) < 50: 
                artist = possible_artist
                title = possible_title
    
    norm_title = normalize_text(title)
    norm_artist = normalize_text(artist)
    
    # Fallback if artist is still missing/invalid, just use title
    if norm_artist in ['none', 'unknown', '']:
        norm_artist = "unknown"
        
    return pd.Series([norm_title, norm_artist])

# Apply cleaning
df_tracks[['clean_title', 'clean_artist']] = df_tracks.apply(clean_track_info, axis=1)

# Handle "En dless Love" type typos? 
# Maybe remove spaces entirely for matching?
# Let's create a 'match_key'
df_tracks['match_key'] = df_tracks['clean_artist'].str.replace(' ', '') + "|" + df_tracks['clean_title'].str.replace(' ', '')

# Merge sales with tracks
merged = df_sales.merge(df_tracks, on='track_id', how='left')

# Group by match_key and sum revenue
grouped = merged.groupby('match_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Get top result info
top_key = grouped.iloc[0]['match_key']
top_revenue = grouped.iloc[0]['total_revenue']

# Find one original entry for this key to get readable Title/Artist
original_entry = merged[merged['match_key'] == top_key].iloc[0]
readable_title = original_entry['title']
readable_artist = original_entry['artist']

print("__RESULT__:")
print(json.dumps({
    "top_song_key": top_key,
    "revenue": top_revenue,
    "sample_title": readable_title,
    "sample_artist": readable_artist,
    "top_5": grouped.head(5).to_dict(orient='records')
}))"""

env_args = {'var_function-call-3835480464136415484': 'file_storage/function-call-3835480464136415484.json', 'var_function-call-6188791716186405650': 'file_storage/function-call-6188791716186405650.json'}

exec(code, env_args)
