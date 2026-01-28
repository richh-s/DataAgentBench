code = """import json

# Sales data from the query for all 4 track_ids
sales_data = [
    {"sale_id": "12386", "track_id": "4122", "country": "Germany", "store": "Apple Music", "units_sold": "47", "revenue_usd": "47.52"},
    {"sale_id": "12387", "track_id": "4122", "country": "France", "store": "Amazon Music", "units_sold": "262", "revenue_usd": "304.13"},
    {"sale_id": "13851", "track_id": "4628", "country": "France", "store": "iTunes", "units_sold": "469", "revenue_usd": "505.61"},
    {"sale_id": "41412", "track_id": "13758", "country": "UK", "store": "Google Play", "units_sold": "44", "revenue_usd": "51.40"},
    {"sale_id": "41413", "track_id": "13758", "country": "USA", "store": "iTunes", "units_sold": "119", "revenue_usd": "148.95"},
    {"sale_id": "41414", "track_id": "13758", "country": "France", "store": "Amazon Music", "units_sold": "353", "revenue_usd": "378.10"},
    {"sale_id": "41415", "track_id": "13758", "country": "UK", "store": "Apple Music", "units_sold": "406", "revenue_usd": "477.06"},
    {"sale_id": "42367", "track_id": "14080", "country": "UK", "store": "Apple Music", "units_sold": "59", "revenue_usd": "68.68"}
]

# Convert to DataFrame for analysis
import pandas as pd
df = pd.DataFrame(sales_data)

# Convert string values to numeric
df['revenue_usd'] = df['revenue_usd'].astype(float)
df['units_sold'] = df['units_sold'].astype(int)

# Group by store to calculate total revenue per store
store_revenue = df.groupby('store')['revenue_usd'].sum().reset_index()

# Sort by revenue in descending order
store_revenue_sorted = store_revenue.sort_values('revenue_usd', ascending=False)

# Get the store with the most revenue
top_store = store_revenue_sorted.iloc[0]

result = {
    "top_store": top_store['store'],
    "total_revenue_usd": round(top_store['revenue_usd'], 2)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_functions.query_db:4': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.list_db:6': ['sales'], 'var_functions.query_db:8': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}], 'var_functions.execute_python:10': {'top_store': 'iTunes', 'total_revenue': 505.61}, 'var_functions.query_db:12': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '13758', 'source_id': '1', 'source_track_id': 'WoM21220012', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005', 'length': 'None', 'language': '02:57'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:14': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '41412', 'track_id': '13758', 'country': 'UK', 'store': 'Google Play', 'units_sold': '44', 'revenue_usd': '51.4'}, {'sale_id': '41413', 'track_id': '13758', 'country': 'USA', 'store': 'iTunes', 'units_sold': '119', 'revenue_usd': '148.95'}, {'sale_id': '41414', 'track_id': '13758', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '353', 'revenue_usd': '378.1'}, {'sale_id': '41415', 'track_id': '13758', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '406', 'revenue_usd': '477.06'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
