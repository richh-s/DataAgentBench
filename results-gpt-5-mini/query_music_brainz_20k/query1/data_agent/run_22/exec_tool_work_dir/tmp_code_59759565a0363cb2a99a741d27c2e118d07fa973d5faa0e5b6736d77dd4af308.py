code = """import json
records = var_call_ePdkx6wDyGEgP7kgmke4ej5U
# Sum revenue_usd values, converting to float
total = sum(float(r['revenue_usd']) for r in records)
# Round to 2 decimal places
total = round(total, 2)
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_TLkq9xK18iI519YOQGwVNWHX': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_ePdkx6wDyGEgP7kgmke4ej5U': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
