code = """import json
import pandas as pd

businesses = pd.DataFrame(var_call_8Kieoyjo8hly9rxnWAm9DQ0k)
ratings = pd.DataFrame(var_call_rn5v8Tp2rVJumJcpGMYtcnkm)

ratings['avg_rating'] = ratings['avg_rating'].astype(float)

merged = businesses.merge(ratings, on='gmap_id')

result_df = merged[merged['avg_rating'] >= 4.0][['name', 'avg_rating']]
result_df['avg_rating'] = result_df['avg_rating'].round(2)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8Kieoyjo8hly9rxnWAm9DQ0k': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_rn5v8Tp2rVJumJcpGMYtcnkm': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
