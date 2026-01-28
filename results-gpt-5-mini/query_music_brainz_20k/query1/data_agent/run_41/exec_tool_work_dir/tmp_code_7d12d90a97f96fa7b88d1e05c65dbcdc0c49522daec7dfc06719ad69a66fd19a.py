code = """import json
# Access previous tool results
tracks = var_call_wKWDHmyy5efLVqBVrUct3838
sales = var_call_cjLFEsFVXUPRYpznKe9wclk2

# Build set of candidate track_ids from tracks that likely refer to "Get Me Bodied" by Beyoncé
candidate_ids = set()
for t in tracks:
    tid = str(t.get('track_id'))
    title = (t.get('title') or '').lower()
    artist = (t.get('artist') or '').lower()
    if 'get me bodied' in title or 'getme bodied' in title or 'getme' in title or 'get me bodied' in title:
        # also require artist mentions beyonce or title contains explicit mention
        if 'beyonc' in artist or 'beyonc' in title or 'get me bodied' in title:
            candidate_ids.add(tid)

# Sum revenue from sales where country=Canada and store=Apple Music and track_id in candidate_ids
total = 0.0
matched_sales = []
for s in sales:
    if str(s.get('track_id')) in candidate_ids:
        try:
            total += float(s.get('revenue_usd'))
            matched_sales.append(s)
        except Exception:
            pass

# Round to 2 decimal places
total_rounded = round(total, 2)

result = {"total_revenue_usd": total_rounded, "currency": "USD", "country": "Canada", "store": "Apple Music", "track_title": "Get Me Bodied", "artist": "Beyoncé", "matched_track_ids": sorted(list(candidate_ids)), "matched_sales": matched_sales}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wKWDHmyy5efLVqBVrUct3838': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007', 'length': '00:00', 'language': 'None'}, {'track_id': '5281', 'title': 'GetMe Bodied', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume X25', 'year': '2007', 'length': 'None', 'language': 'English'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07', 'length': 'None', 'language': 'Egnlish'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07", 'length': 'None', 'language': 'English'}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}], 'var_call_cjLFEsFVXUPRYpznKe9wclk2': [{'track_id': '4233', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '377.62'}, {'track_id': '5281', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '458.02'}, {'track_id': '12954', 'country': 'Canada', 'store': 'Apple Music', 'revenue_usd': '223.82'}]}

exec(code, env_args)
