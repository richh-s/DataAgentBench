code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_bYaLJNfDQF8VdixaJP3PIFuv)
track_ids = set(tracks['track_id'].astype(int).tolist())

# load full sales result from json file
path = var_call_jaB6Rl0Mhi0yED3dCoo0TJw2
with open(path, 'r', encoding='utf-8') as f:
    sales_records = json.load(f)

sales = pd.DataFrame(sales_records)
# cast
sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

revenue = float(sales.loc[sales['track_id'].isin(track_ids), 'revenue_usd'].sum())

out = {
    'track_ids_matched': sorted(list(track_ids)),
    'revenue_usd': round(revenue, 2)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bYaLJNfDQF8VdixaJP3PIFuv': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_jaB6Rl0Mhi0yED3dCoo0TJw2': 'file_storage/call_jaB6Rl0Mhi0yED3dCoo0TJw2.json'}

exec(code, env_args)
