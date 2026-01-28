code = """import json
import pandas as pd
# var_call_smsKWxFRJ7anS6A79hYBjSOO is available from previous query
df = pd.DataFrame(var_call_smsKWxFRJ7anS6A79hYBjSOO)
# Ensure numeric types
if not df.empty:
    df['total_revenue_usd'] = df['total_revenue_usd'].astype(float)
    df['total_units'] = df['total_units'].astype(float)
    total_revenue = float(df['total_revenue_usd'].sum())
    total_units = int(df['total_units'].sum())
else:
    total_revenue = 0.0
    total_units = 0
result = {
    "song": "Get Me Bodied",
    "artist": "Beyoncé",
    "country": "Canada",
    "store": "Apple Music",
    "total_revenue_usd": round(total_revenue, 2),
    "units_sold": total_units
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_c9jkqeSEcFBhhcfKwZhTY2gK': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_smsKWxFRJ7anS6A79hYBjSOO': [{'track_id': '4233', 'total_revenue_usd': '377.62', 'total_units': '354.0', 'country': 'Canada', 'store': 'Apple Music'}, {'track_id': '12954', 'total_revenue_usd': '223.82', 'total_units': '210.0', 'country': 'Canada', 'store': 'Apple Music'}]}

exec(code, env_args)
