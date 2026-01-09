code = """import json, pandas as pd
tracks1 = pd.DataFrame(var_call_ypcgyPKabYhfo4CXNgnrjU0Z)
tracks2 = pd.DataFrame(var_call_nURKjROSzLRhiaqs38e1m1D4)
df = pd.concat([tracks1, tracks2], ignore_index=True).drop_duplicates(subset=['track_id'])
# entity resolution: keep records that look like same song: title contains 'street hype' and artist resembles brucq(e)/bruce maginnis
cand = df[df['title'].str.lower().str.contains('street hype') & df['artist'].str.lower().str.contains('maginnis')].copy()
track_ids = sorted({int(x) for x in cand['track_id'].tolist()})
print('__RESULT__:')
print(json.dumps({'track_ids': track_ids, 'candidates': cand.to_dict(orient='records')}))"""

env_args = {'var_call_ypcgyPKabYhfo4CXNgnrjU0Z': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_nURKjROSzLRhiaqs38e1m1D4': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}]}

exec(code, env_args)
