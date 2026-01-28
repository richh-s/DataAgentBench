code = """import json
sales = var_call_kQ19480sNavKFAbkfs0vZ2c0
# Convert string numbers to appropriate types and aggregate revenue by store across all countries
from collections import defaultdict
agg = defaultdict(float)
for r in sales:
    store = r['store']
    revenue = float(r['revenue_usd'])
    agg[store] += revenue

# find store with max revenue
if agg:
    max_store = max(agg.items(), key=lambda x: x[1])
    result = {'store': max_store[0], 'revenue_usd': round(max_store[1], 2)}
else:
    result = {'store': None, 'revenue_usd': 0.0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_B3cqelzDZtIesXQcbZXEcDSc': 'file_storage/call_B3cqelzDZtIesXQcbZXEcDSc.json', 'var_call_yZ53M3lvJsimljxOJJX5rev3': [7, 4122, 4628, 13758, 14080], 'var_call_kQ19480sNavKFAbkfs0vZ2c0': [{'sale_id': '27', 'track_id': '7', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '99', 'revenue_usd': '114.68'}, {'sale_id': '28', 'track_id': '7', 'country': 'France', 'store': 'Apple Music', 'units_sold': '227', 'revenue_usd': '276.54'}, {'sale_id': '29', 'track_id': '7', 'country': 'Canada', 'store': 'iTunes', 'units_sold': '218', 'revenue_usd': '262.3'}, {'sale_id': '30', 'track_id': '7', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '346', 'revenue_usd': '353.74'}, {'sale_id': '31', 'track_id': '7', 'country': 'USA', 'store': 'Amazon Music', 'units_sold': '63', 'revenue_usd': '73.02'}, {'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '41412', 'track_id': '13758', 'country': 'UK', 'store': 'Google Play', 'units_sold': '44', 'revenue_usd': '51.4'}, {'sale_id': '41413', 'track_id': '13758', 'country': 'USA', 'store': 'iTunes', 'units_sold': '119', 'revenue_usd': '148.95'}, {'sale_id': '41414', 'track_id': '13758', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '353', 'revenue_usd': '378.1'}, {'sale_id': '41415', 'track_id': '13758', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '406', 'revenue_usd': '477.06'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
