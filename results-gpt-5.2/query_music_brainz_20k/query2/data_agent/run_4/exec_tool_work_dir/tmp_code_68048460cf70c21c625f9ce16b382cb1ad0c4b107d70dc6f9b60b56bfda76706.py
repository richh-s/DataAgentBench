code = """import json, pandas as pd, re

tracks_all = pd.DataFrame(var_call_HyEcg2PRIL7j2yYYU7tZdaeh)

# Entity resolution: include obvious variants (Brucqe/Bruce) and title variants that include 'Street Hype'
# Filter to records where normalized artist is close to 'bruce maginnis'

def norm(s):
    if s is None:
        return ''
    s = str(s).lower().strip()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

tracks_all['artist_n'] = tracks_all['artist'].map(norm)
tracks_all['title_n'] = tracks_all['title'].map(norm)

# Accept both 'brucqe' typo and 'bruce'
mask_artist = tracks_all['artist_n'].str.contains(r"brucq?e") & tracks_all['artist_n'].str.contains('maginnis')
mask_title = tracks_all['title_n'].str.contains('street') & tracks_all['title_n'].str.contains('hype')

resolved = tracks_all[mask_artist & mask_title].copy()
track_ids = resolved['track_id'].astype(int).tolist()

out = {"track_ids": track_ids, "resolved_tracks": resolved.drop(columns=['artist_n','title_n']).to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_r82yne3HFZ1u8R5gvphVWV7k': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_HyEcg2PRIL7j2yYYU7tZdaeh': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}]}

exec(code, env_args)
