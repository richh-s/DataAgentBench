code = """import json

sales = var_call_67I73oKIfU1fT6GHSKNnv6Rx
tracks = var_call_IUZjj8IotT9tdYqOlNW0IRBy

track_ids = [r['track_id'] for r in tracks]

total = sum(float(s['revenue_usd']) for s in sales)
breakdown = [{'sale_id': s['sale_id'], 'track_id': s['track_id'], 'revenue_usd': float(s['revenue_usd'])} for s in sales]

result = {'total_revenue_usd': round(total, 2), 'currency': 'USD', 'country': 'Canada', 'store': 'Apple Music', 'track_title': 'Get Me Bodied', 'artist': 'Beyoncé', 'track_ids': track_ids, 'sales_breakdown': breakdown}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_IUZjj8IotT9tdYqOlNW0IRBy': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '5281', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007', 'length': 'None', 'language': 'English'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_67I73oKIfU1fT6GHSKNnv6Rx': [{'sale_id': '12728', 'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354', 'revenue_usd': '377.62'}, {'sale_id': '15801', 'track_id': '5281', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '426', 'revenue_usd': '458.02'}, {'sale_id': '38994', 'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210', 'revenue_usd': '223.82'}]}

exec(code, env_args)
