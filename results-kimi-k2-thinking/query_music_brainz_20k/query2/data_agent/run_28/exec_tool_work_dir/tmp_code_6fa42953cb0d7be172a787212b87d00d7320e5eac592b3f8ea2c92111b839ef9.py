code = """import json

# Get the sales data for the track
sales_data = [{"store": "Apple Music", "revenue_usd": "47.52"}, {"store": "Amazon Music", "revenue_usd": "304.13"}]

# Calculate total revenue per store
store_revenues = {}
for sale in sales_data:
    store = sale["store"]
    revenue = float(sale["revenue_usd"])
    if store not in store_revenues:
        store_revenues[store] = 0
    store_revenues[store] += revenue

# Find the store with the most revenue
max_store = max(store_revenues, key=store_revenues.get)
max_revenue = store_revenues[max_store]

result = {"store": max_store, "revenue_usd": max_revenue}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_functions.query_db:2': [{'store': 'Apple Music', 'revenue_usd': '47.52'}, {'store': 'Amazon Music', 'revenue_usd': '304.13'}]}

exec(code, env_args)
