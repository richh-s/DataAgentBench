code = """import json
import pandas as pd

df_names = pd.DataFrame(var_call_7o4nCTGCq4OWBKPZNkJcY0Bl)
df_r = pd.DataFrame(var_call_I7ZbRmAYgHSs0UxuvhE5L147)
# coerce
for c in ['avg_rating','review_count']:
    df_r[c] = pd.to_numeric(df_r[c], errors='coerce')

df = df_r.merge(df_names, on='gmap_id', how='left')
df = df.sort_values(['avg_rating','review_count','name'], ascending=[False,False,True]).head(5)
res = []
for i, row in enumerate(df.itertuples(index=False), start=1):
    res.append({
        'rank': i,
        'business_name': row.name,
        'gmap_id': row.gmap_id,
        'avg_rating': round(float(row.avg_rating), 3) if pd.notna(row.avg_rating) else None,
        'review_count': int(row.review_count) if pd.notna(row.review_count) else None
    })

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_7nWMo7ZFTx3c5aynmw6m9YdO': [], 'var_call_7o4nCTGCq4OWBKPZNkJcY0Bl': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_call_I7ZbRmAYgHSs0UxuvhE5L147': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
