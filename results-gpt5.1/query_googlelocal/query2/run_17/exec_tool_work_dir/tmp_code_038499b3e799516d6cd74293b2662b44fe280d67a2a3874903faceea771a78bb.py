code = """import json
# Use the stored variables directly
massage_businesses = var_call_JEUiJj0Zr8RJk8SrHgqPUKTd
avg_ratings = var_call_xHbpGp4pbG5qHVYhIMz9UH5Q

# Convert lists to dictionaries for easy lookup
name_lookup = {b['gmap_id']: b['name'] for b in massage_businesses}

result = []
for r in avg_ratings:
    gmap_id = r['gmap_id']
    avg_rating = float(r['avg_rating'])
    name = name_lookup.get(gmap_id, 'Unknown')
    result.append({'business_name': name, 'average_rating': round(avg_rating, 2)})

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_JEUiJj0Zr8RJk8SrHgqPUKTd': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_xHbpGp4pbG5qHVYhIMz9UH5Q': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
