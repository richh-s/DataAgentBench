code = """import pandas as pd
import json

# load sales query result
sales = pd.DataFrame(var_call_Ox7DzlEQpbusOaQxG6tJmGaA)
# convert numeric columns
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

# aggregate total revenue by store across all records
agg = sales.groupby('store', as_index=False)['revenue_usd'].sum()
# find top store
top = agg.sort_values('revenue_usd', ascending=False).iloc[0]
# prepare output
result = {
    'aggregated_revenue_by_store': agg.sort_values('revenue_usd', ascending=False).to_dict(orient='records'),
    'top_store': {
        'store': top['store'],
        'total_revenue_usd': top['revenue_usd']
    }
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CNN3yRYVvkJfCft81uiH2XO5': 'file_storage/call_CNN3yRYVvkJfCft81uiH2XO5.json', 'var_call_4qde2NKRSGe5gAatzqdxOYtG': {'track_ids': [4122, 4628, 13758, 14080], 'records': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}]}, 'var_call_Ox7DzlEQpbusOaQxG6tJmGaA': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '41412', 'track_id': '13758', 'country': 'UK', 'store': 'Google Play', 'units_sold': '44', 'revenue_usd': '51.4'}, {'sale_id': '41413', 'track_id': '13758', 'country': 'USA', 'store': 'iTunes', 'units_sold': '119', 'revenue_usd': '148.95'}, {'sale_id': '41414', 'track_id': '13758', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '353', 'revenue_usd': '378.1'}, {'sale_id': '41415', 'track_id': '13758', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '406', 'revenue_usd': '477.06'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
