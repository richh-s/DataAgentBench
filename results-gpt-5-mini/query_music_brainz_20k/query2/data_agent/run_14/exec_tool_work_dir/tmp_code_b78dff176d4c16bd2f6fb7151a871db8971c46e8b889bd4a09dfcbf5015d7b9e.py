code = """import json
rows = var_call_yCcUxLpG5FPhIewTuxvEtCeq
# Convert revenue to float and find max
best = None
for r in rows:
    try:
        rev = float(r.get('total_revenue'))
    except Exception:
        rev = float(r.get('total_revenue') or 0)
    if best is None or rev > best[1]:
        best = (r.get('store'), rev)
if best is None:
    answer = "No sales found for the specified track(s)."
else:
    answer = f"{best[0]} with total revenue USD {best[1]:.2f}"
print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_VAdK4G7VDYrIHnDH43JisjWV': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_PTHzFOTVPH2uYuNwzR2628FL': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_yCcUxLpG5FPhIewTuxvEtCeq': [{'store': 'Amazon Music', 'total_revenue': '682.23'}, {'store': 'iTunes', 'total_revenue': '654.56'}, {'store': 'Apple Music', 'total_revenue': '593.26'}, {'store': 'Google Play', 'total_revenue': '51.4'}]}

exec(code, env_args)
