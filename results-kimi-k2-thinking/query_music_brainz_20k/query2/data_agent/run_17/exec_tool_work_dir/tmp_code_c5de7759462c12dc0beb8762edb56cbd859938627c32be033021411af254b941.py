code = """import json

# Using the results from previous queries
# var_functions.query_db:8 contains the sales grouped by store

# The result from query 8:
sales_by_store = [
    {"store": "Amazon Music", "total_revenue": "682.23"},
    {"store": "iTunes", "total_revenue": "654.56"},
    {"store": "Apple Music", "total_revenue": "593.26"},
    {"store": "Google Play", "total_revenue": "51.4"}
]

# Find the store with the highest revenue
max_revenue_store = max(sales_by_store, key=lambda x: float(x['total_revenue']))

# Get the result
result = f"{max_revenue_store['store']} earned the most revenue at ${max_revenue_store['total_revenue']} USD"

# Print in the required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:2': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}], 'var_functions.query_db:5': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:6': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '13758', 'source_id': '1', 'source_track_id': 'WoM21220012', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005', 'length': 'None', 'language': '02:57'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:8': [{'store': 'Amazon Music', 'total_revenue': '682.23'}, {'store': 'iTunes', 'total_revenue': '654.56'}, {'store': 'Apple Music', 'total_revenue': '593.26'}, {'store': 'Google Play', 'total_revenue': '51.4'}], 'var_functions.query_db:10': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '13758', 'source_id': '1', 'source_track_id': 'WoM21220012', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005', 'length': 'None', 'language': '02:57'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}]}

exec(code, env_args)
