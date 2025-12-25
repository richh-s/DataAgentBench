code = """import json

reviews = var_call_ToJKCtsPgiglHhwnH71Y3Fxl
businesses = var_call_xYmcKNIfb7fD4mD31kanvCfB

biz_map = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in reviews:
    g = r['gmap_id']
    result.append({
        'business_name': biz_map.get(g, ''),
        'gmap_id': g,
        'high_rating_review_count_2019': int(r['high_review_count'])
    })

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_ToJKCtsPgiglHhwnH71Y3Fxl': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_7IdmBqicWA8lzaAsfWS90IOd': ['business_description'], 'var_call_xYmcKNIfb7fD4mD31kanvCfB': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
