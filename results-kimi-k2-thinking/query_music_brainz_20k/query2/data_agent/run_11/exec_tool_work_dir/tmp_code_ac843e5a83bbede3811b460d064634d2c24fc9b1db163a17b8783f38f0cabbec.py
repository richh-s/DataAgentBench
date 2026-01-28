code = """import json

# Get the sales data from the previous query
sales_data_key = 'var_functions.query_db:8'
sales_data = locals()[sales_data_key]

# If sales_data is a string (file path), load it
if isinstance(sales_data, str):
    with open(sales_data, 'r') as f:
        sales_data = json.load(f)

# Calculate total revenue by store
store_revenue = {}
for sale in sales_data:
    store = sale['store']
    revenue = float(sale['revenue_usd'])
    store_revenue[store] = store_revenue.get(store, 0) + revenue

# Find the store with the most revenue
max_revenue = 0
max_store = None
for store, revenue in store_revenue.items():
    if revenue > max_revenue:
        max_revenue = revenue
        max_store = store

result = {
    'store': max_store,
    'total_revenue_usd': round(max_revenue, 2),
    'all_store_revenues': store_revenue
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:2': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_functions.query_db:5': [{'track_id': '4122', 'store': 'Amazon Music', 'country': 'France', 'units_sold': '262', 'revenue_usd': '304.13'}, {'track_id': '4122', 'store': 'Apple Music', 'country': 'Germany', 'units_sold': '47', 'revenue_usd': '47.52'}, {'track_id': '14080', 'store': 'Apple Music', 'country': 'UK', 'units_sold': '59', 'revenue_usd': '68.68'}, {'track_id': '4628', 'store': 'iTunes', 'country': 'France', 'units_sold': '469', 'revenue_usd': '505.61'}], 'var_functions.query_db:6': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_functions.query_db:8': [{'track_id': '4122', 'store': 'Amazon Music', 'country': 'France', 'units_sold': '262', 'revenue_usd': '304.13'}, {'track_id': '13758', 'store': 'Amazon Music', 'country': 'France', 'units_sold': '353', 'revenue_usd': '378.1'}, {'track_id': '4122', 'store': 'Apple Music', 'country': 'Germany', 'units_sold': '47', 'revenue_usd': '47.52'}, {'track_id': '13758', 'store': 'Apple Music', 'country': 'UK', 'units_sold': '406', 'revenue_usd': '477.06'}, {'track_id': '14080', 'store': 'Apple Music', 'country': 'UK', 'units_sold': '59', 'revenue_usd': '68.68'}, {'track_id': '13758', 'store': 'Google Play', 'country': 'UK', 'units_sold': '44', 'revenue_usd': '51.4'}, {'track_id': '4628', 'store': 'iTunes', 'country': 'France', 'units_sold': '469', 'revenue_usd': '505.61'}, {'track_id': '13758', 'store': 'iTunes', 'country': 'USA', 'units_sold': '119', 'revenue_usd': '148.95'}]}

exec(code, env_args)
