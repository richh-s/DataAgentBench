code = """import json

# Get the sales data from the previous query
sales_data = [
    {"sale_id": "12728", "track_id": "4233", "country": "Canada", "store": "Apple Music", "units_sold": "354", "revenue_usd": "377.62"},
    {"sale_id": "38994", "track_id": "12954", "country": "Canada", "store": "Apple Music", "units_sold": "210", "revenue_usd": "223.82"}
]

# Calculate total revenue in USD
total_revenue = sum(float(sale["revenue_usd"]) for sale in sales_data)

print('__RESULT__:')
print(json.dumps({"total_revenue_usd": round(total_revenue, 2)}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_functions.query_db:4': [{'sale_id': '12728', 'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354', 'revenue_usd': '377.62'}, {'sale_id': '38994', 'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210', 'revenue_usd': '223.82'}]}

exec(code, env_args)
