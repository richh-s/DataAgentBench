code = """import json
# var_call_okMC9KmbLrOHibjuJMZGmste is available from previous query_db call
rows = var_call_okMC9KmbLrOHibjuJMZGmste
# Sum revenues
total = sum(float(r['revenue_usd']) for r in rows)
track_ids = [r['track_id'] for r in rows]
output = {
    "total_revenue_usd": round(total, 2),
    "currency": "USD",
    "country": "Canada",
    "store": "Apple Music",
    "track_title": "Get Me Bodied",
    "artist": "Beyoncé",
    "track_ids": track_ids,
    "note": "Sum across duplicate track records for the same song"
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_evNWEffEGhW52RboXMVMR70a': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_okMC9KmbLrOHibjuJMZGmste': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
