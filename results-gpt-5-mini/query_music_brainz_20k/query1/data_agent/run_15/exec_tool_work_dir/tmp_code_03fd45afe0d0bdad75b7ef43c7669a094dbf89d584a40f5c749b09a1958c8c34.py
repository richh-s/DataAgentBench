code = """import json
# var_call_xzjwywH5N4rNwkNmDfU0IoD4 and var_call_yEHGLaRPWMyyPYPw34YVzuCt are available from previous tool calls
sales = var_call_xzjwywH5N4rNwkNmDfU0IoD4
tracks = var_call_yEHGLaRPWMyyPYPw34YVzuCt

total = 0.0
contrib_ids = []
for r in sales:
    try:
        val = float(r.get('revenue_usd', 0))
    except:
        val = 0.0
    total += val
    contrib_ids.append(r.get('track_id'))

matched_track_ids = [t.get('track_id') for t in tracks]

result_obj = {
    'total_revenue_usd': round(total, 2),
    'currency': 'USD',
    'contributing_track_ids': contrib_ids,
    'matched_track_ids': matched_track_ids,
    'notes': "Summed revenue_usd from Apple Music sales in Canada for track_ids linked to 'Get Me Bodied'"
}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_call_yEHGLaRPWMyyPYPw34YVzuCt': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_xzjwywH5N4rNwkNmDfU0IoD4': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '377.62', 'units_sold': '354.0', 'sale_records': '1'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '223.82', 'units_sold': '210.0', 'sale_records': '1'}]}

exec(code, env_args)
