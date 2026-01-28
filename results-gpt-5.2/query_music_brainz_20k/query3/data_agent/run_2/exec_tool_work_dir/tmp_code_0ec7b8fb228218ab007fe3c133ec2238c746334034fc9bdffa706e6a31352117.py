code = """import json, pandas as pd

def load(obj):
    if isinstance(obj, str):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

sales_tot = pd.DataFrame(load(var_call_Amb3UFtTUVpQalNE9srLROL4))
tracks = pd.DataFrame(load(var_call_keZYBZZUAv2FVa7VTZV4bOvB))

# types
sales_tot['track_id'] = sales_tot['track_id'].astype(int)
sales_tot['total_revenue_usd'] = sales_tot['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# create entity key using normalized title/artist/album; fallback artist from title pattern "Artist - Title"
import re

def norm(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s

def split_artist_title(title, artist):
    if artist is None or str(artist) == 'None' or str(artist).strip()=='' or str(artist).strip().lower()=='none':
        if title and ' - ' in str(title):
            a,t = str(title).split(' - ',1)
            return a.strip(), t.strip()
    return artist, title

artists=[]
titles=[]
for t,a in zip(tracks['title'], tracks['artist']):
    a2,t2 = split_artist_title(t,a)
    artists.append(a2)
    titles.append(t2)
tracks['artist_clean']=artists
tracks['title_clean']=titles

tracks['entity_key'] = tracks.apply(lambda r: norm(r['title_clean'])+'||'+norm(r['artist_clean'])+'||'+norm(r['album']) , axis=1)

# join sales with tracks to entity
merged = sales_tot.merge(tracks[['track_id','entity_key','title_clean','artist_clean','album','year']], on='track_id', how='left')

# aggregate revenue by entity_key
ent = merged.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)

top_key = ent.iloc[0]['entity_key']
top_rev = float(ent.iloc[0]['total_revenue_usd'])

# pick representative metadata: most common (mode) among track records for this entity
cand = merged[merged['entity_key']==top_key].merge(tracks[['track_id','title_clean','artist_clean','album','year']], on='track_id', suffixes=('','_t'))
# get from tracks directly for all ids
ids = merged.loc[merged['entity_key']==top_key,'track_id'].unique().tolist()
track_cand = tracks[tracks['track_id'].isin(ids)].copy()

def mode(series):
    s = series.dropna().astype(str)
    s = s[s.str.lower()!='none']
    if len(s)==0:
        return None
    return s.value_counts().idxmax()

rep = {
    'title': mode(track_cand['title_clean']),
    'artist': mode(track_cand['artist_clean']),
    'album': mode(track_cand['album']),
    'year': mode(track_cand['year']),
    'track_ids': ids
}

out = {'title': rep['title'], 'artist': rep['artist'], 'album': rep['album'], 'year': rep['year'], 'total_revenue_usd': round(top_rev,2)}
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_Amb3UFtTUVpQalNE9srLROL4': 'file_storage/call_Amb3UFtTUVpQalNE9srLROL4.json', 'var_call_keZYBZZUAv2FVa7VTZV4bOvB': 'file_storage/call_keZYBZZUAv2FVa7VTZV4bOvB.json'}

exec(code, env_args)
