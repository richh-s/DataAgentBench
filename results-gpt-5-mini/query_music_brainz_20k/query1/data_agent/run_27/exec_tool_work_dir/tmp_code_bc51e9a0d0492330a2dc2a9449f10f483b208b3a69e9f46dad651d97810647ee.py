code = """import json
from collections import Counter

sales = var_call_DOQYhOv92xbqxl3BogEYK8yW
tracks = var_call_ZEl0jJtO7L9CTIodpWpDLyHU

total_revenue = 0.0
total_units = 0
track_ids = set()
for s in sales:
    try:
        total_revenue += float(s.get('revenue_usd', 0))
    except:
        pass
    try:
        total_units += int(s.get('units_sold', 0))
    except:
        pass
    track_ids.add(str(s.get('track_id')))

# derive canonical title/artist from tracks (most common)
titles = [t.get('title') for t in tracks if t.get('title')]
artists = [t.get('artist') for t in tracks if t.get('artist')]
can_title = Counter(titles).most_common(1)[0][0] if titles else None
can_artist = Counter(artists).most_common(1)[0][0] if artists else None

result = {
    'total_revenue_usd': round(total_revenue, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'units_sold': total_units,
    'track_ids': sorted(list(track_ids)),
    'title': can_title,
    'artist': can_artist
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_ZEl0jJtO7L9CTIodpWpDLyHU': [{'track_id': '4233', 'source_id': '1', 'source_track_id': 'WoM13236213', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '12954', 'source_id': '3', 'source_track_id': '28774315MB-01', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'source_id': '4', 'source_track_id': '93213-A07', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_DOQYhOv92xbqxl3BogEYK8yW': [{'sale_id': '12728', 'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '354', 'revenue_usd': '377.62'}, {'sale_id': '38994', 'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '210', 'revenue_usd': '223.82'}]}

exec(code, env_args)
