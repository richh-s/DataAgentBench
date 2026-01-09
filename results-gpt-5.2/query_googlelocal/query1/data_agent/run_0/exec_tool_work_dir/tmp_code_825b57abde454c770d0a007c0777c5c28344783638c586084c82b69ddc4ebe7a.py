code = """import json, pandas as pd

df_b = pd.DataFrame(var_call_alRRZfSaGZ7QHTe4Nvpda0QM)
df_r = pd.DataFrame(var_call_g7VyNfpZuqj8MzrujQcuJdhu)
if not df_r.empty:
    df_r['avg_rating'] = df_r['avg_rating'].astype(float)
    df_r['review_count'] = df_r['review_count'].astype(int)

df = df_r.merge(df_b, on='gmap_id', how='left')
df = df.sort_values(['avg_rating','review_count'], ascending=[False, False]).head(5)
records = df[['name','gmap_id','avg_rating','review_count']].to_dict(orient='records')
result = json.dumps(records)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_HuzZhUyrO8E9uVceEB5PVqFX': [], 'var_call_alRRZfSaGZ7QHTe4Nvpda0QM': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_call_g7VyNfpZuqj8MzrujQcuJdhu': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
