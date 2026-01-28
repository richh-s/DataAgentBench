code = """import json

tracks = var_functions.query_db:2
sales = var_functions.query_db:5

# Sum revenue per store
store_revenue = {}
for sale in sales:
    store = sale['store']
    revenue = float(sale['revenue_usd'])
    store_revenue[store] = store_revenue.get(store, 0) + revenue

# Find max revenue store
if store_revenue:
    max_store = max(store_revenue, key=store_revenue.get)
    max_revenue = store_revenue[max_store]
    result = f"{max_store} with ${max_revenue:.2f} in revenue"
else:
    result = "No sales found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:5': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}]}

exec(code, env_args)
