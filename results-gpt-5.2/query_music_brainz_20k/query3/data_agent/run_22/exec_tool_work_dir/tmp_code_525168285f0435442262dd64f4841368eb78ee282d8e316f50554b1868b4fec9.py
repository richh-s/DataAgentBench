code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

sales = pd.DataFrame(load_records(var_call_aVs1nZtsjA1twQHxRsC9cMqm))
tracks = pd.DataFrame(load_records(var_call_LVXNuLIFLRUzWL4ldZum2XV1))

# types
sales['track_id'] = sales['track_id'].astype(int)
sales['total_revenue_usd'] = sales['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# simple entity resolution key: normalized (title, artist) with some cleanup

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s*\([^)]*\)", "", s)  # drop parenthetical
    s = re.sub(r"\s*-\s*.*$", "", s)      # drop after dash (often extra info)
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

tracks['title_n'] = tracks['title'].apply(norm)
tracks['artist_n'] = tracks['artist'].apply(norm)
tracks['entity_key'] = (tracks['title_n'] + '||' + tracks['artist_n']).str.strip('|')

# join sales to track metadata
st = sales.merge(tracks[['track_id','title','artist','album','year','entity_key','title_n','artist_n']], on='track_id', how='left')

# aggregate by entity_key (fallback to track_id if key empty)
st['entity_key2'] = st.apply(lambda r: r['entity_key'] if isinstance(r['entity_key'], str) and len(r['entity_key'])>2 else f"track_id::{int(r['track_id'])}", axis=1)
agg = st.groupby('entity_key2', as_index=False)['total_revenue_usd'].sum()
agg = agg.sort_values('total_revenue_usd', ascending=False)

top_key = agg.iloc[0]['entity_key2']
top_rev = float(agg.iloc[0]['total_revenue_usd'])

# representative metadata: choose track_id with max revenue within this entity
sub = st[st['entity_key2']==top_key].copy()
# compute per track within entity
per_track = sub.groupby('track_id', as_index=False)['total_revenue_usd'].sum().sort_values('total_revenue_usd', ascending=False)
rep_track_id = int(per_track.iloc[0]['track_id'])
rep = tracks[tracks['track_id']==rep_track_id].iloc[0].to_dict()

result = {
    'track_id_representative': rep_track_id,
    'title': rep.get('title'),
    'artist': rep.get('artist'),
    'album': rep.get('album'),
    'year': rep.get('year'),
    'total_revenue_usd_all_stores_countries': round(top_rev, 2),
    'entity_key_used': top_key,
    'num_track_ids_merged': int(sub['track_id'].nunique())
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_aVs1nZtsjA1twQHxRsC9cMqm': 'file_storage/call_aVs1nZtsjA1twQHxRsC9cMqm.json', 'var_call_LVXNuLIFLRUzWL4ldZum2XV1': 'file_storage/call_LVXNuLIFLRUzWL4ldZum2XV1.json'}

exec(code, env_args)
