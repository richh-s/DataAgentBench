code = """import json
# var_call_WpjdMAubwCvjk9OYB8E1CR8B and var_call_8CiDQLmIUms84InXWyFOJ0ue are available from previous tool calls
records = var_call_WpjdMAubwCvjk9OYB8E1CR8B
# Sum revenues (strings) to floats
total = sum(float(r['revenue_usd']) for r in records)
per_track = []
for r in records:
    per_track.append({'track_id': r['track_id'], 'revenue_usd': float(r['revenue_usd'])})
output = {
    'total_revenue_usd': round(total, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'query_track_title': "Get Me Bodied",
    'per_track': per_track
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_8CiDQLmIUms84InXWyFOJ0ue': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_WpjdMAubwCvjk9OYB8E1CR8B': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
