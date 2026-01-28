code = """import json
# Accessing previous query results stored in variables
records = var_call_v3eevPQ83h7ORR1BLWIKkGcD
# records is a list of dicts with keys: track_id, revenue_usd_sum, sales_count
breakdown = []
total = 0.0
for r in records:
    rev = float(r['revenue_usd_sum'])
    breakdown.append({'track_id': r['track_id'], 'revenue_usd': rev, 'sales_count': int(r['sales_count'])})
    total += rev
# Prepare result dict
result = {
    'total_revenue_usd': round(total, 2),
    'currency': 'USD',
    'store': 'Apple Music',
    'country': 'Canada',
    'track_title': "Get Me Bodied",
    'artist': "Beyoncé",
    'breakdown_by_track_id': breakdown
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CYyZUQpCUqqxLNDi2iQLcJ4e': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '5281', 'source_id': '5', 'source_track_id': '6618097', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007', 'length': 'None', 'language': 'English'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_v3eevPQ83h7ORR1BLWIKkGcD': [{'track_id': '5281', 'revenue_usd_sum': '458.02', 'sales_count': '1'}, {'track_id': '12954', 'revenue_usd_sum': '223.82', 'sales_count': '1'}, {'track_id': '4233', 'revenue_usd_sum': '377.62', 'sales_count': '1'}]}

exec(code, env_args)
