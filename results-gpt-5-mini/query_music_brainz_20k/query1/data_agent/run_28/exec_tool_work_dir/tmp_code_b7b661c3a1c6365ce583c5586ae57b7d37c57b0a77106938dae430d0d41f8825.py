code = """import json
# var_call_uKSRkSi1lADWybT86RTvldkO and var_call_SvCgDyWBx7xyIW16A4i6Vc5M are available from previous tool calls
tracks = var_call_uKSRkSi1lADWybT86RTvldkO
sales = var_call_SvCgDyWBx7xyIW16A4i6Vc5M

# Collect resolved track_ids from tracks query
resolved_ids = []
for r in tracks:
    try:
        resolved_ids.append(int(r['track_id']))
    except:
        pass

# Sum revenues from sales results
total_revenue = 0.0
sales_ids = []
for s in sales:
    try:
        val = float(s.get('revenue', 0))
    except:
        val = 0.0
    total_revenue += val
    try:
        sales_ids.append(int(s['track_id']))
    except:
        pass

result_obj = {
    'track_title': "Get Me Bodied",
    'artist': "Beyoncé",
    'country': "Canada",
    'store': "Apple Music",
    'revenue_usd': round(total_revenue, 2),
    'currency': "USD",
    'resolved_track_ids': resolved_ids,
    'sales_track_ids': sales_ids
}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_call_uKSRkSi1lADWybT86RTvldkO': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_SvCgDyWBx7xyIW16A4i6Vc5M': [{'track_id': '4233', 'revenue': '377.62'}, {'track_id': '12954', 'revenue': '223.82'}]}

exec(code, env_args)
