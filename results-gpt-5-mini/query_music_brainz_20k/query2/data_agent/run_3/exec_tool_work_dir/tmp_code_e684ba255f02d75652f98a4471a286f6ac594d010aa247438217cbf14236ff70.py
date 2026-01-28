code = """import json
# data from sales query
data = var_call_b7YvKH8HGVxf1OVgtx1cfYEf
# convert revenue strings to floats
for r in data:
    r['total_revenue_usd'] = float(r['total_revenue_usd'])
# find the store with maximum revenue
best = max(data, key=lambda x: x['total_revenue_usd'])
result = {"store": best['store'], "total_revenue_usd": best['total_revenue_usd']}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DN0zpTIVVA498OIcBbbcyFcK': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_b7YvKH8HGVxf1OVgtx1cfYEf': [{'store': 'iTunes', 'total_revenue_usd': '505.61'}, {'store': 'Amazon Music', 'total_revenue_usd': '304.13'}, {'store': 'Apple Music', 'total_revenue_usd': '116.20000000000002'}]}

exec(code, env_args)
