code = """import json
import re

tracks = var_call_x3p4JXP8ddyjoULtTMXRdMVZ
sales = var_call_vC56BH2AkQuGrHfUYObdB9js

# Normalize and match titles that represent 'Get Me Bodied'
matched_ids = set()
for t in tracks:
    tid = str(t.get('track_id'))
    title = str(t.get('title') or '').lower()
    # remove accents
    try:
        import unicodedata
        title_norm = unicodedata.normalize('NFKD', title)
        title_norm = ''.join([c for c in title_norm if not unicodedata.combining(c)])
    except Exception:
        title_norm = title
    # search for pattern get .* me .* bodied or getmebodied or get-me-bodied
    if re.search(r'get\W*me\W*bodied', title_norm) or 'getmebodied' in re.sub(r'\W+', '', title_norm):
        matched_ids.add(tid)

# Sum revenues from sales for matched ids
per_track = []
total = 0.0
sales_by_id = {str(s['track_id']): float(s['revenue_usd']) for s in sales}
for tid in matched_ids:
    rev = sales_by_id.get(tid, 0.0)
    per_track.append({'track_id': tid, 'revenue_usd': rev})
    total += rev

result = {
    'total_revenue_usd': round(total, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'matched_track_ids': sorted(list(matched_ids), key=lambda x: int(x)),
    'per_track_revenue': sorted(per_track, key=lambda x: int(x['track_id']))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_x3p4JXP8ddyjoULtTMXRdMVZ': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '5281', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_vC56BH2AkQuGrHfUYObdB9js': [{'track_id': '5281', 'revenue_usd': '458.02'}, {'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
