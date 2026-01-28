code = """import json
tracks = var_call_cDgGn9gRA7KaQrAk9sG3cfu0
sales = var_call_oyfqKbGmaEfR8p08ak3IuQyg
indiv = {}
total = 0.0
for r in sales:
    tid = int(r['track_id'])
    rev = float(r['revenue_usd_sum'])
    indiv[str(tid)] = rev
    total += rev
all_track_ids = [int(t['track_id']) for t in tracks]
contributing = [int(k) for k in indiv.keys()]
result = {
    "track_title": "Get Me Bodied",
    "artist": "Beyoncé",
    "country": "Canada",
    "store": "Apple Music",
    "total_revenue_usd": round(total, 2),
    "currency": "USD",
    "all_track_ids_considered": all_track_ids,
    "contributing_track_ids": contributing,
    "individual_revenues": {k: round(v,2) for k,v in indiv.items()}
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cDgGn9gRA7KaQrAk9sG3cfu0': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '5281', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_oyfqKbGmaEfR8p08ak3IuQyg': [{'track_id': '5281', 'revenue_usd_sum': '458.02'}, {'track_id': '4233', 'revenue_usd_sum': '377.62'}, {'track_id': '12954', 'revenue_usd_sum': '223.82'}]}

exec(code, env_args)
