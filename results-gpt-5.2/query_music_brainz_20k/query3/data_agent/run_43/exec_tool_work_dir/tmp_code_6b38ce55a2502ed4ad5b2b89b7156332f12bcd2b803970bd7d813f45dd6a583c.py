code = """import json, pandas as pd, re

# load sales top track_id list
sales_path = var_call_ETy2cRzU8vyVRRNrMzoKJBFo
with open(sales_path,'r',encoding='utf-8') as f:
    sales_top = json.load(f)

tracks_path = var_call_WBqk5ggQXDalT8JspkxFxQKo
with open(tracks_path,'r',encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_top)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# take enough top candidates
cand = df_sales.sort_values('total_revenue_usd', ascending=False).head(200).copy()

# map track_id to track attributes
tr = pd.DataFrame(tracks)
tr['track_id'] = tr['track_id'].astype(int)
tr_small = tr[tr['track_id'].isin(cand['track_id'])].copy()

# normalize for entity resolution

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower()=='none':
        return ''
    s = s.lower()
    s = re.sub(r"\s+",' ',s).strip()
    s = re.sub(r"[^a-z0-9 ]+",'',s)
    return s

for col in ['title','artist','album','year']:
    tr_small[col] = tr_small[col].apply(norm)

# heuristic: if artist missing but embedded in title as 'artist - title', split

def split_artist_title(row):
    t = row['title']
    a = row['artist']
    if (not a) and (' - ' in str(row.get('title_raw',''))):
        pass

# keep raw too
tr_small['title_raw'] = tr[tr['track_id'].isin(cand['track_id'])]['title'].values
tr_small['artist_raw'] = tr[tr['track_id'].isin(cand['track_id'])]['artist'].values
tr_small['album_raw'] = tr[tr['track_id'].isin(cand['track_id'])]['album'].values
tr_small['year_raw'] = tr[tr['track_id'].isin(cand['track_id'])]['year'].values

# create resolved key
# If artist missing, try parse from raw title patterns "Artist - Title" or "Artist – Title"

def derive(row):
    title_n = row['title']
    artist_n = row['artist']
    album_n = row['album']
    year_n = row['year']
    raw_title = '' if row['title_raw'] is None else str(row['title_raw'])
    if (not artist_n) and ('-' in raw_title):
        parts = re.split(r"\s*[-–]\s*", raw_title, maxsplit=1)
        if len(parts)==2:
            # guess first is artist if it looks like words and second not empty
            art_guess = norm(parts[0])
            tit_guess = norm(parts[1])
            if art_guess and tit_guess:
                artist_n = art_guess
                title_n = tit_guess
    # some titles have track number prefixes like 001-, 01- etc
    title_n = re.sub(r"^(\d{1,3})(\s+|-)\s*",'',title_n).strip()
    return pd.Series({'title_n':title_n,'artist_n':artist_n,'album_n':album_n,'year_n':year_n})

tr_small = pd.concat([tr_small, tr_small.apply(derive, axis=1)], axis=1)

# entity key: title+artist (album optional)
tr_small['entity_key'] = tr_small['title_n'] + '|' + tr_small['artist_n']

cand = cand.merge(tr_small[['track_id','entity_key','title_raw','artist_raw','album_raw','year_raw','title_n','artist_n']], on='track_id', how='left')

# aggregate revenue across duplicates (same entity_key)
agg = cand.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

top_entity = agg.iloc[0].to_dict()
entity_key = top_entity['entity_key']

# find representative record: highest revenue track_id within entity
sub = cand[cand['entity_key']==entity_key].sort_values('total_revenue_usd', ascending=False)
rep = sub.iloc[0]

result = {
    'entity_key': entity_key,
    'song_title': rep['title_raw'],
    'artist': rep['artist_raw'],
    'total_revenue_usd': float(top_entity['total_revenue_usd']),
    'representative_track_id': int(rep['track_id']),
    'num_duplicate_track_ids_in_top200': int(sub.shape[0]),
    'duplicate_track_ids_in_top200': [int(x) for x in sub['track_id'].tolist()],
    'note': 'Entity resolution via normalized title+artist; aggregated across duplicate track_ids appearing in top200 revenue list.'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ETy2cRzU8vyVRRNrMzoKJBFo': 'file_storage/call_ETy2cRzU8vyVRRNrMzoKJBFo.json', 'var_call_WBqk5ggQXDalT8JspkxFxQKo': 'file_storage/call_WBqk5ggQXDalT8JspkxFxQKo.json'}

exec(code, env_args)
