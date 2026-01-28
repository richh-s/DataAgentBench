code = """import json
# var_call_OeBI0dS7Q2Ni0TKqRFMgmQtQ is available from previous query
sales = var_call_OeBI0dS7Q2Ni0TKqRFMgmQtQ
# Sum revenue_usd values, converting to float
total = 0.0
for r in sales:
    try:
        total += float(r.get('revenue_usd', 0))
    except:
        # if value is None or non-convertible, treat as 0
        pass
# Round to 2 decimal places
total_rounded = round(total, 2)
result = {"total_revenue_usd": total_rounded, "currency": "USD", "country": "Canada", "store": "Apple Music", "track_title_query": "Get Me Bodied", "artist": "Beyonc\u00e9"}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EqJC4sUiycV7xUrmuEwPHRa2': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_OeBI0dS7Q2Ni0TKqRFMgmQtQ': [{'track_id': '4233', 'sale_id': '12728', 'units_sold': '354', 'revenue_usd': '377.62', 'country': 'Canada', 'store': 'Apple Music'}, {'track_id': '12954', 'sale_id': '38994', 'units_sold': '210', 'revenue_usd': '223.82', 'country': 'Canada', 'store': 'Apple Music'}]}

exec(code, env_args)
