code = """import json

rows = var_call_gYzZi7aYPpnNeIVISuIIP2yy

# Sum revenue per store across all duplicate track_ids
store_totals = {}
for r in rows:
    store = r['store']
    rev = float(r['total_revenue'])
    store_totals[store] = store_totals.get(store, 0.0) + rev

# Find store with max revenue
best_store = max(store_totals.items(), key=lambda x: x[1])
result = {
    'store': best_store[0],
    'total_revenue_usd': round(best_store[1], 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AozmnzhHLSekXdSm7glcqgUs': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_dN0t2P6JUz4YamEQ2NgHUBEg': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_gYzZi7aYPpnNeIVISuIIP2yy': [{'track_id': '4122', 'store': 'Amazon Music', 'total_revenue': '304.13'}, {'track_id': '14080', 'store': 'Apple Music', 'total_revenue': '68.68'}, {'track_id': '4628', 'store': 'iTunes', 'total_revenue': '505.61'}, {'track_id': '4122', 'store': 'Apple Music', 'total_revenue': '47.52'}]}

exec(code, env_args)
