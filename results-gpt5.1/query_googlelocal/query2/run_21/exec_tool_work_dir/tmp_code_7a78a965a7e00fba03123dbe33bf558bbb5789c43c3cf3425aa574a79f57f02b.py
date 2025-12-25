code = """import pandas as pd, json
businesses = pd.DataFrame(var_call_rgHgLGrZGZwtIxydrVhIu6Vq)
ratings = pd.DataFrame(var_call_IuYs5SQWEgbJi76FF6W30S63)
merged = pd.merge(ratings, businesses, on='gmap_id', how='left')
merged = merged[['name','avg_rating']]
result = merged.to_dict(orient='records')
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_rgHgLGrZGZwtIxydrVhIu6Vq': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_IuYs5SQWEgbJi76FF6W30S63': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
