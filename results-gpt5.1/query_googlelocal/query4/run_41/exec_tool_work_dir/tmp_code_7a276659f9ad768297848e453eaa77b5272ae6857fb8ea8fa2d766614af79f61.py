code = """import json
rev_data = var_call_v91pTLwKpVxvTnqvXeIV8FoG
biz_data = var_call_Pwre6UgxdX4ZaxZfvIJGle7A

# Map gmap_id to business name
id_to_name = {b['gmap_id']: b['name'] for b in biz_data}

result = []
for r in rev_data:
    gmap_id = r['gmap_id']
    result.append({
        'business_name': id_to_name.get(gmap_id, ''),
        'gmap_id': gmap_id,
        'high_rating_review_count_2019': int(r['high_review_count'])
    })

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_v91pTLwKpVxvTnqvXeIV8FoG': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_4xFd7G98BjgOLtbxMKnPLjZG': ['business_description'], 'var_call_Pwre6UgxdX4ZaxZfvIJGle7A': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
