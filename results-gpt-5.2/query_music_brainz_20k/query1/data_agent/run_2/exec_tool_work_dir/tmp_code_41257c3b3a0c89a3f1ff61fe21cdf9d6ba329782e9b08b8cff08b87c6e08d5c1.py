code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_YRBovbEr1sIIdHHvWrXKzKlv)
track_ids = set(tracks['track_id'].astype(int).tolist())

path = var_call_U7gqDZpbB6INCToB8auFUjiC
with open(path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

df = pd.DataFrame(sales)
df['track_id'] = df['track_id'].astype(int)
df['revenue_usd'] = df['revenue_usd'].astype(float)

rev = float(df.loc[df['track_id'].isin(track_ids), 'revenue_usd'].sum())

print('__RESULT__:')
print(json.dumps({'revenue_usd': round(rev, 2), 'track_ids': sorted(list(track_ids))}))"""

env_args = {'var_call_YRBovbEr1sIIdHHvWrXKzKlv': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_U7gqDZpbB6INCToB8auFUjiC': 'file_storage/call_U7gqDZpbB6INCToB8auFUjiC.json'}

exec(code, env_args)
