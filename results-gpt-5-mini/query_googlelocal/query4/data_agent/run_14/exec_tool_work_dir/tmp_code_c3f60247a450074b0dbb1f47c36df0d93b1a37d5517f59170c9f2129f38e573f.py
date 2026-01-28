code = """import pandas as pd
import json
# load results from previous query_db calls
reviews = pd.DataFrame(var_call_ee5B3gjLKC0s4QCPDBlshbYM)
biz = pd.DataFrame(var_call_7Xieh7szEmwifffD78MqI4PK)
# ensure proper types
reviews['cnt'] = reviews['cnt'].astype(int)
# merge and prepare final output
merged = reviews.merge(biz, on='gmap_id', how='left')
merged = merged.sort_values('cnt', ascending=False)
result = merged[['name', 'cnt']].rename(columns={'cnt': 'high_rating_review_count'}).to_dict(orient='records')
# print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ee5B3gjLKC0s4QCPDBlshbYM': [{'gmap_id': 'gmap_20', 'cnt': '8'}, {'gmap_id': 'gmap_53', 'cnt': '7'}, {'gmap_id': 'gmap_40', 'cnt': '6'}], 'var_call_7Xieh7szEmwifffD78MqI4PK': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
