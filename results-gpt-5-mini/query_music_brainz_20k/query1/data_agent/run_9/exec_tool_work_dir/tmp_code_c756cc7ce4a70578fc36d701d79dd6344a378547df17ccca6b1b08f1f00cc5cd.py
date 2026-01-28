code = """import json
# Accessing previous query results
tracks = var_call_NcjF1s7trgjLZXtyl0wKzzxu
sales = var_call_LevVr69Ghowaww2pQe3O94zZ

# Normalize and pick representative track info for 'Get Me Bodied'
# Find records whose title contains 'get me bodied'
matched_tracks = [t for t in tracks if 'get me bodied' in (t.get('title') or '').lower().replace('-', ' ').replace('_',' ')]
# Collect possible artist names
artist_names = [t.get('artist') for t in matched_tracks if t.get('artist') and t.get('artist').lower() != 'none']
rep_artist = artist_names[0] if artist_names else None
# Choose a representative title (cleaned)
rep_title = 'Get Me Bodied'

# Process sales: sum revenue_usd across returned sales records
total_revenue = 0.0
included_track_ids = []
for s in sales:
    try:
        rev = float(s.get('revenue_usd') or 0)
    except:
        rev = 0.0
    total_revenue += rev
    try:
        included_track_ids.append(int(s.get('track_id')))
    except:
        included_track_ids.append(s.get('track_id'))

result = {
    'track_title': rep_title,
    'artist': rep_artist,
    'country': 'Canada',
    'store': 'Apple Music',
    'total_revenue_usd': round(total_revenue, 2),
    'included_track_ids': included_track_ids
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NcjF1s7trgjLZXtyl0wKzzxu': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '10838', 'source_id': '2', 'source_track_id': 'MBox17886730-HH', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_LevVr69Ghowaww2pQe3O94zZ': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
