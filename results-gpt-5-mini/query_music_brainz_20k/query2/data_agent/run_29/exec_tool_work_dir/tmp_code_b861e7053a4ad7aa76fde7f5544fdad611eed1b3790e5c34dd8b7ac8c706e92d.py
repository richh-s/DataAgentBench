code = """import json
# var_call_gC2gEWPYTlliXsHuMA1QixGj is available from previous query
data = var_call_gC2gEWPYTlliXsHuMA1QixGj
# Normalize and find max
for r in data:
    # revenue may be string; convert to float
    try:
        r['total_revenue'] = float(r['total_revenue'])
    except Exception:
        r['total_revenue'] = None
if not data:
    result = {"store": None, "total_revenue": None}
else:
    # filter out None revenues
    valid = [r for r in data if r['total_revenue'] is not None]
    if not valid:
        result = {"store": None, "total_revenue": None}
    else:
        best = max(valid, key=lambda x: x['total_revenue'])
        result = {"store": best['store'], "total_revenue": best['total_revenue']}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MPGEBckSiVuXbYf7Ib4SGvQM': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_gC2gEWPYTlliXsHuMA1QixGj': [{'store': 'Amazon Music', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'total_revenue': '47.52'}]}

exec(code, env_args)
