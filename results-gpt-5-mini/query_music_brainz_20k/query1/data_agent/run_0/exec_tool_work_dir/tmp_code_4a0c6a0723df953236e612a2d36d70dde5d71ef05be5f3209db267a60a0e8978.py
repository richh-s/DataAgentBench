code = """import json
# var_call_IZBzMStH0FlxyHj0y7w2XeKm and var_call_pU7F98IqjHET1OLNooGksZDW are available from previous tool calls
sales = var_call_IZBzMStH0FlxyHj0y7w2XeKm
tracks = var_call_pU7F98IqjHET1OLNooGksZDW

# Parse and sum revenue_usd_sum values
total = 0.0
counted_track_ids = []
for r in sales:
    try:
        val = float(r.get('revenue_usd_sum', 0))
    except:
        val = 0.0
    total += val
    counted_track_ids.append(int(r.get('track_id')))

# Prepare result
result = {
    'total_revenue_usd': round(total, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'counted_track_ids': counted_track_ids,
    'matching_tracks_query_count': len(tracks)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pU7F98IqjHET1OLNooGksZDW': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_IZBzMStH0FlxyHj0y7w2XeKm': [{'track_id': '4233', 'revenue_usd_sum': '377.62'}, {'track_id': '12954', 'revenue_usd_sum': '223.82'}]}

exec(code, env_args)
