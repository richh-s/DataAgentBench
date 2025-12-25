code = """import pandas as pd
import json

businesses = locals()['var_function-call-6462073071456086775']
ratings = locals()['var_function-call-11990486540730321256']

df_bus = pd.DataFrame(businesses)
df_rate = pd.DataFrame(ratings)

# Merge
df_merged = pd.merge(df_bus, df_rate, on='gmap_id')

# Sort
df_merged['avg_rating'] = df_merged['avg_rating'].astype(float)
df_sorted = df_merged.sort_values(by='avg_rating', ascending=False).head(5)

# Result list
result = df_sorted[['name', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12574583361580597533': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-6903007308018672348': [{'count': '7'}], 'var_function-call-6462073071456086775': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-11990486540730321256': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}]}

exec(code, env_args)
