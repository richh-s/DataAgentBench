code = """import json, pandas as pd, re

# load sales per track_id
sales_src = var_call_ZvqxAmYCsjuCdZxcwn5LzwAy
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales_src = json.load(f)
sales_df = pd.DataFrame(sales_src)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)

tracks_src = var_call_a0MpHsXWeiEYhJ25CWLjmPBB
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks_src = json.load(f)
tracks_df = pd.DataFrame(tracks_src)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# consider only tracks that have sales
df = tracks_df.merge(sales_df, on='track_id', how='inner')

def norm_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s

def canonical_title(raw):
    s = norm_text(raw)
    # remove leading artist prefix if present: "artist - title"
    if ' - ' in s:
        left, right = s.split(' - ', 1)
        # if artist field missing and left seems like artist name, treat right as title
        return right.strip()
    return s

def norm_year(y):
    s = norm_text(y)
    if not s:
        return ''
    s = re.sub(r"[^0-9]", "", s)
    if len(s) == 4:
        return s
    if len(s) == 2:
        # ambiguous; keep as-is
        return s
    if len(s) == 1:
        return s
    return s

# build entity key using title+artist+album+year with normalization
# If artist missing, try parse from title prefix before ' - '
artist_norm = df['artist'].apply(norm_text)
parsed_artist = df['title'].apply(lambda t: norm_text(str(t).split(' - ',1)[0]) if isinstance(t,str) and ' - ' in t else '')
use_artist = artist_norm.where(artist_norm!='', parsed_artist)

title_norm = df['title'].apply(canonical_title)
album_norm = df['album'].apply(norm_text)
year_norm = df['year'].apply(norm_year)

df['entity_key'] = list(zip(title_norm, use_artist, album_norm, year_norm))

# aggregate revenue by entity
agg = df.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)
top = agg.iloc[0]
key = top['entity_key']

# pick a representative record from df for display
rep = df[df['entity_key']==key].sort_values('total_revenue_usd', ascending=False).iloc[0]
ans = {
    'title': rep['title'],
    'artist': rep['artist'] if rep['artist'] not in [None, 'None'] else (rep['title'].split(' - ',1)[0] if isinstance(rep['title'],str) and ' - ' in rep['title'] else None),
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': float(top['total_revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(ans, ensure_ascii=False))"""

env_args = {'var_call_ZvqxAmYCsjuCdZxcwn5LzwAy': 'file_storage/call_ZvqxAmYCsjuCdZxcwn5LzwAy.json', 'var_call_a0MpHsXWeiEYhJ25CWLjmPBB': 'file_storage/call_a0MpHsXWeiEYhJ25CWLjmPBB.json'}

exec(code, env_args)
