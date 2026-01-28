code = """import json
rl1 = var_call_DyveMQzNUkkH3eUuFxSEtLqF
rl2 = var_call_l3Eeoapx3scH1dAvEy7hLZYX
name_map = {item['gmap_id']: item['name'] for item in rl2}
result = []
for item in rl1:
    gid = item['gmap_id']
    count = int(item['high_rating_count'])
    name = name_map.get(gid)
    result.append({'name': name, 'gmap_id': gid, 'high_rating_count': count})
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DyveMQzNUkkH3eUuFxSEtLqF': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}], 'var_call_l3Eeoapx3scH1dAvEy7hLZYX': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
