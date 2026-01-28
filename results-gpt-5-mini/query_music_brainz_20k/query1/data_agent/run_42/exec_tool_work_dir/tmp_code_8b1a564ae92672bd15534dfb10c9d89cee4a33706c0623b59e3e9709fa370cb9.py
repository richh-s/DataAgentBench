code = """import json
sales = var_call_5ZCL5xULTiD5477dS7xteSl1
tracks = var_call_gVFeyvPq5i8sHGBaAYZaXFAQ
beyonce_ids = set()
for r in tracks:
    title = (r.get('title') or '').lower()
    artist = (r.get('artist') or '').lower()
    if 'get me bodied' in title or 'beyonc' in artist:
        tid = r.get('track_id')
        beyonce_ids.add(str(tid))

total = 0.0
for r in sales:
    if str(r.get('track_id')) in beyonce_ids:
        try:
            total += float(r.get('revenue_usd') or 0)
        except:
            pass

total = round(total, 2)
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_gVFeyvPq5i8sHGBaAYZaXFAQ': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '10838', 'title': 'Beyoncé - Get Me Bodied', 'artist': 'None', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '07'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_5ZCL5xULTiD5477dS7xteSl1': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
