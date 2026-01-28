code = """import json
# use the query result from sales
data = var_call_pr7pvz1mXhJCFgjitja1BGTJ
# data is a list of dicts with strings
store_totals = {}
for r in data:
    store = r.get('store')
    rev = r.get('revenue_usd_total')
    try:
        rev_f = float(rev)
    except:
        rev_f = 0.0
    store_totals[store] = store_totals.get(store, 0.0) + rev_f
# round to 2 decimals
store_totals_rounded = {k: round(v, 2) for k, v in store_totals.items()}
# find top
top_store = max(store_totals_rounded.items(), key=lambda x: x[1])
result = {
    'store_totals': store_totals_rounded,
    'top_store': top_store[0],
    'top_revenue': top_store[1]
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lcDjXSrqM6FYjP34MTn1v9rF': 'file_storage/call_lcDjXSrqM6FYjP34MTn1v9rF.json', 'var_call_inNQWEzftDFnW12NIvuzPqoG': [7, 4122, 4628, 13758, 14080], 'var_call_pr7pvz1mXhJCFgjitja1BGTJ': [{'track_id': '7', 'store': 'iTunes', 'revenue_usd_total': '262.3'}, {'track_id': '4122', 'store': 'Amazon Music', 'revenue_usd_total': '304.13'}, {'track_id': '13758', 'store': 'Apple Music', 'revenue_usd_total': '477.06'}, {'track_id': '13758', 'store': 'iTunes', 'revenue_usd_total': '148.95'}, {'track_id': '7', 'store': 'Apple Music', 'revenue_usd_total': '391.22'}, {'track_id': '7', 'store': 'Amazon Music', 'revenue_usd_total': '426.76'}, {'track_id': '4628', 'store': 'iTunes', 'revenue_usd_total': '505.61'}, {'track_id': '14080', 'store': 'Apple Music', 'revenue_usd_total': '68.68'}, {'track_id': '13758', 'store': 'Google Play', 'revenue_usd_total': '51.4'}, {'track_id': '13758', 'store': 'Amazon Music', 'revenue_usd_total': '378.1'}, {'track_id': '4122', 'store': 'Apple Music', 'revenue_usd_total': '47.52'}]}

exec(code, env_args)
