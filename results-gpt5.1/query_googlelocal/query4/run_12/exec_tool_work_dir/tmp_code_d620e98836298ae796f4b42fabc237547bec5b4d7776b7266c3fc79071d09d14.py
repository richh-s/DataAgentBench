code = """import json
reviews = var_call_1H7OV1qEa4buMHrlZXSaXA9l
businesses = var_call_UPTsT7YOSXfZKkYiFJx7oFT9
biz_map = {b['gmap_id']: b['name'] for b in businesses}
result = []
for r in reviews:
    result.append({'business_name': biz_map.get(r['gmap_id'], ''), 'high_rating_reviews_2019': int(r['high_rating_reviews'])})
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_1H7OV1qEa4buMHrlZXSaXA9l': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_call_LbWeAtVEThoHPBRr6udnkWw2': ['business_description'], 'var_call_UPTsT7YOSXfZKkYiFJx7oFT9': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
