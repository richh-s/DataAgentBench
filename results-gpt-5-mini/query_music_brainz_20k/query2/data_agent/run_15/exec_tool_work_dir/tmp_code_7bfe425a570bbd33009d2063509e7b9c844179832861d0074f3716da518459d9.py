code = """import json
# sales records from previous query
sales = var_call_12tIe88KPzu7PfvZY78eKVPM
# aggregate revenue by store
rev_by_store = {}
for r in sales:
    store = r.get('store')
    rev_str = r.get('revenue_usd')
    try:
        rev = float(rev_str)
    except Exception:
        rev = 0.0
    rev_by_store[store] = rev_by_store.get(store, 0.0) + rev
# find top store
if rev_by_store:
    top_store = max(rev_by_store.items(), key=lambda x: x[1])
    top_name, top_revenue = top_store
    # prepare breakdown sorted by revenue desc
    breakdown = {k: round(v, 2) for k, v in sorted(rev_by_store.items(), key=lambda x: -x[1])}
    result = {
        'top_store': top_name,
        'top_revenue_usd': round(top_revenue, 2),
        'breakdown_by_store': breakdown,
        'considered_track_ids': [r.get('track_id') for r in var_call_ijMcA2fGzQgZIcknKZZMsnoQ]
    }
else:
    result = {'error': 'no sales found for given track ids'}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ijMcA2fGzQgZIcknKZZMsnoQ': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_12tIe88KPzu7PfvZY78eKVPM': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
