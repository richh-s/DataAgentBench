code = """import json
# var_call_0d5NMzyM5mIKrKuzIUBdQCtm and var_call_9oY17bcPHnbJ3pXyEcvggLB8 are available from previous tool calls
sales = var_call_9oY17bcPHnbJ3pXyEcvggLB8
# Compute total revenue
total = sum(float(r['revenue_usd']) for r in sales)
# Prepare per-track details
per_track = [{'track_id': r['track_id'], 'revenue_usd': float(r['revenue_usd'])} for r in sales]
result = {'total_revenue_usd': round(total, 2), 'currency': 'USD', 'country': 'Canada', 'store': 'Apple Music', 'track_title': "Get Me Bodied", 'artist': 'Beyoncé', 'track_ids': [r['track_id'] for r in sales], 'per_track': per_track}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0d5NMzyM5mIKrKuzIUBdQCtm': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_9oY17bcPHnbJ3pXyEcvggLB8': [{'track_id': '12954', 'revenue_usd': '223.82'}, {'track_id': '4233', 'revenue_usd': '377.62'}]}

exec(code, env_args)
