code = """import json
businesses = var_call_3k0N1bQOfFyHmUllyBMdIE2R
ratings = var_call_oeEcmzjHzk9XKZhezW3e3hst

# Build lookup for names
name_by_id = {b['gmap_id']: b['name'] for b in businesses}

result = []
for r in ratings:
    avg = float(r['avg_rating'])
    if avg >= 4.0:
        result.append({
            'business_name': name_by_id.get(r['gmap_id'], ''),
            'avg_rating': round(avg, 3)
        })

# Sort by business name
result = sorted(result, key=lambda x: x['business_name'])

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3k0N1bQOfFyHmUllyBMdIE2R': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_oeEcmzjHzk9XKZhezW3e3hst': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
