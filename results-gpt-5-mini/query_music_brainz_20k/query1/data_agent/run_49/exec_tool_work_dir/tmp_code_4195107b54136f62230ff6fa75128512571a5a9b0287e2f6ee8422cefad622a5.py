code = """import json
# variables from previous tool calls: var_call_jgkgihQNUF9A3bIBmIyH1cQO, var_call_SIsvQpJ16RMp27ZJPp0DuXJo
tracks = var_call_jgkgihQNUF9A3bIBmIyH1cQO
sales = var_call_SIsvQpJ16RMp27ZJPp0DuXJo
# Extract track_ids from tracks (ensure integers)
track_ids = []
for t in tracks:
    try:
        track_ids.append(int(t.get('track_id')))
    except Exception:
        pass
# Map sales by track_id to revenue
sales_map = {}
for s in sales:
    try:
        sales_map[int(s.get('track_id'))] = float(s.get('revenue_usd'))
    except Exception:
        pass
# Sum revenue for the track_ids
total = sum(sales_map.get(tid, 0.0) for tid in track_ids)
# Round to 2 decimal places
total_rounded = round(total, 2)
result = {"total_revenue_usd": total_rounded, "currency": "USD", "store": "Apple Music", "country": "Canada", "track_title": "Get Me Bodied", "artist": "Beyoncé"}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jgkgihQNUF9A3bIBmIyH1cQO': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_SIsvQpJ16RMp27ZJPp0DuXJo': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
