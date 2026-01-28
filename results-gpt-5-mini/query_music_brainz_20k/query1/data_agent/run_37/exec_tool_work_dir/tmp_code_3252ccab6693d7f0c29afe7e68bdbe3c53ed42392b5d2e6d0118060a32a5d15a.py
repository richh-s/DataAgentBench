code = """import json
# Accessing tool results stored in variables
sales = var_call_aT2ofkQCRTOVyaeDvOfhY2xv
tracks = var_call_vGC4D1GnvywoNsxM7q1qy9VT

breakdown = []
total = 0.0
for r in sales:
    # revenue_usd may be string; convert to float
    rev = float(r['revenue_usd'])
    breakdown.append({'track_id': r['track_id'], 'revenue_usd': rev})
    total += rev

result = {'total_revenue_usd': round(total, 2), 'currency': 'USD', 'breakdown': breakdown}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_21xK0L2YWO1o9PwPLbgKtUcI': ['tracks'], 'var_call_o0F7mCr8VBBD4zuqBIdZozni': ['sales'], 'var_call_vGC4D1GnvywoNsxM7q1qy9VT': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_aT2ofkQCRTOVyaeDvOfhY2xv': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
