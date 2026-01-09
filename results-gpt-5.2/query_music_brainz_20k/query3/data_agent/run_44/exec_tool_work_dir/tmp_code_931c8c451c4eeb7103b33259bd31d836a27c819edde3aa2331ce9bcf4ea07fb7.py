code = """import json, pandas as pd, re

# load sales totals per track_id
sales_src = var_call_zGCXTYXQrXKY82WZyVBGf3My
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

df_sales = pd.DataFrame(sales)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# load tracks
tracks_src = var_call_TWQww3cgdlwfFir1zE8V0pUn
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

df_tracks = pd.DataFrame(tracks)
for c in ['title','artist','album','year']:
    if c in df_tracks.columns:
        df_tracks[c] = df_tracks[c].astype(str)

# normalize
def norm_str(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower()=='none' or s.strip()=='' or s.strip().lower()=='[unknown]':
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s

def norm_title(t):
    t = norm_str(t)
    # remove leading track numbers like 001-, 01-, etc
    t = re.sub(r"^(\d{1,3}[-_. ]+)", "", t)
    # if pattern 'artist - title' and artist missing, keep full but also compute split
    return t

def year_bucket(y):
    y = norm_str(y)
    if not y:
        return ''
    y = re.sub(r"[^0-9]", "", y)
    if len(y)==4:
        return y
    if len(y)==2:
        # ambiguous; bucket as last2
        return y
    return y

df_tracks['n_title'] = df_tracks['title'].map(norm_title)
df_tracks['n_artist'] = df_tracks['artist'].map(norm_str)
df_tracks['n_album'] = df_tracks['album'].map(norm_str)
df_tracks['y'] = df_tracks['year'].map(year_bucket)

# derive a fallback: if artist is empty but title contains ' - ', split
split = df_tracks['n_title'].str.split(' - ', n=1, expand=True)
mask = (df_tracks['n_artist']=='') & (split.shape[1]==2)
df_tracks.loc[mask, 'n_artist'] = split.loc[mask,0].fillna('')
df_tracks.loc[mask, 'n_title'] = split.loc[mask,1].fillna('')

# entity key: prefer title+artist; include album if available; include year bucket if available
# to avoid over-splitting, use album only when present
key_parts = []
key_parts.append(df_tracks['n_title'])
key_parts.append(df_tracks['n_artist'])
# album if exists else empty
key_parts.append(df_tracks['n_album'])
key_parts.append(df_tracks['y'])

df_tracks['entity_key'] = (key_parts[0]+'|'+key_parts[1]+'|'+key_parts[2]+'|'+key_parts[3]).str.strip('|')

# join sales totals to track attributes
merged = df_sales.merge(df_tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# aggregate by entity_key
agg = merged.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    any_title=('title','first'),
    any_artist=('artist','first'),
    any_album=('album','first'),
    any_year=('year','first'),
    n_track_ids=('track_id','nunique')
).reset_index()

# pick max
agg_sorted = agg.sort_values('total_revenue_usd', ascending=False).head(1)
res = agg_sorted.to_dict(orient='records')[0]
# round revenue
res['total_revenue_usd'] = float(round(res['total_revenue_usd'], 2))

print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_zGCXTYXQrXKY82WZyVBGf3My': 'file_storage/call_zGCXTYXQrXKY82WZyVBGf3My.json', 'var_call_TWQww3cgdlwfFir1zE8V0pUn': 'file_storage/call_TWQww3cgdlwfFir1zE8V0pUn.json'}

exec(code, env_args)
