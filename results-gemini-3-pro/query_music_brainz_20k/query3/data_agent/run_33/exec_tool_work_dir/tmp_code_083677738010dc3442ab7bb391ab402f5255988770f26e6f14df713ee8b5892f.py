code = """import json
import re
import pandas as pd
import unicodedata

# Load data
with open(locals()['var_function-call-3835480464136415484'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6188791716186405650'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

def normalize_text(text):
    if not text:
        return ""
    # Convert to string and lowercase
    text = str(text).lower()
    # Normalize unicode (e.g. accents)
    text = unicodedata.normalize('NFKC', text)
    # Remove punctuation (keep letters, numbers, spaces) from any language
    # Instead of regex [^a-z], lets just remove specific punctuation or keep it simple
    # We want to remove things like '.', ',', '-', '(', ')'
    # Using regex with \w matches unicode alphanumeric
    text = re.sub(r'[^\w\s]', '', text)
    # Collapse spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_track_info(row):
    title = row['title']
    artist = row['artist']
    
    invalid_artists = ['none', 'unknown', '[unknown]', '', 'null']
    normalized_artist_check = str(artist).lower().strip()
    
    artist_missing = normalized_artist_check in invalid_artists
    
    # Try to extract artist from title if missing
    if artist_missing and title and ('-' in title):
        parts = title.split('-', 1)
        if len(parts) == 2:
            # Heuristic: usually Artist - Title
            p1 = parts[0].strip()
            p2 = parts[1].strip()
            # If p1 is short enough, assume it's artist
            if len(p1) > 0 and len(p1) < 50:
                artist = p1
                title = p2

    norm_title = normalize_text(title)
    norm_artist = normalize_text(artist)
    
    if norm_artist in ['none', 'unknown', '']:
        norm_artist = "unknown"
        
    return pd.Series([norm_title, norm_artist])

df_tracks[['clean_title', 'clean_artist']] = df_tracks.apply(clean_track_info, axis=1)

# Group key: artist + title
# Use a separator that won't likely be in the text
df_tracks['match_key'] = df_tracks['clean_artist'] + "|||" + df_tracks['clean_title']

merged = df_sales.merge(df_tracks, on='track_id', how='left')

# Check if 'unknown' artist bucket is still huge
# If 'clean_artist' is unknown, we group by title only?
# No, different songs can have same title (e.g. "Intro", "Love").
# If artist is unknown, we rely on title. If title is also generic, we have a problem.
# But "unknown|||intro" might still group disparate tracks.
# Let's hope the "Artist - Title" split fixed most "None" artists.

grouped = merged.groupby('match_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_rows = grouped.head(10)
results = []
for idx, row in top_rows.iterrows():
    key = row['match_key']
    revenue = row['total_revenue']
    # Get original metadata for one sample
    sample = merged[merged['match_key'] == key].iloc[0]
    results.append({
        "key": key,
        "revenue": revenue,
        "title": sample['title'],
        "artist": sample['artist']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3835480464136415484': 'file_storage/function-call-3835480464136415484.json', 'var_function-call-6188791716186405650': 'file_storage/function-call-6188791716186405650.json', 'var_function-call-8554056373783831330': {'top_song_key': 'unknown|', 'revenue': 207955.01, 'sample_title': '妥協', 'sample_artist': '蔡依林', 'top_5': [{'match_key': 'unknown|', 'total_revenue': 207955.01}, {'match_key': 'unknown|none', 'total_revenue': 17150.55}, {'match_key': '004|', 'total_revenue': 7249.700000000001}, {'match_key': '003|', 'total_revenue': 7090.13}, {'match_key': 'richmatteson|groovey', 'total_revenue': 5417.34}]}}

exec(code, env_args)
