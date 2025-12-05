code = """import json
import pandas as pd

biz = pd.DataFrame(var_call_NJVpYhiJ0BHYErSnc9hIUZZv)
avg = pd.DataFrame(var_call_2SM90d7FE3bXyAeCCkOSAciw)

merged = biz.merge(avg, on='gmap_id')
merged = merged[['name', 'avg_rating']]
merged['avg_rating'] = merged['avg_rating'].astype(float).round(2)
result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NJVpYhiJ0BHYErSnc9hIUZZv': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_2SM90d7FE3bXyAeCCkOSAciw': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
