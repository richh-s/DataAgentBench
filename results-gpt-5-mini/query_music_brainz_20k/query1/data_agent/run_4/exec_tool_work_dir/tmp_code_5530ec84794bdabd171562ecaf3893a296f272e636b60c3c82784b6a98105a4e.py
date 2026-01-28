code = """import json
tracks = var_call_3dG2aTs2FH4mYfyGDcfVp3ia
sales = var_call_UUIdxgmpodkBQnxlphQRvkRo

track_ids = [str(r['track_id']) for r in tracks]
revenue_map = {str(r['track_id']): float(r['revenue_usd']) for r in sales}
revenue_by_track = {tid: revenue_map.get(tid, 0.0) for tid in track_ids}

total_revenue = sum(revenue_by_track.values())
output = {
    'matched_track_ids': track_ids,
    'revenue_by_track': revenue_by_track,
    'total_revenue_usd': round(total_revenue, 2)
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_3dG2aTs2FH4mYfyGDcfVp3ia': [{'track_id': '4233', 'title': 'Get Me Bodied (Sexxxplicit R&B, Volume 25)', 'artist': 'Beyoncé', 'album': 'Sexxxplicit R&B, Volume 25', 'year': '2007'}, {'track_id': '12954', 'title': 'Get Me Bodied - Sexxxplicit R&B, Volume 25', 'artist': 'Beyoncé', 'album': 'None', 'year': "'07"}, {'track_id': '15158', 'title': '022-Get Me Bodied', 'artist': 'Beyonce', 'album': 'Sexxxplicit R&B, Volume 25 (2007)', 'year': 'None'}], 'var_call_UUIdxgmpodkBQnxlphQRvkRo': [{'track_id': '4233', 'revenue_usd': '377.62'}, {'track_id': '12954', 'revenue_usd': '223.82'}]}

exec(code, env_args)
