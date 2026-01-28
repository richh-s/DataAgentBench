code = """import json, pandas as pd

tracks1 = pd.DataFrame(var_call_30ASuJ9Spwmlje6vAlmzfXsy)
tracks2 = pd.DataFrame(var_call_aakQGcmW0qOP78o9pNwOgN8q)

df = pd.concat([tracks1, tracks2], ignore_index=True).drop_duplicates(subset=['track_id'])
# Entity resolution: keep those that appear to be same song by Brucqe/Bruce Maginnis and title containing street hype
# normalize
for col in ['title','artist','album','year','length','language']:
    if col in df.columns:
        df[col] = df[col].astype(str)

df['artist_n'] = df['artist'].str.lower().str.replace(r'[^a-z0-9 ]+','', regex=True).str.replace('  ',' ', regex=False).str.strip()
df['title_n'] = df['title'].str.lower().str.replace(r'[^a-z0-9 ]+','', regex=True).str.replace('  ',' ', regex=False).str.strip()

def is_target(row):
    # accept brucqe/bruce maginnis typos
    if 'maginnis' not in row['artist_n']:
        return False
    if 'street hype' not in row['title_n']:
        return False
    return True

resolved = df[df.apply(is_target, axis=1)].copy()
track_ids = sorted(resolved['track_id'].astype(int).unique().tolist())

print('__RESULT__:')
print(json.dumps({'track_ids': track_ids, 'resolved_tracks': resolved[['track_id','title','artist','album','year','length','language']].to_dict(orient='records')}))"""

env_args = {'var_call_30ASuJ9Spwmlje6vAlmzfXsy': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_aakQGcmW0qOP78o9pNwOgN8q': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}]}

exec(code, env_args)
