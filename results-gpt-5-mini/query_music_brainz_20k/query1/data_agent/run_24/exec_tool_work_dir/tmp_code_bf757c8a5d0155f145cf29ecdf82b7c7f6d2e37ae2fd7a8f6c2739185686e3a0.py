code = """import json
# Access the sales query result stored in var_call_wfGNM8RvqH9YHbhaG3IlKob7
data = var_call_wfGNM8RvqH9YHbhaG3IlKob7

# List of track_ids we considered from the tracks query
tracks_considered = [4233, 12954, 15158]

# Sum revenue and units from the sales records (strings in the data)
total_revenue = 0.0
total_units = 0.0
tracks_found = []
for rec in data:
    try:
        revenue = float(rec.get('revenue_usd_sum', 0) or 0)
    except Exception:
        revenue = 0.0
    try:
        units = float(rec.get('units_sold_sum', 0) or 0)
    except Exception:
        units = 0.0
    total_revenue += revenue
    total_units += units
    try:
        tracks_found.append(int(rec.get('track_id')))
    except Exception:
        pass

output = {
    'total_revenue_usd': round(total_revenue, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'tracks_considered': tracks_considered,
    'tracks_found_in_sales': tracks_found,
    'total_units_sold': int(total_units)
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_HPKHxD8qb1HVBrbcvZvl9mxn': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_wfGNM8RvqH9YHbhaG3IlKob7': [{'track_id': '4233', 'revenue_usd_sum': '377.62', 'units_sold_sum': '354.0'}, {'track_id': '12954', 'revenue_usd_sum': '223.82', 'units_sold_sum': '210.0'}]}

exec(code, env_args)
