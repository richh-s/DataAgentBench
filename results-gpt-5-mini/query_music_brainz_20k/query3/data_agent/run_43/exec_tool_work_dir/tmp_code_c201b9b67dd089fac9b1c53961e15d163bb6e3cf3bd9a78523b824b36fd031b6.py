code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_TLZAG1o26wERfPpNf7lhyFbb, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_cyV1ocxXEcuTIeAQXkQ73DOU, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize column types
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
# revenue may be string
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Helper normalize function
stopwords_pattern = re.compile(r"\b(live|remix|acoustic|version|feat|featuring|ft|remastered|single|deluxe|edition|live edit)\b", re.I)
paren_pattern = re.compile(r"\(.*?\)")
non_alnum = re.compile(r"[^a-z0-9\s]")

def clean_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', 'nan', 'n/a', ''):
        return ''
    # remove parenthetical notes
    s = paren_pattern.sub(' ', s)
    # remove common stopwords
    s = stopwords_pattern.sub(' ', s)
    # lowercase
    s = s.lower()
    # replace hyphen surrounded by spaces (artists sometimes "Artist - Title") keep hyphen removal later
    # remove punctuation
    s = non_alnum.sub(' ', s)
    # collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# If artist missing, try to extract from title if of form 'Artist - Title'
def try_extract_artist_title(row):
    title = row.get('title') or ''
    artist = row.get('artist') or ''
    if isinstance(artist, str) and artist.strip().lower() not in ('', 'none', '[unknown]'):
        return title, artist
    # try splitting by ' - '
    if isinstance(title, str) and '-' in title:
        parts = title.split('-', 1)
        left = parts[0].strip()
        right = parts[1].strip()
        # Heuristic: if left contains letters and not too long, treat as artist
        if 1 <= len(left) <= 60 and re.search(r'[a-zA-Z]', left):
            return right, left
    return title, artist

# Build canonical key
norm_titles = []
norm_artists = []
for _, r in tracks_df.iterrows():
    t, a = try_extract_artist_title(r)
    nt = clean_text(t)
    na = clean_text(a)
    # if artist still empty, try to use album as proxy
    if na == '':
        album = r.get('album') or ''
        na = clean_text(album)
    norm_titles.append(nt)
    norm_artists.append(na)

tracks_df['norm_title'] = norm_titles
tracks_df['norm_artist'] = norm_artists
tracks_df['entity_key'] = tracks_df['norm_title'] + '|' + tracks_df['norm_artist']

# For any completely empty keys, fallback to original title
tracks_df.loc[tracks_df['entity_key']=='|', 'entity_key'] = tracks_df.loc[tracks_df['entity_key']=='|', 'title'].fillna('').astype(str)

# Map track_id to entity_key
track_to_entity = tracks_df.set_index('track_id')['entity_key'].to_dict()

# Assign entity_key to sales
sales_df['entity_key'] = sales_df['track_id'].map(track_to_entity)

# For sales with no matching track metadata, set entity_key to track_id (isolated)
sales_df['entity_key'] = sales_df['entity_key'].fillna(sales_df['track_id'])

# Aggregate revenue by entity
agg = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()
agg = agg.sort_values('revenue_usd', ascending=False)

if agg.shape[0] == 0:
    result = {"title": None, "artist": None, "total_revenue_usd": None, "track_ids": []}
else:
    top = agg.iloc[0]
    top_key = top['entity_key']
    total_rev = float(top['revenue_usd'])
    # retrieve representative title and artist from tracks_df for this key
    reps = tracks_df[tracks_df['entity_key']==top_key]
    if not reps.empty:
        # choose most common non-empty title and artist
        title = reps['title'].replace({'None': '', None: ''}).astype(str)
        artist = reps['artist'].replace({'None': '', None: ''}).astype(str)
        rep_title = title[title.str.strip()!=''].mode()
        rep_artist = artist[artist.str.strip()!=''].mode()
        rep_title = rep_title.iloc[0] if not rep_title.empty else reps['title'].iloc[0]
        rep_artist = rep_artist.iloc[0] if not rep_artist.empty else reps['artist'].iloc[0]
    else:
        # no metadata, use key split
        parts = str(top_key).split('|')
        rep_title = parts[0] if len(parts)>0 else ''
        rep_artist = parts[1] if len(parts)>1 else ''
    track_ids = sales_df[sales_df['entity_key']==top_key]['track_id'].unique().tolist()
    result = {
        "title": rep_title,
        "artist": rep_artist,
        "total_revenue_usd": round(total_rev, 2),
        "track_ids": track_ids,
        "entity_key": top_key
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TLZAG1o26wERfPpNf7lhyFbb': 'file_storage/call_TLZAG1o26wERfPpNf7lhyFbb.json', 'var_call_cyV1ocxXEcuTIeAQXkQ73DOU': 'file_storage/call_cyV1ocxXEcuTIeAQXkQ73DOU.json'}

exec(code, env_args)
