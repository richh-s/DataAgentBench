code = """import json
import pandas as pd
import unicodedata
import re

# Load data from storage variables (they may be file paths)
tracks_obj = var_call_BSAAM0qhzmg2cUsgfxEbYlaN
sales_obj = var_call_xnQwCguZsMt5wacrHgjmqO0C

if isinstance(tracks_obj, str):
    with open(tracks_obj, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_obj

if isinstance(sales_obj, str):
    with open(sales_obj, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_obj

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure numeric types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

# Sum revenue per track_id
rev_per_track = sales_df.groupby('track_id', dropna=False)['revenue_usd'].sum().reset_index()
rev_per_track.columns = ['track_id', 'total_revenue_usd']

# Merge with tracks
merged = pd.merge(tracks_df, rev_per_track, on='track_id', how='left')
merged['total_revenue_usd'] = merged['total_revenue_usd'].fillna(0.0)

# Helper normalization

def clean_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ['none', 'nan', '[unknown]']:
        return ''
    # Move common separators: if artist missing and title contains ' - ', extract
    return s

# Preprocess artist/title extraction when title contains artist
for idx, row in merged.iterrows():
    title = row.get('title', '')
    artist = row.get('artist', '')
    if (not artist or str(artist).strip().lower() in ['', 'none', '[unknown]']) and isinstance(title, str) and ' - ' in title:
        parts = title.split(' - ', 1)
        # if left part looks like a name (contains letters), use it as artist
        left = parts[0].strip()
        right = parts[1].strip()
        if re.search('[A-Za-z]', left):
            merged.at[idx, 'artist'] = left
            merged.at[idx, 'title'] = right

# Normalization function

def normalize(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ['none', 'nan', '[unknown]', '']:
        return ''
    # remove content in parentheses and after colon in many cases
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r":.*$", "", s)
    # unicode normalization (remove accents)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    # replace non-alphanum with space
    s = re.sub(r'[^a-z0-9]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Build signature
merged['title_norm'] = merged['title'].apply(normalize)
merged['artist_norm'] = merged['artist'].apply(normalize)
merged['album_norm'] = merged['album'].apply(normalize)
merged['year_norm'] = merged['year'].apply(lambda x: normalize(str(x)))

# Create signature priority: title+artist, if missing artist use title+album, else title alone

def signature(row):
    t = row['title_norm']
    a = row['artist_norm']
    al = row['album_norm']
    y = row['year_norm']
    if t and a:
        return t + '||' + a
    if t and al:
        return t + '||' + al
    if t and y:
        return t + '||' + y
    return t

merged['signature'] = merged.apply(signature, axis=1)

# Group by signature and sum revenue
grouped = merged.groupby('signature', dropna=False).agg({
    'total_revenue_usd': 'sum',
    'track_id': lambda x: list(x),
    'title': lambda x: list(x),
    'artist': lambda x: list(x)
}).reset_index()

# Choose representative title/artist for each group: most common non-empty

def choose_rep(lst):
    cleaned = [str(x).strip() for x in lst if str(x).strip().lower() not in ['', 'none', '[unknown]']]
    if not cleaned:
        return ''
    # return the most frequent
    from collections import Counter
    return Counter(cleaned).most_common(1)[0][0]

grouped['rep_title'] = grouped['title'].apply(choose_rep)
grouped['rep_artist'] = grouped['artist'].apply(choose_rep)

# Find top group by revenue
if grouped.empty:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0, 'track_ids': []}
else:
    top = grouped.sort_values('total_revenue_usd', ascending=False).iloc[0]
    result = {
        'title': top['rep_title'] if top['rep_title'] else None,
        'artist': top['rep_artist'] if top['rep_artist'] else None,
        'total_revenue_usd': float(top['total_revenue_usd']),
        'track_ids': top['track_id']
    }

# Print result following required format
import json
print("----BEGIN PRINT FORMAT----")
print('__RESULT__:')
print(json.dumps(result))
print("----END PRINT FORMAT----")"""

env_args = {'var_call_BSAAM0qhzmg2cUsgfxEbYlaN': 'file_storage/call_BSAAM0qhzmg2cUsgfxEbYlaN.json', 'var_call_xnQwCguZsMt5wacrHgjmqO0C': 'file_storage/call_xnQwCguZsMt5wacrHgjmqO0C.json'}

exec(code, env_args)
