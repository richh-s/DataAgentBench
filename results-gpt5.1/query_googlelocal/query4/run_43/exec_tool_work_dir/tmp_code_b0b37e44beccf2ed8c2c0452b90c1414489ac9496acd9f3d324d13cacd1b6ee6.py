code = """import json
import pandas as pd

reviews = var_call_gKnIdVassHQe54X1OuFQKKQF
businesses = var_call_zL7kRwho11gQDaZanPvROzxC

reviews_df = pd.DataFrame(reviews)
businesses_df = pd.DataFrame(businesses)

merged = pd.merge(reviews_df, businesses_df, on='gmap_id')
merged['high_rating_reviews'] = merged['high_rating_reviews'].astype(int)

result = merged[['name', 'high_rating_reviews']].sort_values(by='high_rating_reviews', ascending=False).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gKnIdVassHQe54X1OuFQKKQF': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_call_5XdFjLfeco6DQya8a2V2bVhK': ['business_description'], 'var_call_zL7kRwho11gQDaZanPvROzxC': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
