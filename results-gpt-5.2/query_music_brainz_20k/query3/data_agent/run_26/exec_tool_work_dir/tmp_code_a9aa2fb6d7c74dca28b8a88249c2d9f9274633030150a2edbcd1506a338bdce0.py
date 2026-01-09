code = """import json, pandas as pd

# load sales agg
path_sales = var_call_WukId8qzMcGtgecPWdFAplah
with open(path_sales, 'r', encoding='utf-8') as f:
    sales_agg = json.load(f)
df_sales = pd.DataFrame(sales_agg)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# load tracks
path_tracks = var_call_JSsMA4CFGUf5jxq6vvSky9T8
with open(path_tracks, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
df_tracks = pd.DataFrame(tracks)
for c in ['title','artist','album','year']:
    df_tracks[c] = df_tracks[c].astype('string')

def norm_str(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none' or s.lower() == 'nan':
        return ''
    s = s.strip().lower()
    # remove common separators and extra spaces
    for ch in ['\u2013','\u2014','-','_','/','\\','|',':',';','(',')','[',']','{','}','\"','\'']:
        s = s.replace(ch,' ')
    s = ' '.join(s.split())
    return s

def norm_year(y):
    if y is None:
        return ''
    y = str(y).strip().strip("'")
    if y.lower() in ['none','nan','']:
        return ''
    # keep digits only
    digits = ''.join(ch for ch in y if ch.isdigit())
    if len(digits)==4:
        return digits
    if len(digits)==2:
        # ambiguous; keep as 2-digit token
        return digits
    if len(digits)==1:
        return digits
    return digits[:4] if len(digits)>4 else digits

# create entity key using title+artist+album (year ignored due to noise)
df_tracks['k_title'] = df_tracks['title'].map(norm_str)
df_tracks['k_artist'] = df_tracks['artist'].map(norm_str)
df_tracks['k_album'] = df_tracks['album'].map(norm_str)
df_tracks['k_year'] = df_tracks['year'].map(norm_year)

# heuristic: sometimes artist embedded in title like "Artist - Track" when artist missing
# if artist empty and title contains ' - ', split first chunk as artist and rest as title
raw_title = df_tracks['title'].fillna('')
mask = (df_tracks['k_artist']=='') & raw_title.str.contains(' - ')
# split
split = raw_title[mask].str.split(' - ', n=1, expand=True)
df_tracks.loc[mask, 'k_artist'] = split[0].map(norm_str)
df_tracks.loc[mask, 'k_title'] = split[1].map(norm_str)

# entity key
# If album missing, still use empty album.
df_tracks['entity_key'] = df_tracks['k_title'] + '||' + df_tracks['k_artist'] + '||' + df_tracks['k_album']

# join sales to tracks to get entity
merged = df_sales.merge(df_tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# aggregate to entity
ent = merged.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    any_track_id=('track_id','min'),
).reset_index()

# pick top entity
ent_top = ent.sort_values('total_revenue_usd', ascending=False).head(1)
top_key = ent_top.iloc[0]['entity_key']
top_revenue = float(ent_top.iloc[0]['total_revenue_usd'])

# representative metadata: choose the track within entity with max revenue
sub = merged[merged['entity_key']==top_key].copy()
sub = sub.sort_values('total_revenue_usd', ascending=False)
rep = sub.iloc[0]

answer = {
    'title': None if pd.isna(rep['title']) else str(rep['title']),
    'artist': None if pd.isna(rep['artist']) else str(rep['artist']),
    'album': None if pd.isna(rep['album']) else str(rep['album']),
    'year': None if pd.isna(rep['year']) else str(rep['year']),
    'total_revenue_usd': round(top_revenue, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_WukId8qzMcGtgecPWdFAplah': 'file_storage/call_WukId8qzMcGtgecPWdFAplah.json', 'var_call_JSsMA4CFGUf5jxq6vvSky9T8': 'file_storage/call_JSsMA4CFGUf5jxq6vvSky9T8.json'}

exec(code, env_args)
