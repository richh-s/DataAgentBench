code = """import json
tracks = var_call_UqreygN3efJyigmVuY7Jf8CV
sales = var_call_TK79iXAU87hNI1szkJmFXGIP
# extract track_ids from tracks results (they are strings in the records)
track_ids = [int(r['track_id']) for r in tracks]
# build map of revenues from sales results
sales_map = {int(r['track_id']): float(r['revenue_usd']) for r in sales}
# sum revenues for the resolved track IDs
total = sum(sales_map.get(tid, 0.0) for tid in track_ids)
# round to 2 decimals
total = round(total, 2)
result = json.dumps({
    "total_revenue_usd": total,
    "currency": "USD",
    "country": "Canada",
    "store": "Apple Music",
    "track_title": "Get Me Bodied",
    "artist": "Beyoncé",
    "resolved_track_ids": track_ids
})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_UqreygN3efJyigmVuY7Jf8CV': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_TK79iXAU87hNI1szkJmFXGIP': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
