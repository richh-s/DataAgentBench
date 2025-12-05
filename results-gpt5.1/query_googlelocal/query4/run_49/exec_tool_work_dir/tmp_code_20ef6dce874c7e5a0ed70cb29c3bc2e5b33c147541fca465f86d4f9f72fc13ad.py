code = """import json
reviews = var_call_f8M2pHESbdaGXB39oRUowNTo
businesses = var_call_Zff72W26hGBCtgOqKfPTf9PT

biz_map = {b['gmap_id']: b['name'] for b in businesses}
results = []
for r in reviews:
    results.append({
        'business_name': biz_map.get(r['gmap_id'], None),
        'high_rating_review_count_2019': int(r['high_review_count'])
    })

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_f8M2pHESbdaGXB39oRUowNTo': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_NxNa7Na9SgUzKfOJwtMG0uQS': ['business_description'], 'var_call_Zff72W26hGBCtgOqKfPTf9PT': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
