code = """import json
sales_data = [{"track_id": "4233", "country": "Canada", "store": "Apple Music", "units_sold": "354", "revenue_usd": "377.62"}, {"track_id": "12954", "country": "Canada", "store": "Apple Music", "units_sold": "210", "revenue_usd": "223.82"}]

# Calculate total revenue in USD
total_revenue_usd = sum(float(sale["revenue_usd"]) for sale in sales_data)
print("__RESULT__:")
print(json.dumps(round(total_revenue_usd, 2)))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_functions.query_db:2': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210', 'revenue_usd': '223.82'}]}

exec(code, env_args)
