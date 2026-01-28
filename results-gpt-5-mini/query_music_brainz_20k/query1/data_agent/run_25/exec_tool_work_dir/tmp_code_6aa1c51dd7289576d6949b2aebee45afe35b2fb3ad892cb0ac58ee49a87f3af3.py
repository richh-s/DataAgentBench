code = """import json

tracks = var_call_mC6lAUcvOdMGAMXHZ2EN6Due
sales = var_call_HirMLiAtJgFOtv8EzUyLLqXs

# collect track_ids from tracks query
track_ids = set([t['track_id'] for t in tracks])

# build revenue map from sales
revenue_map = {}
for s in sales:
    tid = s['track_id']
    try:
        rev = float(s['revenue_usd'])
    except Exception:
        rev = 0.0
    revenue_map[tid] = revenue_map.get(tid, 0.0) + rev

# ensure all track_ids present
for tid in track_ids:
    revenue_map.setdefault(tid, 0.0)

total_revenue = sum(revenue_map[tid] for tid in track_ids)

result = {
    'track_title_query': "Get Me Bodied",
    'artist_query': "Beyoncé",
    'country': 'Canada',
    'store': 'Apple Music',
    'track_ids_considered': sorted(list(track_ids)),
    'revenue_by_track_id': {tid: round(revenue_map[tid], 2) for tid in sorted(revenue_map.keys())},
    'total_revenue_usd': round(total_revenue, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mC6lAUcvOdMGAMXHZ2EN6Due': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_HirMLiAtJgFOtv8EzUyLLqXs': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
