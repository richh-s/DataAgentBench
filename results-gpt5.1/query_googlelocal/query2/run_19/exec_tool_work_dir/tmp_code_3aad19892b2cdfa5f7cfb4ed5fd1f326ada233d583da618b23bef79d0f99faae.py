code = """import json
ratings = var_call_QbtsrHB5VyIokkZ8AzFSeN41
biz_map = json.loads(var_call_QHk3cx0yvXxZMhr9Lqk8Swtx)
res = []
for r in ratings:
    if float(r['avg_rating']) >= 4.0:
        res.append({'business_name': biz_map[r['gmap_id']], 'average_rating': round(float(r['avg_rating']), 2)})
result = json.dumps(res)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_VD5CXh39YCiQO7Yw5S39f0jc': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_xggnzEfQqixaWDlkdmG8hr2v': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_QbtsrHB5VyIokkZ8AzFSeN41': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}], 'var_call_QHk3cx0yvXxZMhr9Lqk8Swtx': {'gmap_22': 'Angel-A Massage', 'gmap_25': 'Elite Massage', 'gmap_33': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_24': 'SUSY massage', 'gmap_20': 'Aurora Massage', 'gmap_21': 'Orient Massage', 'gmap_28': 'Good Massage'}}

exec(code, env_args)
