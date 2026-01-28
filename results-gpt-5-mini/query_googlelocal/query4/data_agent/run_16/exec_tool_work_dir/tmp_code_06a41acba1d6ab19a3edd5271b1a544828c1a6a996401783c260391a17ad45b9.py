code = """import pandas as pd
import json
# load the previous query result
df = pd.DataFrame(var_call_H0L4Ia9iTMVchL4vCqUCubBR)
# convert counts to int
df['high_rating_count'] = df['high_rating_count'].astype(int)
# sort descending and get top 3
top3 = df.sort_values('high_rating_count', ascending=False).head(3)
result = top3.to_dict(orient='records')
# output must be a JSON-serializable string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_H0L4Ia9iTMVchL4vCqUCubBR': [{'gmap_id': 'gmap_11', 'high_rating_count': '3'}, {'gmap_id': 'gmap_13', 'high_rating_count': '1'}, {'gmap_id': 'gmap_14', 'high_rating_count': '1'}, {'gmap_id': 'gmap_16', 'high_rating_count': '1'}, {'gmap_id': 'gmap_17', 'high_rating_count': '4'}, {'gmap_id': 'gmap_2', 'high_rating_count': '3'}, {'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_26', 'high_rating_count': '1'}, {'gmap_id': 'gmap_29', 'high_rating_count': '1'}, {'gmap_id': 'gmap_3', 'high_rating_count': '2'}, {'gmap_id': 'gmap_30', 'high_rating_count': '1'}, {'gmap_id': 'gmap_34', 'high_rating_count': '1'}, {'gmap_id': 'gmap_35', 'high_rating_count': '6'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}, {'gmap_id': 'gmap_46', 'high_rating_count': '5'}, {'gmap_id': 'gmap_47', 'high_rating_count': '2'}, {'gmap_id': 'gmap_5', 'high_rating_count': '2'}, {'gmap_id': 'gmap_51', 'high_rating_count': '1'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_56', 'high_rating_count': '3'}, {'gmap_id': 'gmap_57', 'high_rating_count': '2'}, {'gmap_id': 'gmap_58', 'high_rating_count': '1'}, {'gmap_id': 'gmap_59', 'high_rating_count': '2'}, {'gmap_id': 'gmap_62', 'high_rating_count': '5'}, {'gmap_id': 'gmap_63', 'high_rating_count': '1'}, {'gmap_id': 'gmap_64', 'high_rating_count': '2'}, {'gmap_id': 'gmap_65', 'high_rating_count': '1'}, {'gmap_id': 'gmap_69', 'high_rating_count': '3'}, {'gmap_id': 'gmap_7', 'high_rating_count': '2'}, {'gmap_id': 'gmap_71', 'high_rating_count': '1'}, {'gmap_id': 'gmap_72', 'high_rating_count': '5'}]}

exec(code, env_args)
