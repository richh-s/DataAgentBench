code = """import json, pandas as pd
# Load full reviews data from file
with open(var_call_4c3ssDvqciF19nSDSutt8bth, 'r') as f:
    reviews = json.load(f)

biz_la = pd.DataFrame(var_call_1jsT5xhaWyo0notNVnrzKG4G)
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

la_reviews = rev_df[rev_df['gmap_id'].isin(biz_la['gmap_id'])]
agg = la_reviews.groupby('gmap_id')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
merged = agg.merge(biz_la, on='gmap_id')

result = merged.sort_values('avg_rating', ascending=False).head(5)
result = result.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1jsT5xhaWyo0notNVnrzKG4G': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_call_4c3ssDvqciF19nSDSutt8bth': 'file_storage/call_4c3ssDvqciF19nSDSutt8bth.json'}

exec(code, env_args)
