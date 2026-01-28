code = """import json
# Access previous query results
reviews = var_call_eBESyj9IYcI5bAwXoVd1tjI0
businesses = var_call_qYbJ5bFKjfKtzOaSOgonpRvt
# Build mapping from gmap_id to name
name_map = {b['gmap_id']: b['name'] for b in businesses}
# Convert review counts to int and sort
for r in reviews:
    r['high_count'] = int(r['high_count'])
sorted_reviews = sorted(reviews, key=lambda x: x['high_count'], reverse=True)
# Take top 3
top3 = sorted_reviews[:3]
# Build result list with names and counts
result = []
for r in top3:
    gid = r['gmap_id']
    name = name_map.get(gid, gid)
    result.append({'name': name, 'high_count': r['high_count']})
# Print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eBESyj9IYcI5bAwXoVd1tjI0': [{'gmap_id': 'gmap_20', 'high_count': '8'}, {'gmap_id': 'gmap_53', 'high_count': '7'}, {'gmap_id': 'gmap_40', 'high_count': '6'}, {'gmap_id': 'gmap_35', 'high_count': '6'}, {'gmap_id': 'gmap_72', 'high_count': '5'}, {'gmap_id': 'gmap_62', 'high_count': '5'}, {'gmap_id': 'gmap_46', 'high_count': '5'}, {'gmap_id': 'gmap_17', 'high_count': '4'}, {'gmap_id': 'gmap_69', 'high_count': '3'}, {'gmap_id': 'gmap_56', 'high_count': '3'}, {'gmap_id': 'gmap_2', 'high_count': '3'}, {'gmap_id': 'gmap_11', 'high_count': '3'}, {'gmap_id': 'gmap_7', 'high_count': '2'}, {'gmap_id': 'gmap_64', 'high_count': '2'}, {'gmap_id': 'gmap_59', 'high_count': '2'}, {'gmap_id': 'gmap_57', 'high_count': '2'}, {'gmap_id': 'gmap_5', 'high_count': '2'}, {'gmap_id': 'gmap_47', 'high_count': '2'}, {'gmap_id': 'gmap_3', 'high_count': '2'}, {'gmap_id': 'gmap_71', 'high_count': '1'}, {'gmap_id': 'gmap_65', 'high_count': '1'}, {'gmap_id': 'gmap_63', 'high_count': '1'}, {'gmap_id': 'gmap_58', 'high_count': '1'}, {'gmap_id': 'gmap_51', 'high_count': '1'}, {'gmap_id': 'gmap_34', 'high_count': '1'}, {'gmap_id': 'gmap_30', 'high_count': '1'}, {'gmap_id': 'gmap_29', 'high_count': '1'}, {'gmap_id': 'gmap_26', 'high_count': '1'}, {'gmap_id': 'gmap_16', 'high_count': '1'}, {'gmap_id': 'gmap_14', 'high_count': '1'}, {'gmap_id': 'gmap_13', 'high_count': '1'}], 'var_call_qYbJ5bFKjfKtzOaSOgonpRvt': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
