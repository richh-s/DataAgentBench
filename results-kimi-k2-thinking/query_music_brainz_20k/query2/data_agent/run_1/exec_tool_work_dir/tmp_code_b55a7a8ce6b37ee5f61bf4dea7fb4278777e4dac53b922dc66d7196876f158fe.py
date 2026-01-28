code = """import json

# Load the sales data
sales_data = var_functions.query_db:12

# Parse the data
sales = json.loads(sales_data.replace("'", '"'))

# Aggregate revenue by store
store_revenue = {}
for sale in sales:
    store = sale['store']
    revenue = float(sale['total_revenue'])
    if store in store_revenue:
        store_revenue[store] += revenue
    else:
        store_revenue[store] = revenue

# Find the store with maximum revenue
max_store = max(store_revenue, key=store_revenue.get)
max_revenue = store_revenue[max_store]

# Prepare result
result = {
    "store": max_store,
    "total_revenue_usd": round(max_revenue, 2),
    "all_store_revenues": store_revenue
}

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:5': [{'store': 'Amazon Music', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'total_revenue': '47.52'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'artist': 'Max Bruch'}, {'artist': 'Bruce Broughton'}, {'artist': 'Bruce Dikinson'}, {'artist': 'Bruce Springsteen & The E Street Band'}, {'artist': 'Brucqe Maginnis'}, {'artist': 'Bruce Daigrepont'}, {'artist': 'Bruce Maginnis'}, {'artist': 'Bruce Springsteen'}, {'artist': 'Arthur Dobrucki'}, {'artist': 'Bruce Cockburn'}, {'artist': 'Bruce Anthony'}, {'artist': 'Bruce '}, {'artist': 'Bruce Dickinson'}, {'artist': 'Bruce Broughtopn'}], 'var_functions.query_db:10': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_functions.query_db:12': [{'track_id': '4122', 'store': 'Amazon Music', 'total_revenue': '304.13'}, {'track_id': '4122', 'store': 'Apple Music', 'total_revenue': '47.52'}, {'track_id': '4628', 'store': 'iTunes', 'total_revenue': '505.61'}, {'track_id': '14080', 'store': 'Apple Music', 'total_revenue': '68.68'}]}

exec(code, env_args)
