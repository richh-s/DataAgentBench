code = """import json

# Query results
sales_track_store = [{"track_id": "4122", "store": "Apple Music", "total_revenue": "47.52"}, {"track_id": "4122", "store": "Amazon Music", "total_revenue": "304.13"}, {"track_id": "4628", "store": "iTunes", "total_revenue": "505.61"}, {"track_id": "14080", "store": "Apple Music", "total_revenue": "68.68"}]

sales_store_agg = [{"store": "iTunes", "total_revenue": "505.61"}]

total_revenue_by_store = {}
for rec in sales_track_store:
    store = rec['store']
    rev = float(rec['total_revenue'])
    if store not in total_revenue_by_store:
        total_revenue_by_store[store] = 0
    total_revenue_by_store[store] += rev

# Find the store with highest revenue
max_store = max(total_revenue_by_store, key=total_revenue_by_store.get)
max_revenue = total_revenue_by_store[max_store]

result = {"store": max_store, "total_revenue_usd": max_revenue}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:5': [{'store': 'Amazon Music', 'total_revenue': '304.13'}], 'var_functions.query_db:6': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:8': [{'track_id': '4122', 'store': 'Apple Music', 'total_revenue': '47.52'}, {'track_id': '4122', 'store': 'Amazon Music', 'total_revenue': '304.13'}, {'track_id': '4628', 'store': 'iTunes', 'total_revenue': '505.61'}, {'track_id': '14080', 'store': 'Apple Music', 'total_revenue': '68.68'}], 'var_functions.query_db:12': [{'store': 'iTunes', 'total_revenue': '505.61'}]}

exec(code, env_args)
