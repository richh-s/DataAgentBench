code = """import json
import pandas as pd
import re
import unicodedata

tracks_path = var_call_9ksKfgeBSeGqi6ZS3zfuGO9x
sales_path = var_call_N2XtFAzb2T8Xv7zyNtytDrnl

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
# ensure revenue numeric
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# normalization helpers

def remove_accents(s):
    if s is None:
        return ''
    s = str(s)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s

remove_pattern = re.compile(r"\(.*?\)|\[.*?\]")

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = remove_accents(s)
    s = remove_pattern.sub('', s)
    s = s.lower()
    s = re.sub(r"\b(live|remix|acoustic|version|edit|feat\.?|featuring|with)\b", ' ', s)
    s = re.sub(r"[^a-z0-9\s]", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# clean indicators
bad_vals = set(['none', '', '[unknown]', 'nan', 'na', 'null'])

# extract artist from title when artist missing
def extract_artist_title(row):
    title = row.get('title') or ''
    artist = row.get('artist') or ''
    title = str(title)
    artist = str(artist)
    if artist.strip().lower() in bad_vals:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            if len(parts[0].strip())>0 and re.search('[a-zA-Z]', parts[0]):
                artist = parts[0].strip()
                title = parts[1].strip()
    return title, artist

tracks_df[['clean_title','clean_artist']] = tracks_df.apply(lambda r: pd.Series(extract_artist_title(r)), axis=1)

# normalized fields
tracks_df['norm_title'] = tracks_df['clean_title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['clean_artist'].apply(normalize_text)
# if artist still empty, try album
tracks_df.loc[tracks_df['norm_artist']=='', 'norm_artist'] = tracks_df.loc[tracks_df['norm_artist']=='', 'album'].fillna('').apply(normalize_text)

tracks_df['group_key'] = (tracks_df['norm_artist'].fillna('') + '||' + tracks_df['norm_title'].fillna(''))
tracks_df.loc[tracks_df['group_key']=='||', 'group_key'] = tracks_df.loc[tracks_df['group_key']=='||', 'norm_title']

# mapping
trackid_to_group = tracks_df.set_index('track_id')['group_key'].to_dict()

sales_df['group_key'] = sales_df['track_id'].map(trackid_to_group).fillna(sales_df['track_id'])

# aggregate
rev_by_group = sales_df.groupby('group_key', dropna=False)['revenue_usd'].sum().reset_index()
rev_by_group = rev_by_group.sort_values('revenue_usd', ascending=False)

top_row = rev_by_group.iloc[0]
top_key = top_row['group_key']
top_revenue = float(top_row['revenue_usd'])

# choose representative title/artist
rep_title = ''
rep_artist = ''
if top_key in tracks_df['group_key'].values:
    subset = tracks_df[tracks_df['group_key']==top_key]
    # prefer non-empty and not 'None'
    def pick_mode(col):
        vals = [v for v in subset[col].astype(str).tolist() if v.strip().lower() not in bad_vals]
        if not vals:
            return ''
        # return most common
        return pd.Series(vals).mode(dropna=True).iat[0]
    rep_title = pick_mode('clean_title')
    rep_artist = pick_mode('clean_artist')
else:
    # top group is an unmapped track id
    tid = str(top_key)
    tmeta = tracks_df[tracks_df['track_id']==tid]
    if not tmeta.empty:
        rep_title = tmeta['title'].iat[0]
        rep_artist = tmeta['artist'].iat[0]
    else:
        # fallback: show track id
        rep_title = f"track_id {tid}"
        rep_artist = ''

result = {
    'title': rep_title if rep_title is not None else '',
    'artist': rep_artist if rep_artist is not None else '',
    'total_revenue_usd': round(top_revenue,2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9ksKfgeBSeGqi6ZS3zfuGO9x': 'file_storage/call_9ksKfgeBSeGqi6ZS3zfuGO9x.json', 'var_call_N2XtFAzb2T8Xv7zyNtytDrnl': 'file_storage/call_N2XtFAzb2T8Xv7zyNtytDrnl.json', 'var_call_23Dox7p3A9RmLJJnMVuDZUmk': {'title': '... - ...', 'artist': 'None', 'total_revenue_usd': 120656.95}}

exec(code, env_args)
