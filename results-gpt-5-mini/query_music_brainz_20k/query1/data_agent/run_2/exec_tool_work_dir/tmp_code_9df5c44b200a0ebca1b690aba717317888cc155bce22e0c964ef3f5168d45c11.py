code = """import json
# Access previous query results
tracks = var_call_Ndi1LvULhelbIqLruYodK7m4
sales = var_call_PUhj1f7WAzEVngihZbtQIjSV

# Identify resolved track ids for Beyoncé's 'Get Me Bodied' by matching title and artist heuristically
resolved_track_ids = []
for t in tracks:
    title = (t.get('title') or '').lower()
    artist = (t.get('artist') or '').lower()
    if 'get me bodied' in title and ('beyonc' in artist or 'beyonce' in artist):
        resolved_track_ids.append(t.get('track_id'))
# If artist missing but title matches, also include
for t in tracks:
    title = (t.get('title') or '').lower()
    artist = (t.get('artist') or '').lower()
    if 'get me bodied' in title and t.get('track_id') not in resolved_track_ids:
        resolved_track_ids.append(t.get('track_id'))

# Sum revenue_usd from sales for these resolved track ids
total = 0.0
included_sales = []
for s in sales:
    if s.get('track_id') in resolved_track_ids:
        try:
            total += float(s.get('revenue_usd') or 0)
            included_sales.append(s)
        except:
            pass

# Prepare result
result_obj = {
    'total_revenue_usd': round(total, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'resolved_track_ids': resolved_track_ids,
    'sales_track_ids_included': [s.get('track_id') for s in included_sales]
}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_call_Ndi1LvULhelbIqLruYodK7m4': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_PUhj1f7WAzEVngihZbtQIjSV': [{'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210.0', 'revenue_usd': '223.82'}, {'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354.0', 'revenue_usd': '377.62'}]}

exec(code, env_args)
