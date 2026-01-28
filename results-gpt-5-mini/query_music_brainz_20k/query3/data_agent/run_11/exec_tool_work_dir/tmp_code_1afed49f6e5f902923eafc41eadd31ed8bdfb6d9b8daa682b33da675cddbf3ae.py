code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage paths
with open(var_call_Mln8s1FaGhHeRlX9sKrlAgCK, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_ko0lAPvxRRQt5rqv6sTm9EiB, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Clean columns and types
for col in ['track_id']:
    if col in df_tracks.columns:
        df_tracks[col] = df_tracks[col].astype(str)
if 'track_id' in df_sales.columns:
    df_sales['track_id'] = df_sales['track_id'].astype(str)

# Convert revenue to float
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Aggregate revenue by track_id
rev_by_track = df_sales.groupby('track_id', dropna=False)['revenue_usd'].sum().reset_index()

# Merge with tracks
df = pd.merge(rev_by_track, df_tracks, on='track_id', how='left')

# Helper functions for normalization

def remove_parentheses(txt):
    return re.sub(r"\([^)]*\)", "", txt) if isinstance(txt, str) else txt

def normalize_text(txt):
    if pd.isna(txt):
        return ''
    if not isinstance(txt, str):
        txt = str(txt)
    txt = txt.strip()
    if txt.lower() in ['none', 'nan', '']:
        return ''
    # remove parenthetical content
    txt = remove_parentheses(txt)
    # try to split if pattern 'Artist - Title' in title and artist missing
    txt = txt
    # normalize unicode
    txt = unicodedata.normalize('NFKD', txt)
    txt = ''.join([c for c in txt if not unicodedata.combining(c)])
    # lowercase
    txt = txt.lower()
    # remove punctuation except spaces
    txt = re.sub(r"[^0-9a-z ]+", ' ', txt)
    # collapse whitespace
    txt = re.sub(r"\s+", ' ', txt).strip()
    return txt

# If artist missing, try to extract from title if it contains ' - '
def extract_artist_title(row):
    title = row.get('title') if pd.notna(row.get('title')) else ''
    artist = row.get('artist') if pd.notna(row.get('artist')) else ''
    if isinstance(artist, str) and artist.strip().lower() not in ['', 'none']:
        return title, artist
    # try split
    if isinstance(title, str) and ' - ' in title:
        parts = title.split(' - ', 1)
        # Heuristic: if left part has letters and is shorter than right, treat as artist
        left, right = parts[0].strip(), parts[1].strip()
        if len(left) <= 50:
            return right, left
    return title, artist

# Build normalized keys
entities = []
for _, r in df.iterrows():
    orig_title, orig_artist = extract_artist_title(r)
    norm_title = normalize_text(orig_title)
    norm_artist = normalize_text(orig_artist)
    # fallback to album if artist still missing
    if norm_artist == '':
        norm_artist = normalize_text(r.get('album',''))
    key = norm_title + '||' + norm_artist
    entities.append(key)

df['entity_key'] = entities

# Group by entity_key to aggregate revenue
agg = df.groupby('entity_key').agg({
    'revenue_usd': 'sum',
    'title': lambda x: next((t for t in x if isinstance(t, str) and t.strip().lower() not in ['none','']), None),
    'artist': lambda x: next((a for a in x if isinstance(a, str) and a.strip().lower() not in ['none','']), None),
    'track_id': lambda x: list(x.dropna().astype(str).unique())
}).reset_index()

# Clean up returned title/artist by applying extract_artist_title on representative row if needed
clean_titles = []
clean_artists = []
for _, row in agg.iterrows():
    # If artist is missing, try to parse from title string
    t = row['title']
    a = row['artist']
    if (not isinstance(a, str) or a.strip().lower() in ['', 'none']) and isinstance(t, str) and ' - ' in t:
        parsed_t, parsed_a = extract_artist_title({'title': t, 'artist': a})
        t, a = parsed_t, parsed_a
    clean_titles.append(t if pd.notna(t) else '')
    clean_artists.append(a if pd.notna(a) else '')

agg['resolved_title'] = clean_titles
agg['resolved_artist'] = clean_artists

# Find max revenue entity
agg['revenue_usd'] = agg['revenue_usd'].astype(float)
max_row = agg.loc[agg['revenue_usd'].idxmax()]

result = {
    'title': max_row['resolved_title'] if max_row['resolved_title'] is not None else '',
    'artist': max_row['resolved_artist'] if max_row['resolved_artist'] is not None else '',
    'total_revenue_usd': round(float(max_row['revenue_usd']), 2),
    'contributing_track_ids': max_row['track_id']
}

# Print result following required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Mln8s1FaGhHeRlX9sKrlAgCK': 'file_storage/call_Mln8s1FaGhHeRlX9sKrlAgCK.json', 'var_call_ko0lAPvxRRQt5rqv6sTm9EiB': 'file_storage/call_ko0lAPvxRRQt5rqv6sTm9EiB.json'}

exec(code, env_args)
