code = """import json
sales = var_call_hKeFKpfXeQFzT0VdDoK5SzAn
total = 0.0
breakdown = []
for r in sales:
    rev = float(r['revenue_usd'])
    total += rev
    breakdown.append({'track_id': r['track_id'], 'revenue_usd': rev})
result = {'total_revenue_usd': round(total, 2), 'currency': 'USD', 'country': 'Canada', 'store': 'Apple Music', 'breakdown': breakdown}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fW9lF4QBPqZgwTzJkOrrPaJb': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_hKeFKpfXeQFzT0VdDoK5SzAn': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '223.82'}]}

exec(code, env_args)
