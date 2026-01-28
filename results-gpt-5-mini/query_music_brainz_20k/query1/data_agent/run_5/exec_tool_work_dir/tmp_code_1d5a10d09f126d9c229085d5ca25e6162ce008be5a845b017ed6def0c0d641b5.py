code = """import json
sales = var_call_vPTN1wCJQBgOs7JMBahDqOLE
tracks = var_call_3OstscQoM3Wtk4TjFiOf1VO4

total = 0.0
breakdown = []
for r in sales:
    rev = float(r.get('revenue_usd') if r.get('revenue_usd') is not None else 0)
    units = float(r.get('units_sold') if r.get('units_sold') is not None else 0)
    tid = r.get('track_id')
    breakdown.append({'track_id': tid, 'revenue_usd': rev, 'units_sold': units})
    total += rev

id_to_title = {t['track_id']: t.get('title') for t in tracks}
for b in breakdown:
    b['title'] = id_to_title.get(b['track_id'])

result = {
    'country': 'Canada',
    'store': 'Apple Music',
    'artist': 'Beyoncé',
    'track_title_query': 'Get Me Bodied',
    'track_ids_considered': [t['track_id'] for t in tracks],
    'breakdown': breakdown,
    'total_revenue_usd': round(total, 2)
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3OstscQoM3Wtk4TjFiOf1VO4': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_vPTN1wCJQBgOs7JMBahDqOLE': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '377.62', 'units_sold': '354.0', 'sales_count': '1'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '223.82', 'units_sold': '210.0', 'sales_count': '1'}]}

exec(code, env_args)
