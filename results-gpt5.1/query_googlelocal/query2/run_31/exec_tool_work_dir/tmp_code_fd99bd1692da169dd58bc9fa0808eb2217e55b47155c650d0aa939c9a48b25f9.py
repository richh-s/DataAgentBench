code = """import json

businesses = var_call_PE9LdJ4uNkBicB5wpWuqzf5b
ratings = var_call_bbKV2Gv7jDqAqezwA9FfaKoE

rating_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings}

result = []
for b in businesses:
    gid = b['gmap_id']
    if gid in rating_map and rating_map[gid] >= 4.0:
        result.append({'business_name': b['name'], 'avg_rating': round(rating_map[gid], 3)})

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_PE9LdJ4uNkBicB5wpWuqzf5b': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_bbKV2Gv7jDqAqezwA9FfaKoE': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
