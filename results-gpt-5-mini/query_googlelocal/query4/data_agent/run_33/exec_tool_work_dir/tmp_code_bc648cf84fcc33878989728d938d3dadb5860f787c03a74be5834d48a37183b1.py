code = """import json
import pandas as pd

df_reviews = pd.DataFrame(var_call_XIwub9YDYzHlZKkq6fA2mTEk)
df_bus = pd.DataFrame(var_call_wgDBxQGndFRzwwwlSoFf4rof)

# Ensure correct types
if 'high_review_count' in df_reviews.columns:
    df_reviews['high_review_count'] = df_reviews['high_review_count'].astype(int)

# Merge to get business names
df_merged = pd.merge(df_reviews, df_bus[['gmap_id', 'name']], on='gmap_id', how='left')

# Prepare output list
output = []
for _, row in df_merged.sort_values('high_review_count', ascending=False).iterrows():
    output.append({'name': row['name'], 'high_review_count': int(row['high_review_count'])})

result_json = json.dumps(output)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_XIwub9YDYzHlZKkq6fA2mTEk': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_wgDBxQGndFRzwwwlSoFf4rof': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'description': ' This vibrant establishment in Vista, CA 92081 specializes in crafting a diverse selection of artisanal beers, offering a cozy atmosphere for tasting and enjoying unique local brews.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
