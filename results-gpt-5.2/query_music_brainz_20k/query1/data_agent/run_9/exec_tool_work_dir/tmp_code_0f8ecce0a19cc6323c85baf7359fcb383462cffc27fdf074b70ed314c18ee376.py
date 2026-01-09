code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_VpSW5lzYdS6DABUL5RsNdRrj)
path_or_list = var_call_RRMXyl7UIETYU0bW271atEG4
if isinstance(path_or_list, str):
    with open(path_or_list, 'r') as f:
        sales = pd.DataFrame(json.load(f))
else:
    sales = pd.DataFrame(path_or_list)

tracks['track_id'] = tracks['track_id'].astype(int)
sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

ids = set(tracks['track_id'].tolist())
revenue = float(sales.loc[sales['track_id'].isin(ids), 'revenue_usd'].sum())

print('__RESULT__:')
print(json.dumps({'track_ids': sorted(list(ids)), 'revenue_usd': round(revenue, 2)}))"""

env_args = {'var_call_VpSW5lzYdS6DABUL5RsNdRrj': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_RRMXyl7UIETYU0bW271atEG4': 'file_storage/call_RRMXyl7UIETYU0bW271atEG4.json'}

exec(code, env_args)
