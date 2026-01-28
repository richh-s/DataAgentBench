code = """sales_data = [{"sale_id": "12386", "track_id": "4122", "country": "Germany", "store": "Apple Music", "units_sold": "47", "revenue_usd": "47.52"}, {"sale_id": "12387", "track_id": "4122", "country": "France", "store": "Amazon Music", "units_sold": "262", "revenue_usd": "304.13"}]

# Calculate total revenue per store
store_revenues = {}
for sale in sales_data:
    store = sale['store']
    revenue = float(sale['revenue_usd'])
    if store in store_revenues:
        store_revenues[store] += revenue
    else:
        store_revenues[store] = revenue

# Find the store with max revenue
max_store = max(store_revenues, key=store_revenues.get)
max_revenue = store_revenues[max_store]

result = {"store": max_store, "total_revenue_usd": max_revenue}

print('__RESULT__:')
print(str(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:2': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}]}

exec(code, env_args)
