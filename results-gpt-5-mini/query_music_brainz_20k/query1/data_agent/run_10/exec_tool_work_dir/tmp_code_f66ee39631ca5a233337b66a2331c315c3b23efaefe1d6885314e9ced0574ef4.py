code = """import json

# Data from previous query_db calls
tracks = var_call_qTOzYSjttxsgNXWCHN5ngotB
sales = var_call_8KMG0spkibnOQnchY0aFVFXH

# Sum revenue_usd_sum from sales records (strings) into float
total = 0.0
for r in sales:
    try:
        total += float(r.get('revenue_usd_sum', 0))
    except:
        # if already numeric
        total += r.get('revenue_usd_sum', 0)

# Format result
result_str = f"Apple Music revenue in Canada for Beyoncé's 'Get Me Bodied' is ${total:.2f} USD."

print("__RESULT__:")
print(json.dumps(result_str))"""

env_args = {'var_call_qTOzYSjttxsgNXWCHN5ngotB': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_8KMG0spkibnOQnchY0aFVFXH': [{'track_id': '4233', 'revenue_usd_sum': '377.62'}, {'track_id': '12954', 'revenue_usd_sum': '223.82'}]}

exec(code, env_args)
