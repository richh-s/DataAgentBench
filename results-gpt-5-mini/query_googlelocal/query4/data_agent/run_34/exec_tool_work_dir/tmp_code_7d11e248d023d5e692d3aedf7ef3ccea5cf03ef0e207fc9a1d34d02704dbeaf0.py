code = """import pandas as pd
import json

df_reviews = pd.DataFrame(var_call_DrLUgoQyjrNruvDR03AZU6Qs)
df_business = pd.DataFrame(var_call_hGyFf5SPOUqNHI3HoOVbPQ51)

df_reviews['high_count'] = df_reviews['high_count'].astype(int)
merged = pd.merge(df_business, df_reviews, on='gmap_id', how='left')

top3 = merged.sort_values('high_count', ascending=False).head(3)
result = top3[['name', 'high_count']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DrLUgoQyjrNruvDR03AZU6Qs': [{'gmap_id': 'gmap_20', 'high_count': '8'}, {'gmap_id': 'gmap_53', 'high_count': '7'}, {'gmap_id': 'gmap_40', 'high_count': '6'}, {'gmap_id': 'gmap_35', 'high_count': '6'}, {'gmap_id': 'gmap_72', 'high_count': '5'}, {'gmap_id': 'gmap_62', 'high_count': '5'}, {'gmap_id': 'gmap_46', 'high_count': '5'}, {'gmap_id': 'gmap_17', 'high_count': '4'}, {'gmap_id': 'gmap_69', 'high_count': '3'}, {'gmap_id': 'gmap_56', 'high_count': '3'}], 'var_call_hGyFf5SPOUqNHI3HoOVbPQ51': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
