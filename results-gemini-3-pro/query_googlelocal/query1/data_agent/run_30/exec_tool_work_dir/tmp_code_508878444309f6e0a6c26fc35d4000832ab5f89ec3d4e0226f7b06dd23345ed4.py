code = """import pandas as pd
import json

businesses = locals()['var_function-call-7222795603416814757']
ratings = locals()['var_function-call-5004566465326486098']

df_biz = pd.DataFrame(businesses)
df_rate = pd.DataFrame(ratings)

# Ensure avg_rating is float
df_rate['avg_rating'] = df_rate['avg_rating'].astype(float)

# Merge
merged = pd.merge(df_biz, df_rate, on='gmap_id')

# Sort
sorted_df = merged.sort_values(by='avg_rating', ascending=False)

# Top 5
top5 = sorted_df.head(5)

result = top5[['name', 'avg_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8842983142241906803': [{'column_name': 'num_of_reviews', 'data_type': 'bigint'}, {'column_name': 'gmap_id', 'data_type': 'text'}, {'column_name': 'description', 'data_type': 'text'}, {'column_name': 'name', 'data_type': 'text'}, {'column_name': 'hours', 'data_type': 'text'}, {'column_name': 'MISC', 'data_type': 'text'}, {'column_name': 'state', 'data_type': 'text'}], 'var_function-call-8438186459306573336': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-155917521377751831': [{'count': '7'}], 'var_function-call-7222795603416814757': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-5004566465326486098': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}]}

exec(code, env_args)
