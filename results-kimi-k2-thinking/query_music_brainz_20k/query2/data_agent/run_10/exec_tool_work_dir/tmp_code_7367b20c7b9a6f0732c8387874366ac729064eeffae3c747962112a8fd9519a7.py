code = """import json
import pandas as pd

# Load sales data from storage
sales_data = [
    {"sale_id": "12386", "track_id": "4122", "country": "Germany", "store": "Apple Music", "units_sold": "47", "revenue_usd": "47.52"},
    {"sale_id": "12387", "track_id": "4122", "country": "France", "store": "Amazon Music", "units_sold": "262", "revenue_usd": "304.13"},
    {"sale_id": "13851", "track_id": "4628", "country": "France", "store": "iTunes", "units_sold": "469", "revenue_usd": "505.61"},
    {"sale_id": "42367", "track_id": "14080", "country": "UK", "store": "Apple Music", "units_sold": "59", "revenue_usd": "68.68"}
]

# Convert to DataFrame and aggregate revenue by store
df = pd.DataFrame(sales_data)
df['revenue_usd'] = df['revenue_usd'].astype(float)

# Group by store and sum revenue
store_revenue = df.groupby('store')['revenue_usd'].sum().reset_index()
store_revenue = store_revenue.sort_values('revenue_usd', ascending=False)

print('__RESULT__:')
print(json.dumps({
    'store_revenue_by_store': store_revenue.to_dict('records'),
    'top_store': store_revenue.iloc[0]['store'],
    'top_revenue': store_revenue.iloc[0]['revenue_usd']
}))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_functions.query_db:2': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
