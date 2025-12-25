code = """import json

reviews = var_call_ONp9eqW71cuwrehZ6RaYq9iM
businesses = var_call_FNpHfS9uJBYR6PbQn4bf650f

bus_map = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in reviews:
    result.append({
        'business_name': bus_map.get(r['gmap_id'], r['gmap_id']),
        'high_rating_review_count': int(r['high_review_count'])
    })

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_ONp9eqW71cuwrehZ6RaYq9iM': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_PlVEcH1v0hsK00fiOhnxp4kD': ['business_description'], 'var_call_FNpHfS9uJBYR6PbQn4bf650f': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
