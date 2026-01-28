code = """import json

# Load the sales data for all three track IDs
sales_data = [
    {"sale_id": "12386", "track_id": "4122", "country": "Germany", "store": "Apple Music", "units_sold": "47", "revenue_usd": "47.52"},
    {"sale_id": "12387", "track_id": "4122", "country": "France", "store": "Amazon Music", "units_sold": "262", "revenue_usd": "304.13"},
    {"sale_id": "13851", "track_id": "4628", "country": "France", "store": "iTunes", "units_sold": "469", "revenue_usd": "505.61"},
    {"sale_id": "42367", "track_id": "14080", "country": "UK", "store": "Apple Music", "units_sold": "59", "revenue_usd": "68.68"}
]

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

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:2': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}], 'var_functions.execute_python:5': 'Amazon Music earned the most revenue: $304.13 USD', 'var_functions.query_db:6': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_functions.query_db:8': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_functions.query_db:10': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_functions.query_db:12': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
