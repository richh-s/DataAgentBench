code = """import json, pandas as pd

df_counts = pd.DataFrame(var_call_8jauIMeeWiDrHomMhfw8XlEp)
df_names = pd.DataFrame(var_call_ecJ2MjrHq2ttSpE4Xb76T9RP)

df_counts['high_rating_reviews_2019'] = df_counts['high_rating_reviews_2019'].astype(int)

out = (df_counts.merge(df_names, on='gmap_id', how='left')
       .sort_values(['high_rating_reviews_2019','name'], ascending=[False, True])
       [['name','high_rating_reviews_2019']]
       .to_dict(orient='records'))

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8jauIMeeWiDrHomMhfw8XlEp': [{'gmap_id': 'gmap_20', 'high_rating_reviews_2019': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_2019': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_2019': '6'}], 'var_call_ecJ2MjrHq2ttSpE4Xb76T9RP': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
