code = """import json
import pandas as pd

businesses = pd.DataFrame(var_call_WQ7nRGXAAaql4oCl9nTTtRzc)
ratings = pd.DataFrame(var_call_RiPCT9KLnd6z2fhvTH1RPLNX)

merged = businesses.merge(ratings, on='gmap_id')
merged['avg_rating'] = merged['avg_rating'].astype(float)
merged = merged[['name', 'avg_rating']].sort_values('avg_rating', ascending=False)

result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WQ7nRGXAAaql4oCl9nTTtRzc': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_RiPCT9KLnd6z2fhvTH1RPLNX': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
