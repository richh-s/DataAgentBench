code = """import pandas as pd
import json

businesses = locals()['var_function-call-17891663531124021584']
ratings = locals()['var_function-call-7804598537916700556']

df_bus = pd.DataFrame(businesses)
df_rat = pd.DataFrame(ratings)

# Ensure avg_rating is float
df_rat['avg_rating'] = df_rat['avg_rating'].astype(float)

# Merge
df_merged = pd.merge(df_bus, df_rat, on='gmap_id')

# Sort
df_sorted = df_merged.sort_values(by='avg_rating', ascending=False)

# Top 5
top5 = df_sorted.head(5)

# Result list
result = top5[['name', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4378422844185924665': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-17891663531124021584': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-7804598537916700556': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}]}

exec(code, env_args)
