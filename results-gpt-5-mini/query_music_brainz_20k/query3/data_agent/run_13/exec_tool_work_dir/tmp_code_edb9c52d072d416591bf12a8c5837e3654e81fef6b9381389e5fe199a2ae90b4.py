code = """import json
import pandas as pd
import unicodedata
import re

# Load data from storage-provided file paths
tracks_path = var_call_tq0V5K0COm1jqsPeOdHJsvJE
sales_path = var_call_sKEgFpD63Glg93zgMyGqqQH3

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Convert to DataFrame
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure track_id types consistent
# They are strings; keep as strings

# Convert revenue to float
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)

# Sum revenue per track_id
rev_per_track = df_sales.groupby('track_id', as_index=False)['revenue_usd'].sum()
rev_per_track.rename(columns={'revenue_usd': 'total_revenue_usd'}, inplace=True)

# Merge with tracks
df = pd.merge(df_tracks, rev_per_track, on='track_id', how='inner')

# Normalization function
import unicodedata

def normalize_text(s: str) -> str:
    if s is None:
        return ''
    # Convert to str
    s = str(s)
    if s.lower() in ('none', 'nan', 'nan', '[unknown]'):
        return ''
    # Normalize unicode
    s = unicodedata.normalize('NFKD', s)
    # Remove content in parentheses or brackets
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\[[^]]*\]", "", s)
    # Replace ampersand with 'and'
    s = s.replace('&', ' and ')
    # Lowercase
    s = s.lower()
    # Remove punctuation (keep letters, numbers, spaces)
    s = re.sub(r"[^0-9a-z\s]", "", s)
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Apply normalization on title and artist
df['norm_title'] = df['title'].apply(normalize_text)
df['norm_artist'] = df['artist'].apply(normalize_text)

# For records where artist is empty, try to extract artist from title if title contains ' - ' pattern like 'Artist - Title'
def extract_artist_from_title(title_raw, artist_raw):
    if artist_raw.strip() == '':
        if isinstance(title_raw, str) and ' - ' in title_raw:
            parts = title_raw.split(' - ', 1)
            maybe_artist = normalize_text(parts[0])
            return maybe_artist
    return artist_raw

# Update norm_artist where empty
for idx, row in df.iterrows():
    if row['norm_artist'] == '':
        df.at[idx, 'norm_artist'] = extract_artist_from_title(row['title'], row['norm_artist'])

# Group by normalized title+artist to perform entity resolution
grouped = df.groupby(['norm_title', 'norm_artist'], dropna=False).agg({
    'total_revenue_usd': 'sum',
    'title': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0],
    'artist': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0],
    'track_id': lambda x: list(x)
}).reset_index()

# Find max revenue group
max_row = grouped.loc[grouped['total_revenue_usd'].idxmax()]

result = {
    'title': max_row['title'] if pd.notna(max_row['title']) else None,
    'artist': max_row['artist'] if pd.notna(max_row['artist']) else None,
    'total_revenue_usd': round(float(max_row['total_revenue_usd']), 2),
    'member_track_ids': list(map(str, max_row['track_id']))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Gsf1FIKE3UcnvC5osMupAhzz': ['tracks'], 'var_call_YsBWxNTo0EYEIINbGlINRDfe': ['sales'], 'var_call_tq0V5K0COm1jqsPeOdHJsvJE': 'file_storage/call_tq0V5K0COm1jqsPeOdHJsvJE.json', 'var_call_sKEgFpD63Glg93zgMyGqqQH3': 'file_storage/call_sKEgFpD63Glg93zgMyGqqQH3.json'}

exec(code, env_args)
