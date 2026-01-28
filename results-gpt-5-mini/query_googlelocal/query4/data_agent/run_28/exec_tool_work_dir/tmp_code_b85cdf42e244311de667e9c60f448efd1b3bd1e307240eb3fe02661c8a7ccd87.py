code = """import json
# Accessing results from earlier query_db calls
reviews = var_call_8994P1z5PAZDY5Wys0p4GzBA
businesses = var_call_b3GZrQ0E74j6LTgoQn1X2ZO9

# Build mapping from gmap_id to name
name_map = {b['gmap_id']: b['name'] for b in businesses}

# Merge and prepare final list, preserving order from reviews
result_list = []
for r in reviews:
    gid = r['gmap_id']
    count = int(r['high_rating_count'])
    name = name_map.get(gid, None)
    result_list.append({'gmap_id': gid, 'name': name, 'high_rating_count': count})

# Convert to JSON string
output = json.dumps(result_list)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_8994P1z5PAZDY5Wys0p4GzBA': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_call_b3GZrQ0E74j6LTgoQn1X2ZO9': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
