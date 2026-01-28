code = """import json

tracks = [{"track_id": "4122", "source_id": "5", "source_track_id": "10609996", "title": "Street Hype", "artist": "Brucqe Maginnis", "album": "Groove City", "year": "2005", "length": "177000", "language": "English"}]

sales = [{"sale_id": "12386", "track_id": "4122", "country": "Germany", "store": "Apple Music", "units_sold": "47", "revenue_usd": "47.52"}, {"sale_id": "12387", "track_id": "4122", "country": "France", "store": "Amazon Music", "units_sold": "262", "revenue_usd": "304.13"}]

# Calculate total revenue per store
store_revenue = {}
for sale in sales:
    store = sale['store']
    revenue = float(sale['revenue_usd'])
    if store in store_revenue:
        store_revenue[store] += revenue
    else:
        store_revenue[store] = revenue

# Find store with most revenue
max_revenue = 0
max_store = None
for store, revenue in store_revenue.items():
    if revenue > max_revenue:
        max_revenue = revenue
        max_store = store

result = {
    "store": max_store,
    "total_revenue_usd": max_revenue,
    "all_store_revenues": store_revenue
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:2': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}], 'var_functions.query_db:4': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}]}

exec(code, env_args)
