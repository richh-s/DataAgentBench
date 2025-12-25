code = """import json, pandas as pd
from pathlib import Path

# Load reviews from file path stored in var_call_5I1k4jZhBuVuEdHCGdDZnTxB
review_path = Path(var_call_5I1k4jZhBuVuEdHCGdDZnTxB)
with review_path.open() as f:
    reviews = json.load(f)

biz_la = pd.DataFrame(var_call_FJyGstUKLojHcjbtkdVJBzm1)
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# Filter reviews to only those businesses in Los Angeles set (by gmap_id)
la_ids = set(biz_la['gmap_id'])
rev_la = rev_df[rev_df['gmap_id'].isin(la_ids)]

# Compute average rating per business
avg_rating = rev_la.groupby('gmap_id')['rating'].mean().reset_index(name='avg_rating')

# Join with business names
result_df = avg_rating.merge(biz_la, on='gmap_id', how='left')[['name','avg_rating']]

# Sort and take top 5
result_df = result_df.sort_values(by='avg_rating', ascending=False).head(5)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BwLPpnnKDtIIzTFI8Gv2CDGP': [], 'var_call_5I1k4jZhBuVuEdHCGdDZnTxB': 'file_storage/call_5I1k4jZhBuVuEdHCGdDZnTxB.json', 'var_call_9dRKUbWMAqTLOt7JEf6DXOUm': ['business_description'], 'var_call_FJyGstUKLojHcjbtkdVJBzm1': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
