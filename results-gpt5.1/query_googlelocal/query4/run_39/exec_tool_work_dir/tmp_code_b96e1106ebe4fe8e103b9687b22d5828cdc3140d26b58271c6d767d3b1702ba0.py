code = """import json

reviews = var_call_m1Sazsc9kyMeJriBcDgyoc66
businesses = var_call_O5DWpq3PXveaGJjZQscEpy9D

name_map = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in reviews:
    result.append({
        'business_name': name_map.get(r['gmap_id'], ''),
        'gmap_id': r['gmap_id'],
        'high_rating_review_count_2019': int(r['high_review_count'])
    })

result_sorted = sorted(result, key=lambda x: x['high_rating_review_count_2019'], reverse=True)

output = json.dumps(result_sorted)

print('__RESULT__:')
print(output)"""

env_args = {'var_call_m1Sazsc9kyMeJriBcDgyoc66': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_rGD0oAzQjYBAZ97afQo2Rxgh': ['business_description'], 'var_call_O5DWpq3PXveaGJjZQscEpy9D': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
