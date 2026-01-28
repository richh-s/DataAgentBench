code = """import json
import pandas as pd

df = pd.DataFrame(var_call_CbZMjOc63Z9a72YMOZYmwkGn)
if df.empty:
    total = 0.0
else:
    df['revenue_usd'] = df['revenue_usd'].astype(float)
    total = df['revenue_usd'].sum()

result = {"total_revenue_usd": round(float(total), 2)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UYfFq8HlaG1oFxUzTA5hJeNx': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_CbZMjOc63Z9a72YMOZYmwkGn': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '223.82'}]}

exec(code, env_args)
