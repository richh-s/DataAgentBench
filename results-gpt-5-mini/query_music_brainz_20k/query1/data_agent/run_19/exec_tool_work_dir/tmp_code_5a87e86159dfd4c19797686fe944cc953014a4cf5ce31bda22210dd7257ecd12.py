code = """import json
# Data from previous queries
tracks = var_call_ch3gBdhgzamHlL2CojflkGJ3
sales = var_call_Imb5FMZRpipZDLt0K34Yvod0

# Sum revenues (they may be strings)
total = 0.0
for r in sales:
    try:
        total += float(r.get('revenue_usd', 0))
    except Exception:
        # if value is None or non-numeric, skip
        pass

# Prepare result
track_ids = [r.get('track_id') for r in sales]
result = {
    "total_revenue_usd": round(total, 2),
    "currency": "USD",
    "country": "Canada",
    "store": "Apple Music",
    "track_title": "Get Me Bodied",
    "artist": "Beyoncé",
    "matched_track_ids": track_ids
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ch3gBdhgzamHlL2CojflkGJ3': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_Imb5FMZRpipZDLt0K34Yvod0': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '377.62'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '223.82'}]}

exec(code, env_args)
