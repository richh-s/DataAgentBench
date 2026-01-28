code = """import json
sales = var_call_AMYBQdhPHR808gZhmT3ttPXi
# Aggregate revenue by store
totals = {}
for r in sales:
    store = r['store']
    try:
        rev = float(r['revenue_usd'])
    except:
        rev = 0.0
    totals[store] = totals.get(store, 0.0) + rev
# Determine top store
if totals:
    top_store, top_rev = max(totals.items(), key=lambda x: x[1])
    top_rev = round(top_rev, 2)
else:
    top_store, top_rev = None, 0.0
out = {"store_totals": totals, "top_store": top_store, "top_revenue": top_rev}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_u5TWATYNyv7F1kG8b6u6QXLR': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_call_AMYBQdhPHR808gZhmT3ttPXi': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
