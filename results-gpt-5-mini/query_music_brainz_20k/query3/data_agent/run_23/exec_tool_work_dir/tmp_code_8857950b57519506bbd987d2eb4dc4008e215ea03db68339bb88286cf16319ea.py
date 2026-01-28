code = """import json
import pandas as pd
import re

# Load data from storage files
tracks_path = var_call_G6FzIukjR2235Ty5bjIQGYlP
sales_path = var_call_eYAcjsmmXFAqyHeMDoIpuKVU

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize missing values that are literal strings like 'None' or empty
def clean_null(x):
    if pd.isna(x):
        return None
    if isinstance(x, str):
        s = x.strip()
        if s == '' or s.lower() in ('none', 'nan', '[unknown]'):
            return None
        return s
    return x

for col in tracks_df.columns:
    tracks_df[col] = tracks_df[col].apply(clean_null)
for col in sales_df.columns:
    sales_df[col] = sales_df[col].apply(clean_null)

# Convert types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
# revenue_usd may be string; convert to float
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Helper normalization
non_alnum_re = re.compile(r'[^0-9a-zA-Z ]+')
paren_re = re.compile(r"\(.*?\)")

def extract_artist_title(row):
    title = row.get('title') or ''
    artist = row.get('artist') or ''
    album = row.get('album') or ''
    year = row.get('year') or ''

    # If artist missing or generic, try to extract from title patterns like 'Artist - Title' or 'Artist: Title'
    if not artist:
        if ' - ' in title:
            left, right = title.split(' - ', 1)
            # Heuristic: if left has letters and right also, assume left is artist
            if re.search('[A-Za-z]', left):
                artist = left.strip()
                title = right.strip()
        elif ' – ' in title:
            left, right = title.split(' – ', 1)
            if re.search('[A-Za-z]', left):
                artist = left.strip()
                title = right.strip()
        elif ':' in title:
            left, right = title.split(':', 1)
            # only take as artist if left looks like a name (no digits)
            if re.search('[A-Za-z]', left) and not re.search('\d', left):
                artist = left.strip()
                title = right.strip()

    # Remove parentheses content from title
    title = paren_re.sub('', title)
    # Remove any trailing descriptors after ':' (keep the main title before colon)
    if ':' in title:
        title = title.split(':',1)[0]
    # Normalize
    def norm(s):
        if not s:
            return ''
        s = s.lower()
        s = paren_re.sub('', s)
        s = s.replace('\n',' ').replace('\t',' ')
        s = re.sub(r"\s+"," ", s)
        # remove punctuation
        s = non_alnum_re.sub('', s)
        s = s.strip()
        return s

    norm_title = norm(title)
    norm_artist = norm(artist)
    norm_album = norm(album)
    norm_year = norm(str(year)) if year else ''

    # Build canonical key: prefer title+artist; if artist missing, include album+year
    if norm_artist:
        key = f"{norm_title}||{norm_artist}"
    else:
        key = f"{norm_title}||album:{norm_album}||year:{norm_year}"
    return pd.Series({'canon_key': key, 'canon_title': title.strip() if title else None, 'canon_artist': artist.strip() if artist else None})

canon = tracks_df.apply(extract_artist_title, axis=1)
tracks_df = pd.concat([tracks_df, canon], axis=1)

# For each canonical key, decide a representative title and artist (most common non-empty)
rep = tracks_df.groupby('canon_key').agg({
    'canon_title': lambda x: next((v for v in x if v and v.strip()), ''),
    'canon_artist': lambda x: next((v for v in x if v and v.strip()), '')
}).reset_index()

# Map track_id to canon_key
track_to_key = tracks_df.set_index('track_id')['canon_key'].to_dict()

# Map sales to canonical keys
sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)

# Drop sales that don't map (shouldn't happen)
sales_df = sales_df[sales_df['canon_key'].notnull()]

# Aggregate revenue by canonical key
rev_by_key = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].sum().reset_index()
# Join representative title/artist
rev_by_key = rev_by_key.merge(rep, on='canon_key', how='left')

# Find max
rev_by_key['revenue_usd'] = rev_by_key['revenue_usd'].astype(float)
max_row = rev_by_key.loc[rev_by_key['revenue_usd'].idxmax()]

result = {
    'title': max_row['canon_title'] if max_row['canon_title'] else None,
    'artist': max_row['canon_artist'] if max_row['canon_artist'] else None,
    'total_revenue_usd': round(float(max_row['revenue_usd']), 2)
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_G6FzIukjR2235Ty5bjIQGYlP': 'file_storage/call_G6FzIukjR2235Ty5bjIQGYlP.json', 'var_call_eYAcjsmmXFAqyHeMDoIpuKVU': 'file_storage/call_eYAcjsmmXFAqyHeMDoIpuKVU.json'}

exec(code, env_args)
