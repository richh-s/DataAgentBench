code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3992495390837066285'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-7409539752900977037'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Function to clean and extract artist/title
def clean_record(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    # Check for invalid artist
    invalid_artists = ['None', '[unknown]', 'Unknown', '']
    is_artist_invalid = artist in invalid_artists
    
    # Try to extract artist from title if artist is invalid
    if is_artist_invalid and ' - ' in title:
        parts = title.split(' - ', 1)
        # Heuristic: assume "Artist - Title"
        potential_artist = parts[0].strip()
        potential_title = parts[1].strip()
        # Update if it looks reasonable (not too long, etc? strictly strictly heuristic)
        # For now, let's just assume it is Artist - Title
        artist = potential_artist
        title = potential_title
        
    return pd.Series([title, artist])

merged[['clean_title', 'clean_artist']] = merged.apply(clean_record, axis=1)

# Further normalization for grouping
def normalize_text(text):
    if not text:
        return ""
    # Lowercase
    text = text.lower()
    # Remove special chars (keep alphanumeric and spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

merged['norm_title'] = merged['clean_title'].apply(normalize_text)
merged['norm_artist'] = merged['clean_artist'].apply(normalize_text)

# Aggregation
grouped = merged.groupby(['norm_title', 'norm_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values('revenue_usd', ascending=False)

# Get top 20 to inspect
top_20 = grouped.head(20).to_dict(orient='records')
# Also get the original titles/artists for the top entry to report nicely
# We can just pick the most frequent title/artist for the winning group
top_group = grouped.iloc[0]
norm_t = top_group['norm_title']
norm_a = top_group['norm_artist']

# Find original records for the top group to pick a nice display name
originals = merged[(merged['norm_title'] == norm_t) & (merged['norm_artist'] == norm_a)]
display_title = originals['clean_title'].mode()[0] if not originals['clean_title'].mode().empty else norm_t
display_artist = originals['clean_artist'].mode()[0] if not originals['clean_artist'].mode().empty else norm_a

print("__RESULT__:")
print(json.dumps({
    "top_20": top_20,
    "winner": {
        "title": display_title,
        "artist": display_artist,
        "revenue": top_group['revenue_usd']
    }
}))"""

env_args = {'var_function-call-3992495390837066285': 'file_storage/function-call-3992495390837066285.json', 'var_function-call-7409539752900977037': 'file_storage/function-call-7409539752900977037.json'}

exec(code, env_args)
