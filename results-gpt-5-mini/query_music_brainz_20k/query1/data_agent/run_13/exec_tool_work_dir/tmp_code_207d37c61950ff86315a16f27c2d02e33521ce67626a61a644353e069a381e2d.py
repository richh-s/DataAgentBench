code = """import json
# Accessing previous query results
tracks = var_call_rQqMt4OGDYlsFbAcromPI8yK
sales = var_call_TSoRYmVuql0pHNZJTf8asXcj

# Normalize and compute total revenue for the matching sales
total_revenue = 0.0
revenue_by_track = {}
for s in sales:
    try:
        rev = float(s.get('revenue_usd', 0) or 0)
    except:
        rev = 0.0
    tid = int(s.get('track_id')) if s.get('track_id') is not None else None
    total_revenue += rev
    revenue_by_track.setdefault(tid, 0.0)
    revenue_by_track[tid] += rev

# Collect track ids and a representative title/artist
track_ids = []
for t in tracks:
    try:
        track_ids.append(int(t.get('track_id')))
    except:
        pass

rep_title = tracks[0].get('title') if tracks else None
rep_artist = tracks[0].get('artist') if tracks else None

result = {
    'total_revenue_usd': round(total_revenue, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'track_title_sample': rep_title,
    'artist_sample': rep_artist,
    'track_ids_considered': track_ids,
    'revenue_by_track': {str(k): round(v,2) for k,v in revenue_by_track.items()}
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rQqMt4OGDYlsFbAcromPI8yK': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_TSoRYmVuql0pHNZJTf8asXcj': [{'sale_id': '12728', 'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354', 'revenue_usd': '377.62'}, {'sale_id': '38994', 'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210', 'revenue_usd': '223.82'}]}

exec(code, env_args)
