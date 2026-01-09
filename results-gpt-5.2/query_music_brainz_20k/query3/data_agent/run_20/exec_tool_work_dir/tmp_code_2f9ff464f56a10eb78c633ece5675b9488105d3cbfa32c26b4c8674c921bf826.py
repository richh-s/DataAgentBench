code = """import json, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales_by_track = pd.DataFrame(load(var_call_wEDhsuYn7vd6q7BHMpadMwVZ))
tracks = pd.DataFrame(load(var_call_dkY288CZqa3EyOwulLEIG95r))

# type cleanup
sales_by_track['track_id'] = sales_by_track['track_id'].astype(int)
sales_by_track['total_revenue_usd'] = sales_by_track['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# entity resolution: canonical key based on normalized title+artist (+album when artist missing)
import re

def norm(s):
    if s is None:
        return ''
    s = str(s).strip().lower()
    if s in {'none','null','nan'}:
        return ''
    s = re.sub(r'\s*\(live\)\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r"[^a-z0-9\s']+", ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

tracks['title_n'] = tracks['title'].map(norm)
tracks['artist_n'] = tracks['artist'].map(norm)
tracks['album_n'] = tracks['album'].map(norm)

# If title embeds artist prefix like 'Artist - Title', split heuristically when artist missing
split_mask = (tracks['artist_n'] == '') & tracks['title_n'].str.contains(' - ')
if split_mask.any():
    parts = tracks.loc[split_mask, 'title_n'].str.split(' - ', n=1, expand=True)
    tracks.loc[split_mask, 'artist_n'] = parts[0]
    tracks.loc[split_mask, 'title_n'] = parts[1]

tracks['entity_key'] = tracks['title_n'] + '||' + tracks['artist_n']
# If still no artist, add album to reduce collisions
no_artist = tracks['artist_n'] == ''
tracks.loc[no_artist, 'entity_key'] = tracks.loc[no_artist, 'entity_key'] + '||' + tracks.loc[no_artist, 'album_n']

# join sales with tracks to map entity
df = sales_by_track.merge(tracks[['track_id','title','artist','album','entity_key']], on='track_id', how='left')

# aggregate across duplicates
agg = df.groupby('entity_key', as_index=False).agg(total_revenue_usd=('total_revenue_usd','sum'))
# pick representative metadata: highest-revenue track_id within entity
rep = df.sort_values(['entity_key','total_revenue_usd'], ascending=[True,False]).drop_duplicates('entity_key')
result = agg.merge(rep[['entity_key','title','artist','album']], on='entity_key', how='left')

best = result.sort_values('total_revenue_usd', ascending=False).head(1)
answer_obj = {
    'title': best.iloc[0]['title'],
    'artist': best.iloc[0]['artist'],
    'album': best.iloc[0]['album'],
    'total_revenue_usd': round(float(best.iloc[0]['total_revenue_usd']), 2)
}

print('__RESULT__:')
print(json.dumps(answer_obj, ensure_ascii=False))"""

env_args = {'var_call_wEDhsuYn7vd6q7BHMpadMwVZ': 'file_storage/call_wEDhsuYn7vd6q7BHMpadMwVZ.json', 'var_call_dkY288CZqa3EyOwulLEIG95r': 'file_storage/call_dkY288CZqa3EyOwulLEIG95r.json'}

exec(code, env_args)
