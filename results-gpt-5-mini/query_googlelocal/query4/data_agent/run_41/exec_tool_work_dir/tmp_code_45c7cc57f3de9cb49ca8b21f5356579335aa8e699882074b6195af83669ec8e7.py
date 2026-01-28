code = """import json
# var_call_7K4niadi3iw2LGwuwYlSJ18Z and var_call_P6tLP39HUND8SHPM1v86ChtG are available from previous tool calls
reviews = var_call_7K4niadi3iw2LGwuwYlSJ18Z
businesses = var_call_P6tLP39HUND8SHPM1v86ChtG
# Create mapping from gmap_id to name
name_map = {b['gmap_id']: b.get('name') for b in businesses}
# Build result list with names and counts (convert counts to int)
result = []
for r in reviews:
    gid = r['gmap_id']
    count = int(r['high_rating_count'])
    name = name_map.get(gid, gid)
    result.append({'name': name, 'gmap_id': gid, 'high_rating_count': count})
# Convert to JSON string
output = json.dumps(result)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_7K4niadi3iw2LGwuwYlSJ18Z': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_call_P6tLP39HUND8SHPM1v86ChtG': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
