code = """import json
reviews = var_call_MFS1XkZlosXmKF961MIo5Z17
businesses = var_call_n7ZAbhSmLmwTV0ZN74FkT5xG

biz_map = {b['gmap_id']: b['name'] for b in businesses}
results = []
for r in reviews:
    results.append({
        'business_name': biz_map.get(r['gmap_id'], None),
        'gmap_id': r['gmap_id'],
        'high_rating_review_count_2019': int(r['high_review_count'])
    })

results_sorted = sorted(results, key=lambda x: x['high_rating_review_count_2019'], reverse=True)

out = json.dumps(results_sorted, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MFS1XkZlosXmKF961MIo5Z17': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_GaTu7lXIkLyGyzUdZb8CzHqh': ['business_description'], 'var_call_n7ZAbhSmLmwTV0ZN74FkT5xG': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
