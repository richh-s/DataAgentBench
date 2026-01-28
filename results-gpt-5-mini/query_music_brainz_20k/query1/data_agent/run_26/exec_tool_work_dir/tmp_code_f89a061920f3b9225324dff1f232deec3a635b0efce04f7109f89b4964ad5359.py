code = """import json
# sales data from filtered query
sales = var_call_WC9M3ZmiMr6Dp3kqlXiFrhz3
# sum revenue_usd values (strings) to float
total = sum(float(r['revenue_usd']) for r in sales)
# prepare output
output = {
    "total_revenue_usd": round(total, 2),
    "currency": "USD",
    "store": "Apple Music",
    "country": "Canada",
    "track_title": "Get Me Bodied",
    "artist": "Beyonc\u00e9"
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_eAu20Z5nc9zlyA41I5sDTOcM': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_D2c8eNUAIRAQzasK8wC0c1jI': 'file_storage/call_D2c8eNUAIRAQzasK8wC0c1jI.json', 'var_call_WC9M3ZmiMr6Dp3kqlXiFrhz3': [{'sale_id': '12728', 'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354', 'revenue_usd': '377.62'}, {'sale_id': '38994', 'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210', 'revenue_usd': '223.82'}]}

exec(code, env_args)
