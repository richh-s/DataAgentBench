code = """import json

high_reviews = var_call_hJjsUeqVuJ4EwkkvH5ndvX0j
businesses = var_call_D676MDtgoArG0tQtlNB9MDBO

biz_map = {b['gmap_id']: b['name'] for b in businesses}

result = []
for row in high_reviews:
    gmap_id = row['gmap_id']
    result.append({
        'business_name': biz_map.get(gmap_id, None),
        'gmap_id': gmap_id,
        'high_rating_reviews_2019': int(row['high_review_count'])
    })

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_hJjsUeqVuJ4EwkkvH5ndvX0j': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_weZamSCB6x053BTrcXcxmQpq': ['business_description'], 'var_call_D676MDtgoArG0tQtlNB9MDBO': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
