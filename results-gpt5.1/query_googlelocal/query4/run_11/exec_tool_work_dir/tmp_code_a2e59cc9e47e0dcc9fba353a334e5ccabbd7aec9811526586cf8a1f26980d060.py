code = """import json
reviews = var_call_BIIKf1YDpFmC0C6rwfUwDuSh
businesses = var_call_0ZtQBgS8D1F5mKaOyZjo0Hg5
biz_map = {b['gmap_id']: b['name'] for b in businesses}
result = []
for r in reviews:
    result.append({'business_name': biz_map.get(r['gmap_id'], ''), 'gmap_id': r['gmap_id'], 'high_rating_review_count_2019': int(r['high_review_count'])})
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_BIIKf1YDpFmC0C6rwfUwDuSh': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_A4Y3IhdIzSJvrmYqkQiZEAtj': ['business_description'], 'var_call_0ZtQBgS8D1F5mKaOyZjo0Hg5': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
