code = """import pandas as pd
import json
import re
import unicodedata

# Load data from storage file paths
with open(var_call_LdxmDu0vLGdZH08zCRY0wDqB, 'r', encoding='utf-8') as f:
    tracks_data = json.load(f)
with open(var_call_2Nkay3xgXi0mDWfKvaFNYI6z, 'r', encoding='utf-8') as f:
    sales_data = json.load(f)

tracks = pd.DataFrame(tracks_data)
sales = pd.DataFrame(sales_data)

# Ensure numeric types
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce').fillna(0.0)
sales['track_id'] = sales['track_id'].astype(str)
tracks['track_id'] = tracks['track_id'].astype(str)

# Clean helper functions

def remove_diacritics(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))

COMMON_BAD_WORDS = [r'\blive\b', r'\bremix\b', r'\bacoustic\b', r"\bversion\b", r"\bremastered\b",
                    r"\bfeat\b", r"\bfeaturing\b", r"\bft\b", r"\bedit\b", r"\bsingle\b"]


def normalize_text(s):
    if s is None: 
        return ''
    s = str(s)
    if s.strip().lower() in ['', 'none', "nan", 'n/a']:
        return ''
    s = s.strip()
    # remove quotes
    s = s.replace('\u2019', "'")
    # remove content in parentheses and brackets
    s = re.sub(r"\[.*?\]", "", s)
    s = re.sub(r"\(.*?\)", "", s)
    # remove trailing/leading separators like ':' or ' - ' content if clearly a qualifier
    # but keep a chance to split artist-title if artist missing
    s = s
    # unicode normalize and lower
    s = remove_diacritics(s).lower()
    # remove punctuation except spaces
    s = re.sub(r"[^a-z0-9\s]", ' ', s)
    # remove common bad words
    for w in COMMON_BAD_WORDS:
        s = re.sub(w, ' ', s)
    # collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# If artist missing and title contains ' - ', split
tracks['artist'] = tracks['artist'].replace({'None': None, '': None})
tracks['title'] = tracks['title'].replace({'None': None, '': None})

for idx, row in tracks.iterrows():
    art = row['artist']
    tit = row['title']
    if (art is None or str(art).strip().lower() in ['none', '']) and isinstance(tit, str) and ' - ' in tit:
        parts = tit.split(' - ', 1)
        # Heuristic: if left side looks like an artist (contains letters and not too long), assign
        left = parts[0].strip()
        right = parts[1].strip()
        if len(left) <= 60:
            tracks.at[idx, 'artist'] = left
            tracks.at[idx, 'title'] = right

# Create normalized fields
tracks['norm_title'] = tracks['title'].apply(lambda x: normalize_text(x))
tracks['norm_artist'] = tracks['artist'].apply(lambda x: normalize_text(x))

# If artist is empty after normalization, rely on title only for key
tracks['entity_key'] = tracks.apply(lambda r: (r['norm_title'] + '||' + r['norm_artist']) if r['norm_artist'] else r['norm_title'], axis=1)

# Aggregate sales by track_id
sales_agg = sales.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Map each track to its entity_key
mapping = tracks.set_index('track_id')['entity_key'].to_dict()

# Some sales may reference track_ids not present in tracks; handle by using track_id as key
sales_agg['entity_key'] = sales_agg['track_id'].map(mapping).fillna(sales_agg['track_id'])

# Aggregate revenue by entity_key
entity_rev = sales_agg.groupby('entity_key', as_index=False)['revenue_usd'].sum()

# Find top entity
top = entity_rev.sort_values('revenue_usd', ascending=False).iloc[0]
top_key = top['entity_key']
top_revenue = float(top['revenue_usd'])

# Derive display title and artist from tracks grouped by key
group = tracks[tracks['entity_key'] == top_key]
if not group.empty:
    # choose most common original title and artist (non-null)
    disp_title = group['title'].dropna().mode()
    disp_artist = group['artist'].dropna().mode()
    display_title = disp_title.iloc[0] if not disp_title.empty else ''
    display_artist = disp_artist.iloc[0] if not disp_artist.empty else ''
else:
    # fallback when key is raw track_id
    tid = top_key
    display_title = ''
    display_artist = ''
    # try to find in tracks
    if tid in mapping:
        row = tracks[tracks['track_id']==tid].iloc[0]
        display_title = row['title'] if pd.notna(row['title']) else ''
        display_artist = row['artist'] if pd.notna(row['artist']) else ''

result = {
    'title': display_title,
    'artist': display_artist,
    'total_revenue_usd': round(top_revenue, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_b5caUjr1yW8cIc92j5K3XGk7': ['tracks'], 'var_call_z6F8SCIdovij91U8urvKRDjl': ['sales'], 'var_call_LdxmDu0vLGdZH08zCRY0wDqB': 'file_storage/call_LdxmDu0vLGdZH08zCRY0wDqB.json', 'var_call_2Nkay3xgXi0mDWfKvaFNYI6z': 'file_storage/call_2Nkay3xgXi0mDWfKvaFNYI6z.json'}

exec(code, env_args)
