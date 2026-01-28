code = """import json

# Get the query results from storage
sales_data = locals()['var_functions.query_db:14']

# Create a dictionary to store total revenue by store
store_revenue = {}

# Process each sale record
for record in sales_data:
    store = record['store']
    revenue = float(record['total_revenue'])
    
    if store in store_revenue:
        store_revenue[store] += revenue
    else:
        store_revenue[store] = revenue

# Sort stores by total revenue in descending order
sorted_stores = sorted(store_revenue.items(), key=lambda x: x[1], reverse=True)

# Get the store with the most revenue
top_store = sorted_stores[0]

result = {
    'store': top_store[0],
    'total_revenue_usd': round(top_store[1], 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:4': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:6': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:8': [{'store': 'Amazon Music', 'country': 'France', 'total_revenue': '304.13'}, {'store': 'Apple Music', 'country': 'Germany', 'total_revenue': '47.52'}], 'var_functions.query_db:10': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:12': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:14': [{'track_id': '4628', 'store': 'iTunes', 'country': 'France', 'total_revenue': '505.61'}, {'track_id': '4122', 'store': 'Amazon Music', 'country': 'France', 'total_revenue': '304.13'}, {'track_id': '14080', 'store': 'Apple Music', 'country': 'UK', 'total_revenue': '68.68'}, {'track_id': '4122', 'store': 'Apple Music', 'country': 'Germany', 'total_revenue': '47.52'}]}

exec(code, env_args)
