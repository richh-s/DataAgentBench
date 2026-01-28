code = """import json

# Load the sales data
sales_data = [
    {"store": "Apple Music", "revenue_usd": "47.52"},
    {"store": "Amazon Music", "revenue_usd": "304.13"},
    {"store": "iTunes", "revenue_usd": "505.61"},
    {"store": "Apple Music", "revenue_usd": "68.68"}
]

# Convert revenue to float and aggregate by store
store_revenues = {}
for sale in sales_data:
    store = sale["store"]
    revenue = float(sale["revenue_usd"])
    if store in store_revenues:
        store_revenues[store] += revenue
    else:
        store_revenues[store] = revenue

# Find the store with the highest revenue
max_revenue = 0
max_store = ""
for store, revenue in store_revenues.items():
    if revenue > max_revenue:
        max_revenue = revenue
        max_store = store

# Print in required format
result = {
    "store": max_store,
    "revenue_usd": max_revenue
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:5': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}], 'var_functions.query_db:6': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:8': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:10': [{'store': 'Apple Music', 'revenue_usd': '47.52'}, {'store': 'Amazon Music', 'revenue_usd': '304.13'}, {'store': 'iTunes', 'revenue_usd': '505.61'}, {'store': 'Apple Music', 'revenue_usd': '68.68'}]}

exec(code, env_args)
