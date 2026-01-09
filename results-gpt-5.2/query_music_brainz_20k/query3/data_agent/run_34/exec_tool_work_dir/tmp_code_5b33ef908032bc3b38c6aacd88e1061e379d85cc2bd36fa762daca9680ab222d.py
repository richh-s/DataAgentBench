code = """import json, pandas as pd, re

with open(var_call_K6pNnJA0y6eEPho7e0x3iJZ4, 'r', encoding='utf-8') as f:
    sales_by_track = json.load(f)
with open(var_call_03vrOZFdUe9s1kZ69WwVJPHI, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

df_sales['track_id'] = df_sales['track_id'].astype(int)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.strip().lower()
    s = s.replace('\u2019','')
    s = s.replace("'",'')
    s = s.replace('"','')
    for ch in ['-','_','/','\\\",':',';','(',')','[',']',',','.','!','?']:
        s = s.replace(ch,' ')
    s = ' '.join(s.split())
    return s

def extract_artist_from_title(title, artist):
    if artist is not None and str(artist).strip() != '' and str(artist).lower() != 'none':
        return artist
    if title is None or str(title).lower() == 'none':
        return artist
    m = re.match(r'^\s*([^\-]{2,}?)\s*-\s*(.+)$', str(title))
    if m:
        return m.group(1).strip()
    return artist

nt = df_tracks.copy()
nt['artist2'] = [extract_artist_from_title(t,a) for t,a in zip(nt['title'], nt['artist'])]
nt['t'] = nt['title'].apply(norm)
nt['a'] = nt['artist'].apply(norm)
nt['a2'] = nt['artist2'].apply(norm)
nt['al'] = nt['album'].apply(norm)
nt['entity_key'] = ['|'.join([t,(a2 if a2 else a),al]) for t,a2,a,al in zip(nt['t'], nt['a2'], nt['a'], nt['al'])]

df = df_sales.merge(nt[['track_id','title','artist','artist2','album','year','entity_key']], on='track_id', how='left')
entity_rev = df.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
top = entity_rev.sort_values('total_revenue_usd', ascending=False).head(1)
entity_key = top.iloc[0]['entity_key']
max_rev = float(top.iloc[0]['total_revenue_usd'])

cand = df[df['entity_key'] == entity_key].copy()
track_rev = cand.groupby('track_id')['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)
top_track_id = int(track_rev.iloc[0]['track_id'])
rep = nt[nt['track_id'] == top_track_id].iloc[0]

artist_out = rep['artist2'] if rep['artist2'] is not None and norm(rep['artist2']) else rep['artist']

answer = {
    'track_id_representative': top_track_id,
    'title': rep['title'],
    'artist': artist_out,
    'album': rep['album'],
    'total_revenue_usd': round(max_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_K6pNnJA0y6eEPho7e0x3iJZ4': 'file_storage/call_K6pNnJA0y6eEPho7e0x3iJZ4.json', 'var_call_03vrOZFdUe9s1kZ69WwVJPHI': 'file_storage/call_03vrOZFdUe9s1kZ69WwVJPHI.json', 'var_call_wpzP1hV7WKhfYIvv2QnuSgoX': [{'n_sales': '58049', 'n_track_ids': '19375'}], 'var_call_iiOtFqlN29Z6OtnFYQImaI5f': [{'n_tracks': '19375', 'n_titles': '18967', 'n_artists': '8994'}]}

exec(code, env_args)
