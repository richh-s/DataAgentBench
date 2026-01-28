code = """import json
# Access previous query results stored in variables
tracks = var_call_aVeKPm5J5spAIrAOt8lR1020
sales = var_call_SnUleZJVmGv78C5LrVmpUcSx

# Normalize and compute
breakdown = []
total = 0.0
for s in sales:
    # revenue_usd may be string; convert to float
    rev = float(s.get('revenue_usd') or 0)
    total += rev
    breakdown.append({'track_id': str(s.get('track_id')), 'revenue_usd': round(rev, 2)})

# Collect matching track_ids from tracks query
track_ids = [str(t.get('track_id')) for t in tracks]

result = {
    'country': 'Canada',
    'store': 'Apple Music',
    'track_title': "Get Me Bodied",
    'artist': 'Beyoncé',
    'matched_track_ids': track_ids,
    'sales_track_ids': [b['track_id'] for b in breakdown],
    'breakdown': breakdown,
    'total_revenue_usd': round(total, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_aVeKPm5J5spAIrAOt8lR1020': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_SnUleZJVmGv78C5LrVmpUcSx': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354.0', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210.0', 'revenue_usd': '223.82'}]}

exec(code, env_args)
