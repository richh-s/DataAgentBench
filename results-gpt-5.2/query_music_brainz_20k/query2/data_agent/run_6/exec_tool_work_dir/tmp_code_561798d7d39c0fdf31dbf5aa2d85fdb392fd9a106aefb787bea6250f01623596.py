code = """import json, pandas as pd
tracks_main = pd.DataFrame(var_call_RXFteLneQxwpyOjLOtDhg6a5)
tracks_candidates = pd.DataFrame(var_call_s6l7gLTp3Ru28fFCTq1m8klD)
# Entity resolution: include obvious variants: Brucqe vs Bruce, title variations containing 'Street Hype'
# We'll pick all candidate track_ids whose normalized artist matches 'bruce maginnis' after minor spelling fixes.

def norm(s):
    if s is None:
        return ''
    s=str(s).lower().strip()
    # fix common misspelling brucqe->bruce
    s=s.replace('brucqe','bruce')
    s=s.replace('  ',' ')
    return s

tracks_candidates['artist_n']=tracks_candidates['artist'].map(norm)
tracks_candidates['title_n']=tracks_candidates['title'].map(lambda x: norm(x).replace('-',' '))
# keep those with artist bruce maginnis and title contains street hype
mask = tracks_candidates['artist_n'].str.contains('bruce maginnis') & tracks_candidates['title_n'].str.contains('street hype')
resolved = tracks_candidates.loc[mask, ['track_id','title','artist','album','year','length','language']].copy()
track_ids = resolved['track_id'].astype(int).tolist()
print('__RESULT__:')
print(json.dumps({'track_ids': track_ids, 'resolved_records': resolved.to_dict(orient='records')}))"""

env_args = {'var_call_RXFteLneQxwpyOjLOtDhg6a5': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_s6l7gLTp3Ru28fFCTq1m8klD': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}]}

exec(code, env_args)
