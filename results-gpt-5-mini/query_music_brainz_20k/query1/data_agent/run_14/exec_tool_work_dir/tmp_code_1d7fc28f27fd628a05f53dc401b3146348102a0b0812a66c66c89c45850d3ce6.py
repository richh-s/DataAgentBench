code = """import json
# var_call_SNqmzCdV7cHegLInBVV4WlHa contains track records
# var_call_KbxaeO6dgCSAob1o2ku2PtlS contains sales aggregation for Canada Apple Music
tracks = var_call_SNqmzCdV7cHegLInBVV4WlHa
sales = var_call_KbxaeO6dgCSAob1o2ku2PtlS

# Sum revenue_usd from sales records, converting strings to floats
total_revenue = 0.0
for r in sales:
    try:
        total_revenue += float(r.get('revenue_usd', 0) or 0)
    except Exception:
        # If value isn't parseable, skip or treat as 0
        continue

# Round to 2 decimals
total_revenue = round(total_revenue, 2)

result = {
    'total_revenue_usd': total_revenue,
    'currency': 'USD',
    'store': 'Apple Music',
    'country': 'Canada',
    'track_title_query': "Get Me Bodied",
    'artist_query': "Beyoncé",
    'matched_track_ids': [t.get('track_id') for t in tracks],
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SNqmzCdV7cHegLInBVV4WlHa': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown'}], 'var_call_KbxaeO6dgCSAob1o2ku2PtlS': [{'track_id': '4233', 'units_sold': '354.0', 'revenue_usd': '377.62'}, {'track_id': '12954', 'units_sold': '210.0', 'revenue_usd': '223.82'}]}

exec(code, env_args)
