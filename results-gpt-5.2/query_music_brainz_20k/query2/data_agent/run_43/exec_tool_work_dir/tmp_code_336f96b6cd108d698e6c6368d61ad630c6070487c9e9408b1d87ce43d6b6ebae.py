code = """import json
# Ensure numeric formatting and pick top store
rows = var_call_nQViakFgIeBDxOWzhw1e6eX1
# convert revenue to float
for r in rows:
    r['revenue_usd'] = float(r['revenue_usd'])
rows_sorted = sorted(rows, key=lambda x: x['revenue_usd'], reverse=True)
top = rows_sorted[0]
answer = f"{top['store']} (USD {top['revenue_usd']:.2f})"
print('__RESULT__:')
print(json.dumps({'answer': answer}))"""

env_args = {'var_call_ZxRt2A2hTJLxCyeSYqEVZXoi': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_FUGUSPzhnGxyZiMMJft4Ji3Y': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_nQViakFgIeBDxOWzhw1e6eX1': [{'store': 'iTunes', 'revenue_usd': '505.61'}, {'store': 'Amazon Music', 'revenue_usd': '304.13'}, {'store': 'Apple Music', 'revenue_usd': '116.20000000000002'}]}

exec(code, env_args)
