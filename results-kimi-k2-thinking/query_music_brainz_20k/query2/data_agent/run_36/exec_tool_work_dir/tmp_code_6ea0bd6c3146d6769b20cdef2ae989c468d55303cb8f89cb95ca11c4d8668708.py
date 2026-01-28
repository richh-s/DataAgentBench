code = """import json

# Load the results from the sales queries
sales_4122 = [{"sale_id": "12386", "track_id": "4122", "country": "Germany", "store": "Apple Music", "units_sold": "47", "revenue_usd": "47.52"}, {"sale_id": "12387", "track_id": "4122", "country": "France", "store": "Amazon Music", "units_sold": "262", "revenue_usd": "304.13"}]

sales_4628_14080 = [{"sale_id": "13851", "track_id": "4628", "country": "France", "store": "iTunes", "units_sold": "469", "revenue_usd": "505.61"}, {"sale_id": "42367", "track_id": "14080", "country": "UK", "store": "Apple Music", "units_sold": "59", "revenue_usd": "68.68"}]

# Combine all sales
all_sales = sales_4122 + sales_4628_14080

# Group by store and sum revenue
store_revenues = {}
for sale in all_sales:
    store = sale['store']
    revenue = float(sale['revenue_usd'])
    store_revenues[store] = store_revenues.get(store, 0) + revenue

# Find store with max revenue
max_store = max(store_revenues.items(), key=lambda x: x[1])

print('__RESULT__:')
print(json.dumps({"store": max_store[0], "total_revenue_usd": max_store[1]}))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:2': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:5': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}], 'var_functions.query_db:6': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:8': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:10': [{'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
