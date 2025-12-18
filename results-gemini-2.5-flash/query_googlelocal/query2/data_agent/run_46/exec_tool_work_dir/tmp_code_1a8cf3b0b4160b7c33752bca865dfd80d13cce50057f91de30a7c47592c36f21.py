code = """import pandas as pd
import json

massage_businesses = locals()['var_function-call-374750667616518621']
ratings = locals()['var_function-call-12208699052270239960']

massage_businesses_df = pd.DataFrame(massage_businesses)
ratings_df = pd.DataFrame(ratings)

merged_df = pd.merge(massage_businesses_df, ratings_df, on='gmap_id')

result_list = []
for index, row in merged_df.iterrows():
    result_list.append(f"{row['name']}: {float(row['average_rating']):.1f}")

final_answer = "; ".join(result_list)

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-16730726033356625513': [], 'var_function-call-3138104655230594539': [], 'var_function-call-374750667616518621': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-17725908768388484088': "'gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_21', 'gmap_28'", 'var_function-call-12208699052270239960': [{'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'average_rating': '5.0'}]}

exec(code, env_args)
