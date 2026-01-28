code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage-provided file paths
sales_agg_path = var_call_h4ljpS3m7ghbUXbS9Afgi9Ae
tracks_path = var_call_kjDtG3XQV07Tv5BORYXHhmBh

with open(sales_agg_path, 'r', encoding='utf-8') as f:
    sales_agg = json.load(f)
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales_agg)
tracks_df = pd.DataFrame(tracks)

# Normalize types
sales_df['track_id'] = sales_df['track_id'].astype(int)
# total_revenue might be strings
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Merge
df = pd.merge(tracks_df, sales_df, on='track_id', how='inner')

# Helper normalize function
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    # treat common null-like values
    if s.strip().lower() in ('none', "[unknown]", '', 'nan'):
        return ''
    # remove content in parentheses
    s = re.sub(r"\(.*?\)", "", s)
    # unicode normalize
    s = unicodedata.normalize('NFKD', s)
    # remove accents
    s = ''.join(c for c in s if not unicodedata.combining(c))
    # lower
    s = s.lower()
    # remove punctuation except spaces and alphanum
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    # remove common words like live, remix, version
    s = re.sub(r"\b(live|remix|version|studio|acoustic|edit)\b", " ", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Create normalized keys
for col in ['title', 'artist', 'album', 'year']:
    df[f'norm_{col}'] = df[col].apply(normalize_text)

# Combine into an entity key; year may be noisy, but include
df['entity_key'] = df['norm_title'] + ' ||| ' + df['norm_artist'] + ' ||| ' + df['norm_album'] + ' ||| ' + df['norm_year']

# Group by entity_key
grouped = df.groupby('entity_key').agg(
    total_revenue_sum = ('total_revenue', 'sum'),
    track_ids = ('track_id', lambda x: sorted(x.unique().tolist())),
    titles = ('title', lambda x: list(x.dropna().unique().tolist())),
    artists = ('artist', lambda x: list(x.dropna().unique().tolist())),
    albums = ('album', lambda x: list(x.dropna().unique().tolist())),
    years = ('year', lambda x: list(x.dropna().unique().tolist())),
    records_count = ('track_id', 'count')
).reset_index()

# Sort to find top
grouped = grouped.sort_values('total_revenue_sum', ascending=False)
if grouped.shape[0] == 0:
    result = {
        'title': None,
        'artist': None,
        'album': None,
        'year': None,
        'total_revenue_usd': None,
        'track_ids': [],
        'records_count': 0
    }
else:
    top = grouped.iloc[0]
    # pick representative title/artist/album/year: choose the longest non-empty string from the lists
    def pick_best(lst):
        if not lst:
            return None
        # filter out null-like
        lst2 = [str(x).strip() for x in lst if str(x).strip().lower() not in ('none', '')]
        if not lst2:
            return None
        # choose most common or longest
        # prefer the one with max length
        return max(lst2, key=lambda x: (len(x), lst2.count(x)))
    rep_title = pick_best(top['titles'])
    rep_artist = pick_best(top['artists'])
    rep_album = pick_best(top['albums'])
    rep_year = pick_best(top['years'])
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'album': rep_album,
        'year': rep_year,
        'total_revenue_usd': round(float(top['total_revenue_sum']), 2),
        'track_ids': [int(x) for x in top['track_ids']],
        'records_count': int(top['records_count'])
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VdgrA13WTSfKCgB8y1Fg5jA1': ['tracks'], 'var_call_3quJsaegkdfmHWEFNfOk2IHA': ['sales'], 'var_call_h4ljpS3m7ghbUXbS9Afgi9Ae': 'file_storage/call_h4ljpS3m7ghbUXbS9Afgi9Ae.json', 'var_call_kjDtG3XQV07Tv5BORYXHhmBh': 'file_storage/call_kjDtG3XQV07Tv5BORYXHhmBh.json'}

exec(code, env_args)
