code = """import json
import pandas as pd
import re
import unicodedata

# Load data from previous query results stored in files
tracks_path = var_call_SbvgonvKSXjZptd2QOolOEKO
sales_path = var_call_yPn6frnCncRmblUeK9HOdJFk

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks_list = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales_list = json.load(f)

tracks = pd.DataFrame(tracks_list)
sales = pd.DataFrame(sales_list)

# Ensure track_id and numeric columns are correct types
tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)
sales['units_sold'] = sales['units_sold'].astype(int)

# Normalization helpers

def remove_parenthetical(text):
    if not isinstance(text, str):
        return text
    # remove content in parentheses or brackets
    return re.sub(r"\([^)]*\)|\[[^]]*\]", "", text)


def normalize_text(text):
    if text is None:
        return ''
    if not isinstance(text, str):
        text = str(text)
    text = text.strip()
    if text.lower() in ('none', '', 'nan'):
        return ''
    # remove parenthetical parts
    text = remove_parenthetical(text)
    # normalize unicode
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    # replace ampersand
    text = text.replace('&', ' and ')
    # remove punctuation except alphanum and spaces
    text = re.sub(r"[^0-9a-z\s]", ' ', text)
    # collapse whitespace
    text = re.sub(r"\s+", ' ', text).strip()
    return text


def normalize_year(y):
    if not isinstance(y, str):
        try:
            y = str(int(y))
        except Exception:
            return ''
    if y.lower() in ('none', 'nan', ''):
        return ''
    # find 4-digit year
    m = re.search(r"(19|20)\d{2}", y)
    if m:
        return m.group(0)
    # find two digits
    m2 = re.search(r"\d{2}", y)
    if m2:
        return m2.group(0)
    return ''

# Apply normalization
tracks['n_title'] = tracks['title'].apply(normalize_text)
tracks['n_artist'] = tracks['artist'].apply(normalize_text)
tracks['n_album'] = tracks['album'].apply(normalize_text)
tracks['n_year'] = tracks['year'].apply(lambda x: normalize_year(x if x is not None else ''))

# Create grouping key: use title + artist as main identity
tracks['entity_key'] = tracks['n_title'] + ' ||| ' + tracks['n_artist']

# Map track_id to entity_key and keep original fields
track_map = tracks[['track_id', 'entity_key', 'title', 'artist', 'album', 'year']].copy()

# Merge sales with track mapping
merged = sales.merge(track_map, on='track_id', how='left')

# For any sales with missing mapping, create entity_key from sales track_id (unlikely)
merged['entity_key'] = merged['entity_key'].fillna('unknown_entity_' + merged['track_id'])

# Aggregate revenue by entity_key
agg = merged.groupby('entity_key').agg(
    total_revenue_usd=('revenue_usd', 'sum'),
    total_units_sold=('units_sold', 'sum'),
    track_ids=('track_id', lambda x: sorted(list(set(x))))
).reset_index()

# Attach representative metadata for each entity_key from tracks table
# choose most frequent non-empty title/artist/album/year among mapped track_ids
rep_rows = []
for _, row in agg.iterrows():
    tids = row['track_ids']
    subset = tracks[tracks['track_id'].isin(tids)]
    def most_common_nonempty(col):
        vals = subset[col].astype(str).replace('None', '').replace('nan', '')
        vals = [v for v in vals if v and v.lower()!='none']
        if not vals:
            return ''
        # return most common
        return max(set(vals), key=vals.count)
    rep_title = most_common_nonempty('title')
    rep_artist = most_common_nonempty('artist')
    rep_album = most_common_nonempty('album')
    rep_year = most_common_nonempty('year')
    rep_rows.append((rep_title, rep_artist, rep_album, rep_year))

agg[['rep_title','rep_artist','rep_album','rep_year']] = pd.DataFrame(rep_rows, index=agg.index)

# Find the max revenue entity
max_row = agg.loc[agg['total_revenue_usd'].idxmax()]

result = {
    'title': max_row['rep_title'] if max_row['rep_title'] else None,
    'artist': max_row['rep_artist'] if max_row['rep_artist'] else None,
    'album': max_row['rep_album'] if max_row['rep_album'] else None,
    'year': max_row['rep_year'] if max_row['rep_year'] else None,
    'total_revenue_usd': round(float(max_row['total_revenue_usd']), 2),
    'total_units_sold': int(max_row['total_units_sold']),
    'track_ids': max_row['track_ids']
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_SbvgonvKSXjZptd2QOolOEKO': 'file_storage/call_SbvgonvKSXjZptd2QOolOEKO.json', 'var_call_yPn6frnCncRmblUeK9HOdJFk': 'file_storage/call_yPn6frnCncRmblUeK9HOdJFk.json'}

exec(code, env_args)
