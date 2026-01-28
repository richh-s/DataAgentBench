code = """import json
reviews = var_call_mKy7jkeURP0SCkrhQd2Ipjf3
businesses = var_call_hZTZLF9FCbemqoOgSJgMoG5z
id_to_name = {b['gmap_id']: b['name'] for b in businesses}
out = []
for r in reviews:
    gid = r['gmap_id']
    count = int(r['high_count'])
    name = id_to_name.get(gid)
    out.append({"name": name, "high_rating_reviews_2019": count})
result = json.dumps(out)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_mKy7jkeURP0SCkrhQd2Ipjf3': [{'gmap_id': 'gmap_20', 'high_count': '8'}, {'gmap_id': 'gmap_53', 'high_count': '7'}, {'gmap_id': 'gmap_40', 'high_count': '6'}], 'var_call_hZTZLF9FCbemqoOgSJgMoG5z': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
