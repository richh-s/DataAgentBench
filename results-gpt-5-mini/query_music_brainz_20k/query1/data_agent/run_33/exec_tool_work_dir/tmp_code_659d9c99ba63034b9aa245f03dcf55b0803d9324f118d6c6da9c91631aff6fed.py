code = """import json

# Access previous tool results
tracks = var_call_zhzwFb3DrsXe2g1yJ9Z8WnGY
sales = var_call_ZJdqUvFv5lcenCwXWtU29PzK

# Extract matched track ids from tracks result
matched_track_ids = [r['track_id'] for r in tracks]

# Create a dict for sales by track_id and compute total
total = 0.0
sales_by_id = {}
for r in sales:
    tid = r['track_id']
    rev = float(r['revenue_usd'])
    sales_by_id[tid] = rev
    total += rev

# For clarity, list which of the matched track ids had sales
matched_with_sales = [tid for tid in matched_track_ids if tid in sales_by_id]

result = {
    'song_title': "Get Me Bodied",
    'artist': "Beyoncé",
    'country': "Canada",
    'store': "Apple Music",
    'matched_track_ids': matched_track_ids,
    'matched_track_ids_with_sales': matched_with_sales,
    'revenue_usd': round(total, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zhzwFb3DrsXe2g1yJ9Z8WnGY': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '5281', 'source_id': '5', 'source_track_id': '6618097', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007', 'length': 'None', 'language': 'English'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_ZJdqUvFv5lcenCwXWtU29PzK': [{'track_id': '5281', 'revenue_usd': '458.02'}, {'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
