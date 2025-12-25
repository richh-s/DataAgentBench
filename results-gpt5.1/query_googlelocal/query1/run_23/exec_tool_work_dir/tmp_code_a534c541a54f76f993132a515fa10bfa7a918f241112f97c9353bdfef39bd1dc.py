code = """import json, pandas as pd

# Load business and review data
biz = pd.DataFrame(var_call_yyIJIDx9X1g3Vf80nSow3QId)

# Read full reviews file
with open(var_call_I3BQ1lIkpqXWzZokpXPSKkTw, 'r') as f:
    reviews = json.load(f)
rev = pd.DataFrame(reviews)
rev['rating'] = rev['rating'].astype(float)

# Filter to businesses in Los Angeles list
rev_la = rev[rev['gmap_id'].isin(biz['gmap_id'])]

# Compute average rating per business
avg = rev_la.groupby('gmap_id')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Join with business names
res = avg.merge(biz, on='gmap_id')

# Sort by avg_rating desc, then by name, and take top 5
res = res.sort_values(['avg_rating','name'], ascending=[False, True]).head(5)

out = res[['name','avg_rating']].to_dict(orient='records')

s = json.dumps(out)
print("__RESULT__:")
print(s)"""

env_args = {'var_call_fkz8eOTHwJbjAgIuQ2R0u6PZ': [], 'var_call_I3BQ1lIkpqXWzZokpXPSKkTw': 'file_storage/call_I3BQ1lIkpqXWzZokpXPSKkTw.json', 'var_call_yyIJIDx9X1g3Vf80nSow3QId': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
