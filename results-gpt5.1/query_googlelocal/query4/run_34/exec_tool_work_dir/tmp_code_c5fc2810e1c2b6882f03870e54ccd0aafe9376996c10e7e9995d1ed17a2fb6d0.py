code = """import json
reviews = var_call_eHRLxi81VBmlKEqqyPYAMPgy
businesses = var_call_1ae7hIdk9d3MOgwdiaBFg00k
biz_map = {b['gmap_id']: b['name'] for b in businesses}
result = []
for r in reviews:
    result.append({'business_name': biz_map.get(r['gmap_id'], r['gmap_id']), 'high_rating_review_count_2019': int(r['high_review_count'])})
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_eHRLxi81VBmlKEqqyPYAMPgy': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_v9QBweL9m5kjznhQRlEmXR5D': ['business_description'], 'var_call_1ae7hIdk9d3MOgwdiaBFg00k': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
