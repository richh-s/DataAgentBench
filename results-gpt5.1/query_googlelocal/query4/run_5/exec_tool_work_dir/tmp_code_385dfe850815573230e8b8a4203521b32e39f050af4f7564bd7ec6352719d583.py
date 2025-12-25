code = """import json
reviews = var_call_5MlSvj5lMEUWOt5IdG7l9CgU
businesses = var_call_HaCjwwSlFYUp4pa16CIMhapk
merged = []
for r in reviews:
    for b in businesses:
        if r['gmap_id'] == b['gmap_id']:
            merged.append({'business_name': b['name'], 'high_rating_review_count_2019': int(r['high_review_count'])})
merged_sorted = sorted(merged, key=lambda x: x['high_rating_review_count_2019'], reverse=True)
result = json.dumps(merged_sorted)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_5MlSvj5lMEUWOt5IdG7l9CgU': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_6EUhmuqJZ5ZVIVbe2E4Q1kKF': ['business_description'], 'var_call_HaCjwwSlFYUp4pa16CIMhapk': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
