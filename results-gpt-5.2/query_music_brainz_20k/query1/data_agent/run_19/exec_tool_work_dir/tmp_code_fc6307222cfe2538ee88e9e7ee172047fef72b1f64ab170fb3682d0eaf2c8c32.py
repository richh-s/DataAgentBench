code = """import json, pandas as pd

# tracks candidates
tracks = pd.DataFrame(var_call_hkWfYxxZ4rMA1YT5D9HvhIeP)
track_ids = set(tracks['track_id'].astype(int).tolist())

# load canada+apple music revenue by track_id
path = var_call_UH2NYWKyB4qhoONOyYiVUUYZ
with open(path, 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

rev = float(sales.loc[sales['track_id'].isin(track_ids), 'revenue_usd'].sum())

out = {
    'matched_track_ids': sorted(list(track_ids)),
    'revenue_usd': rev
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hkWfYxxZ4rMA1YT5D9HvhIeP': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_dnBDoq5Q824l8EEcvrNbnVFZ': [{'revenue_usd': 'nan'}], 'var_call_UH2NYWKyB4qhoONOyYiVUUYZ': 'file_storage/call_UH2NYWKyB4qhoONOyYiVUUYZ.json'}

exec(code, env_args)
