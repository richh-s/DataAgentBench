code = """import json, pandas as pd

tracks = pd.DataFrame(var_call_GCM0TDa56MLJUCJeU7Pg4mfx)
# sales result stored as a json file path
path = var_call_q3nZiKMnjWC1QGiXzKKIbPWm
with open(path, 'r', encoding='utf-8') as f:
    sales = pd.DataFrame(json.load(f))

# normalize types
tracks['track_id'] = tracks['track_id'].astype(int)
sales['track_id'] = sales['track_id'].astype(int)
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

# entity resolution: the query already narrowed to Beyonce + Get Me Bodied variants; use those track_ids
target_ids = set(tracks['track_id'].tolist())
revenue = float(sales.loc[sales['track_id'].isin(target_ids), 'revenue_usd'].sum())

result = {"revenue_usd": round(revenue, 2), "matched_track_ids": sorted(list(target_ids)), "num_sales_rows": int(sales.loc[sales['track_id'].isin(target_ids)].shape[0])}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GCM0TDa56MLJUCJeU7Pg4mfx': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_q3nZiKMnjWC1QGiXzKKIbPWm': 'file_storage/call_q3nZiKMnjWC1QGiXzKKIbPWm.json'}

exec(code, env_args)
