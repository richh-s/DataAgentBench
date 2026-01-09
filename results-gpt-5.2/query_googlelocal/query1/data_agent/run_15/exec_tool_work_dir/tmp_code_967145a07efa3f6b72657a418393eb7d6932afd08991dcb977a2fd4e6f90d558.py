code = """import json, pandas as pd
biz = pd.DataFrame(var_call_OXVhKqgEIOjV8ckBk5ft1XPD)
ratings = pd.DataFrame(var_call_8Ce3q0E92z9iLUbQ4z04xXEE)
ratings['avg_rating'] = ratings['avg_rating'].astype(float)
ratings['review_count'] = ratings['review_count'].astype(int)
out = ratings.merge(biz, on='gmap_id', how='left')[['name','gmap_id','avg_rating','review_count']]
out = out.sort_values(['avg_rating','review_count','name'], ascending=[False,False,True]).head(5)
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Fxs4hWNZf6WcQ1nyVTrT0t1i': [], 'var_call_OXVhKqgEIOjV8ckBk5ft1XPD': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_call_8Ce3q0E92z9iLUbQ4z04xXEE': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
