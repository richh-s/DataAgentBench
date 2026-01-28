code = """import json
import pandas as pd

df_reviews = pd.DataFrame(var_call_BLCZqTGGD6zCIf5sRpaem9Oz)
df_business = pd.DataFrame(var_call_HLTSoBdo2rm46KnnO3JZXQo7)

df_reviews['high_count'] = df_reviews['high_count'].astype(int)
merged = df_reviews.merge(df_business, on='gmap_id', how='left')

result = merged.sort_values('high_count', ascending=False)[['name','high_count']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BLCZqTGGD6zCIf5sRpaem9Oz': [{'gmap_id': 'gmap_20', 'high_count': '8'}, {'gmap_id': 'gmap_53', 'high_count': '7'}, {'gmap_id': 'gmap_40', 'high_count': '6'}], 'var_call_HLTSoBdo2rm46KnnO3JZXQo7': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
