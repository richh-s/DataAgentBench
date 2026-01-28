code = """import json
# Sales data pulled from storage
sales = locals()['var_functions.query_db:2']
# Ensure we have list of dicts
if isinstance(sales, str):
    # It's a file path: read it
    with open(sales) as f:
        sales = json.load(f)
# Compute total revenue per store
store_revenue = {}
for record in sales:
    store = record['store']
    revenue = float(record['revenue_usd'])
    store_revenue[store] = store_revenue.get(store, 0.0) + revenue
# Find store with max revenue
max_store = max(store_revenue, key=store_revenue.get)
max_revenue = store_revenue[max_store]
# Print result as JSON
result = {"store": max_store, "total_revenue_usd": max_revenue}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:2': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
