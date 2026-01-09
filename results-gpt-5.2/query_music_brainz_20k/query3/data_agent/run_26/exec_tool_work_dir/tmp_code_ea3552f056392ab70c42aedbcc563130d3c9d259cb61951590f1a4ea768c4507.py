code = """import json, pandas as pd

path_sales = var_call_WukId8qzMcGtgecPWdFAplah
with open(path_sales, 'r', encoding='utf-8') as f:
    sales_agg = json.load(f)
df_sales = pd.DataFrame(sales_agg)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

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
    if s.lower() in ['none','nan']:
        return ''
    s = s.strip().lower()
    for ch in ['–','—','-','_','/','\\','|',':',';','(',')','[',']','{','}','"',"'"]:
        s = s.replace(ch,' ')
    return ' '.join(s.split())

def norm_year(y):
    if y is None:
        return ''
    y = str(y).strip().strip("'")
    if y.lower() in ['none','nan','']:
        return ''
    digits = ''.join(ch for ch in y if ch.isdigit())
    if len(digits) in [1,2,4]:
        return digits
    return digits[:4] if len(digits)>4 else digits

# initial keys
raw_title = df_tracks['title'].fillna('')
df_tracks['k_title'] = df_tracks['title'].map(norm_str)
df_tracks['k_artist'] = df_tracks['artist'].map(norm_str)
df_tracks['k_album'] = df_tracks['album'].map(norm_str)
df_tracks['k_year'] = df_tracks['year'].map(norm_year)

# if artist missing and title contains ' - ', split into artist/title
mask = (df_tracks['k_artist']=='') & raw_title.str.contains(' - ')
split = raw_title[mask].str.split(' - ', n=1, expand=True)
df_tracks.loc[mask, 'k_artist'] = split[0].map(norm_str)
df_tracks.loc[mask, 'k_title'] = split[1].map(norm_str)

# entity key
df_tracks['entity_key'] = df_tracks['k_title'] + '||' + df_tracks['k_artist'] + '||' + df_tracks['k_album']

merged = df_sales.merge(df_tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

ent = merged.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum')
).reset_index()

ent_top = ent.sort_values('total_revenue_usd', ascending=False).head(1)
top_key = ent_top.iloc[0]['entity_key']
top_revenue = float(ent_top.iloc[0]['total_revenue_usd'])

sub = merged[merged['entity_key']==top_key].copy()
# representative metadata: track_id with largest track-level total (already aggregated)
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
