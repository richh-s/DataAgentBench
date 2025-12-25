code = """import json

massage_businesses = var_call_2ufxXDifxir8ImWb9JrMhSbu
avg_ratings = var_call_nnA7h3kKqCMH8I33rAUit7FX

avg_rating_dict = {item['gmap_id']: float(item['avg_rating']) for item in avg_ratings}

result = []
for biz in massage_businesses:
    gmap_id = biz['gmap_id']
    if gmap_id in avg_rating_dict and avg_rating_dict[gmap_id] >= 4.0:
        result.append({
            'business_name': biz['name'],
            'average_rating': round(avg_rating_dict[gmap_id], 2)
        })

result_json = json.dumps(result)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_2ufxXDifxir8ImWb9JrMhSbu': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_nnA7h3kKqCMH8I33rAUit7FX': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
