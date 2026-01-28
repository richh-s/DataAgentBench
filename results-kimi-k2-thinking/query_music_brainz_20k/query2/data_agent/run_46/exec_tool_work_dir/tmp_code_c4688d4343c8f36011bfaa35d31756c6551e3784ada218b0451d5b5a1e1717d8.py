code = """import json

# Load the sales data
sales_data = [{"sale_id": "12386", "track_id": "4122", "country": "Germany", "store": "Apple Music", "units_sold": "47", "revenue_usd": "47.52"}, {"sale_id": "12387", "track_id": "4122", "country": "France", "store": "Amazon Music", "units_sold": "262", "revenue_usd": "304.13"}]

# Calculate total revenue per store
store_revenue = {}
for sale in sales_data:
    store = sale['store']
    revenue = float(sale['revenue_usd'])
    store_revenue[store] = store_revenue.get(store, 0) + revenue

# Find store with most revenue
max_revenue_store = max(store_revenue, key=store_revenue.get)
max_revenue = store_revenue[max_revenue_store]

result = f"{max_revenue_store} earned the most revenue: ${max_revenue:.2f} USD"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:2': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}]}

exec(code, env_args)
