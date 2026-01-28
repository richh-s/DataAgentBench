code = """import json
rows = var_call_fzYW8nsL0Y76UW2OOnL7Cvmo
# Convert revenue strings to floats
for r in rows:
    try:
        r['total_revenue'] = float(r['total_revenue'])
    except:
        r['total_revenue'] = None
if rows:
    # filter out None revenues
    valid = [r for r in rows if r['total_revenue'] is not None]
    if valid:
        top = max(valid, key=lambda x: x['total_revenue'])
        result = {"store": top['store'], "revenue_usd": round(top['total_revenue'], 2)}
    else:
        result = {"store": None, "revenue_usd": None}
else:
    result = {"store": None, "revenue_usd": None}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZFy6cVejLEV5lyValgSDYBpg': ['tracks'], 'var_call_vf5iiqBhdfXsjYgpy2Uq0Zi8': ['sales'], 'var_call_PpsChfKSo0m0rQ7NLLe8ySqg': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_fzYW8nsL0Y76UW2OOnL7Cvmo': [{'store': 'Amazon Music', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'total_revenue': '47.52'}]}

exec(code, env_args)
