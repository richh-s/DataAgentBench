code = """import json
# Access the query results from storage variables
tracks = var_call_HFOpBCqM2nJtazXToN0iqmse
sales = var_call_LBYkzEAXV1Ylf8GvyPFbxVCW

# Convert revenue strings to floats and sum
total = 0.0
track_ids = []
for r in sales:
    try:
        rev = float(r.get('revenue_usd', 0))
    except:
        rev = 0.0
    total += rev
    track_ids.append(int(r.get('track_id')))

# Prepare result dict
result = {
    'country': 'Canada',
    'store': 'Apple Music',
    'query_track_title': "Get Me Bodied",
    'artist': "Beyoncé",
    'matched_track_ids': track_ids,
    'revenue_usd': round(total, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HFOpBCqM2nJtazXToN0iqmse': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '5281', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007', 'length': 'None', 'language': 'English'}, {'track_id': '7588', 'title': 'Feel', 'artist': 'Beyond Surface', 'album': "Destination's End", 'year': '2004', 'length': '205000', 'language': 'Englishh'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15011', 'title': '主題曲 (慢版)', 'artist': 'Beyond', 'album': 'Beyond 25th Anniversary', 'year': '2008', 'length': '171026', 'language': 'Chinese'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_LBYkzEAXV1Ylf8GvyPFbxVCW': [{'track_id': '5281', 'revenue_usd': '458.02'}, {'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
