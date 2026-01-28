code = """import json, pandas as pd

df_counts = pd.DataFrame(var_call_l9gAJDk9KjCj1KIdjGxibnjg)
df_names = pd.DataFrame(var_call_TY4E6fHKegR7JHXo7cdeiG1p)

df_counts['high_rating_reviews_2019'] = df_counts['high_rating_reviews_2019'].astype(int)
res = df_counts.merge(df_names, on='gmap_id', how='left')[['name','high_rating_reviews_2019']]
res = res.sort_values('high_rating_reviews_2019', ascending=False).reset_index(drop=True)

lines = []
for idx, row in res.iterrows():
    lines.append(str(idx+1) + '. ' + str(row['name']) + ' — ' + str(int(row['high_rating_reviews_2019'])))
answer = 'Top 3 businesses by count of reviews with rating >= 4.5 in 2019:' + '\n' + '\n'.join(lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_l9gAJDk9KjCj1KIdjGxibnjg': [{'gmap_id': 'gmap_20', 'high_rating_reviews_2019': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_2019': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_2019': '6'}], 'var_call_TY4E6fHKegR7JHXo7cdeiG1p': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
