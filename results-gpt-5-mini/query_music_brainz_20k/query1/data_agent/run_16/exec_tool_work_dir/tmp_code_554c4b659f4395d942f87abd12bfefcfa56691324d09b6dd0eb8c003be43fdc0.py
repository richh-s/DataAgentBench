code = """import json

tracks = var_call_MRkjmYGwXoN2afUpJCtx0c9u
sales = var_call_abdlBaH8bIn1A8K1DOHFFvnX

# Convert revenue strings to floats and sum
for r in sales:
    r['revenue_usd'] = float(r['revenue_usd'])

total_revenue = sum(r['revenue_usd'] for r in sales)

# Find matched track records
sales_track_ids = set(int(r['track_id']) for r in sales)
matched_tracks = [t for t in tracks if int(t['track_id']) in sales_track_ids]

# Helper to choose a representative field value
def choose_field(records, field):
    for r in records:
        v = r.get(field)
        if v and str(v).strip().lower() not in ('none','null',''):
            return v
    return None

representative_title = choose_field(matched_tracks, 'title') or 'Get Me Bodied'
representative_artist = choose_field(matched_tracks, 'artist') or 'Beyonce'

result = {
    'total_revenue_usd': round(total_revenue, 2),
    'currency': 'USD',
    'country': 'Canada',
    'store': 'Apple Music',
    'track_title': representative_title,
    'artist': representative_artist,
    'contributing_track_ids': sorted(list(sales_track_ids))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MRkjmYGwXoN2afUpJCtx0c9u': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '5281', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_abdlBaH8bIn1A8K1DOHFFvnX': [{'track_id': '5281', 'revenue_usd': '458.02'}, {'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
