code = """import json

# var_call_zBq4EdopK1OEBDKqrK3FDI2Q and var_call_HXUnJIqEmKoANlsYdUid1m4J are available from previous tool calls
records = var_call_zBq4EdopK1OEBDKqrK3FDI2Q

total = sum(float(r['revenue_usd']) for r in records)

breakdown = []
for r in records:
    breakdown.append({
        'track_id': int(r['track_id']),
        'units_sold': float(r['units_sold']),
        'revenue_usd': float(r['revenue_usd'])
    })

result = {
    'song_title': "Get Me Bodied",
    'artist': "Beyoncé",
    'country': "Canada",
    'store': "Apple Music",
    'total_revenue_usd': total,
    'breakdown': breakdown
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HXUnJIqEmKoANlsYdUid1m4J': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_zBq4EdopK1OEBDKqrK3FDI2Q': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354.0', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210.0', 'revenue_usd': '223.82'}]}

exec(code, env_args)
