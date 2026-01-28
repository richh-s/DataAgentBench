code = """import json

sales = var_call_A3qVjQKvU9j3T2p3BBGcjJPc
tracks = var_call_TKmcTWD7ZI0I3tTo7T0rcIJ6

# Convert revenue and units to numeric and sum
total_revenue = 0.0
total_units = 0
breakdown = []
for r in sales:
    try:
        rev = float(r.get('revenue_usd', 0) if r.get('revenue_usd') is not None else 0)
    except:
        rev = 0.0
    try:
        units = int(float(r.get('units_sold', 0) if r.get('units_sold') is not None else 0))
    except:
        units = 0
    total_revenue += rev
    total_units += units
    breakdown.append({'track_id': r.get('track_id'), 'units_sold': units, 'revenue_usd': round(rev, 2)})

# Check if any tracks matched but had no sales
track_ids = [t.get('track_id') for t in tracks]
sales_track_ids = [r.get('track_id') for r in sales]
missing_track_ids = [tid for tid in track_ids if tid not in sales_track_ids]

result = {
    'query': "Apple Music revenue for Beyoncé - 'Get Me Bodied' in Canada",
    'country': 'Canada',
    'store': 'Apple Music',
    'artist': 'Beyoncé',
    'title_search': 'Get Me Bodied',
    'matched_track_ids': track_ids,
    'sales_track_ids': sales_track_ids,
    'missing_track_ids': missing_track_ids,
    'total_units_sold': total_units,
    'total_revenue_usd': round(total_revenue, 2),
    'breakdown': breakdown
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TKmcTWD7ZI0I3tTo7T0rcIJ6': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_A3qVjQKvU9j3T2p3BBGcjJPc': [{'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210.0', 'revenue_usd': '223.82'}, {'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354.0', 'revenue_usd': '377.62'}]}

exec(code, env_args)
