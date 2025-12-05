code = """import json
reviews = var_call_nDH9kUgz7omdxaDFcLdPdAeP
businesses = var_call_uhAcYackuohlgwRarmWr6iTQ

biz_map = {b['gmap_id']: b['name'] for b in businesses}
result = []
for r in reviews:
    result.append({
        'business_name': biz_map.get(r['gmap_id'], ''),
        'high_rating_review_count_2019': int(r['high_review_count'])
    })

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nDH9kUgz7omdxaDFcLdPdAeP': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_MMXIX83PxClPU04k3VruqQMx': ['business_description'], 'var_call_uhAcYackuohlgwRarmWr6iTQ': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
