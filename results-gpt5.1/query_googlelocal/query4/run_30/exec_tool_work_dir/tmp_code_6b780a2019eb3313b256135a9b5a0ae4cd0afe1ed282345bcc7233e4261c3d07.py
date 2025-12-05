code = """import json
rev = var_call_Py6bjJwUVjbr5IW4PQZSXal7
biz = var_call_XZheMSPEYaE1VXPuSugPH235

map_counts = {r['gmap_id']: int(r['high_review_count']) for r in rev}

out = []
for b in biz:
    out.append({'business_name': b['name'], 'high_rating_review_count_2019': map_counts.get(b['gmap_id'], 0)})

result = json.dumps(out)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Py6bjJwUVjbr5IW4PQZSXal7': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_NtqYN79iil2NJuB07zEpxSlm': ['business_description'], 'var_call_XZheMSPEYaE1VXPuSugPH235': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
