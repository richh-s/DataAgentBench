code = """import json, pandas as pd

# load full results from storage paths
sales_path = var_call_1OvxUyEPJ2XUC1tSa01vWlzP
tracks_path = var_call_Otgw48tjZXwyK2oLcXre4f2s

with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales)
tracks_df = pd.DataFrame(tracks)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# entity resolution key: normalize title/artist/album/year (very light)
def norm(s):
    if s is None:
        return ''
    s = str(s).strip().lower()
    if s in ('none','null','[unknown]'):
        return ''
    # collapse spaces
    s = ' '.join(s.split())
    return s

def norm_year(y):
    if y is None:
        return ''
    y = str(y).strip()
    if y.lower() in ('none','null',''):
        return ''
    # extract 4-digit year if present
    import re
    m = re.search(r'(19\d{2}|20\d{2})', y)
    if m:
        return m.group(1)
    # handle '11, 05, 75 etc heuristics: treat 2-digit as 19xx if >=30 else 20xx
    m2 = re.search(r"\b(\d{2})\b", y)
    if m2:
        yy = int(m2.group(1))
        return str(1900+yy) if yy>=30 else str(2000+yy)
    return ''

tracks_df['n_title'] = tracks_df['title'].map(norm)
tracks_df['n_artist'] = tracks_df['artist'].map(norm)
tracks_df['n_album'] = tracks_df['album'].map(norm)
tracks_df['n_year'] = tracks_df['year'].map(norm_year)

# build entity key primarily on title+artist, fallback to title+album if artist missing
tracks_df['entity_key'] = tracks_df.apply(lambda r: (r['n_title']+'||'+r['n_artist']) if r['n_artist']!='' else (r['n_title']+'||'+r['n_album']), axis=1)

# join sales to tracks
st = sales_df.merge(tracks_df[['track_id','entity_key','title','artist','album','year']], on='track_id', how='left')

# aggregate revenue by entity
ent = st.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)

top_key = ent.iloc[0]['entity_key']
top_rev = float(ent.iloc[0]['total_revenue_usd'])

# pick representative track metadata: choose row with max individual track revenue among that entity
st_top = st[st['entity_key']==top_key].copy()
per_track = st_top.groupby('track_id')['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)
rep_track_id = int(per_track.iloc[0]['track_id'])
rep = tracks_df[tracks_df['track_id']==rep_track_id].iloc[0]

answer_obj = {
    'track_id_representative': rep_track_id,
    'title': None if pd.isna(rep['title']) else str(rep['title']),
    'artist': None if pd.isna(rep['artist']) else str(rep['artist']),
    'album': None if pd.isna(rep['album']) else str(rep['album']),
    'year': None if pd.isna(rep['year']) else str(rep['year']),
    'total_revenue_usd': round(top_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer_obj))"""

env_args = {'var_call_1OvxUyEPJ2XUC1tSa01vWlzP': 'file_storage/call_1OvxUyEPJ2XUC1tSa01vWlzP.json', 'var_call_Otgw48tjZXwyK2oLcXre4f2s': 'file_storage/call_Otgw48tjZXwyK2oLcXre4f2s.json'}

exec(code, env_args)
