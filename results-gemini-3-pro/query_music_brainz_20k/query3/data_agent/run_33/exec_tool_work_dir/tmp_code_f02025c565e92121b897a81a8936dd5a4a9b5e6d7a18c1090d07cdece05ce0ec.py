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
    text = str(text).lower()
    text = unicodedata.normalize('NFKC', text)
    # Remove all characters that are NOT alphanumeric or whitespace
    # This keeps unicode letters/numbers (Chinese, etc)
    text = re.sub(r'[^\w\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_track_info(row):
    title = row['title']
    artist = row['artist']
    
    invalid_artists = ['none', 'unknown', '[unknown]', '', 'null']
    normalized_artist_check = str(artist).lower().strip()
    
    artist_missing = normalized_artist_check in invalid_artists
    
    if artist_missing and title and ('-' in title):
        parts = title.split('-', 1)
        if len(parts) == 2:
            p1 = parts[0].strip()
            p2 = parts[1].strip()
            if len(p1) > 0 and len(p1) < 50:
                artist = p1
                title = p2

    norm_title = normalize_text(title)
    norm_artist = normalize_text(artist)
    
    if norm_artist in ['none', 'unknown', '']:
        norm_artist = "unknown"
        
    return pd.Series([norm_title, norm_artist])

df_tracks[['clean_title', 'clean_artist']] = df_tracks.apply(clean_track_info, axis=1)

df_tracks['match_key'] = df_tracks['clean_artist'] + "|||" + df_tracks['clean_title']

merged = df_sales.merge(df_tracks, on='track_id', how='left')
grouped = merged.groupby('match_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Filter garbage
def is_valid_key(key):
    parts = key.split('|||')
    if len(parts) != 2: return False
    art, tit = parts
    if art == 'unknown' and tit == '': return False
    if art == 'unknown' and tit == 'none': return False
    if tit.isdigit(): return False # Title is just numbers
    # Check if title has no letters
    if not any(c.isalpha() for c in tit):
        # Allow if it's unicode characters that act like letters
        # but normalize_text keeps \w, so digits are kept. 
        # "004" is kept.
        # Let's reject if title is only digits/spaces
        if re.match(r'^[\d\s]+$', tit):
            return False
    return True

grouped['is_valid'] = grouped['match_key'].apply(is_valid_key)
valid_grouped = grouped[grouped['is_valid']].head(20)

results = []
for idx, row in valid_grouped.iterrows():
    key = row['match_key']
    revenue = row['total_revenue']
    sample = merged[merged['match_key'] == key].iloc[0]
    results.append({
        "key": key,
        "revenue": revenue,
        "title": sample['title'],
        "artist": sample['artist']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3835480464136415484': 'file_storage/function-call-3835480464136415484.json', 'var_function-call-6188791716186405650': 'file_storage/function-call-6188791716186405650.json', 'var_function-call-8554056373783831330': {'top_song_key': 'unknown|', 'revenue': 207955.01, 'sample_title': '妥協', 'sample_artist': '蔡依林', 'top_5': [{'match_key': 'unknown|', 'total_revenue': 207955.01}, {'match_key': 'unknown|none', 'total_revenue': 17150.55}, {'match_key': '004|', 'total_revenue': 7249.700000000001}, {'match_key': '003|', 'total_revenue': 7090.13}, {'match_key': 'richmatteson|groovey', 'total_revenue': 5417.34}]}, 'var_function-call-16098740597880241896': [{'key': 'unknown|||none', 'revenue': 14647.52, 'title': 'None', 'artist': 'None'}, {'key': '004|||', 'revenue': 7249.700000000001, 'title': '004- ', 'artist': ' '}, {'key': '003|||', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'key': '005|||', 'revenue': 5222.0, 'title': '005-', 'artist': 'None'}, {'key': '009|||', 'revenue': 5045.7, 'title': '009-   ', 'artist': 'None'}, {'key': '010|||', 'revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue': 4132.27, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'key': '002|||', 'revenue': 4119.89, 'title': '002-', 'artist': ' '}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}]}

exec(code, env_args)
