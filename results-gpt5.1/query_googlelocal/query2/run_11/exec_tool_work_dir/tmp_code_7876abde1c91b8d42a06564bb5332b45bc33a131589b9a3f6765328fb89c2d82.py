code = """import json
import pandas as pd

biz = pd.DataFrame(var_call_ZII4xb2ivmqzk30ohD3Xot9q)
avg = pd.DataFrame(var_call_dqUYmOAzy774f4ExeX4sWTEG)
merged = avg.merge(biz, on='gmap_id', how='left')[['name','avg_rating']]
merged['avg_rating'] = merged['avg_rating'].astype(float).round(2)
result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZII4xb2ivmqzk30ohD3Xot9q': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_dqUYmOAzy774f4ExeX4sWTEG': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
