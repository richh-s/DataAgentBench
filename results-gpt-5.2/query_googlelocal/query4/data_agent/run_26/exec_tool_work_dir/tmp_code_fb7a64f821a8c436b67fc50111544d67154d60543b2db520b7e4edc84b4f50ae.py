code = """import json, pandas as pd

top = pd.DataFrame(var_call_K9Gdui3w8b2KPRuJZO9qxbC9)
biz = pd.DataFrame(var_call_4ELYvL5w6KFV2jsXp5gpxnZ6)

top['high_rating_reviews_2019'] = top['high_rating_reviews_2019'].astype(int)
res = top.merge(biz, on='gmap_id', how='left')[['name','high_rating_reviews_2019']]
res = res.sort_values('high_rating_reviews_2019', ascending=False)

print('__RESULT__:')
print(res.to_json(orient='records'))"""

env_args = {'var_call_K9Gdui3w8b2KPRuJZO9qxbC9': [{'gmap_id': 'gmap_20', 'high_rating_reviews_2019': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_2019': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_2019': '6'}], 'var_call_GHhWtclc8ymmEHtVuKUaeAui': [{'time': '01 Apr 2021, 21:28', 'n': '1'}, {'time': '01 Aug 2019, 23:51', 'n': '1'}, {'time': '01 Dec 2018, 17:08', 'n': '1'}, {'time': '01 Feb 2021, 00:13', 'n': '1'}, {'time': '01 Jan 2017, 08:20', 'n': '1'}], 'var_call_lhoEtEGg1lgKLAFNVQG2xtHP': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles'}], 'var_call_4ELYvL5w6KFV2jsXp5gpxnZ6': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
