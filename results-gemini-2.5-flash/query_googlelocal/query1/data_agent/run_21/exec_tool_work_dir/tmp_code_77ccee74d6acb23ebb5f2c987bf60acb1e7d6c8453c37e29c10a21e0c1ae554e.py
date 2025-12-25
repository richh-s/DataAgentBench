code = """import pandas as pd
import json
business_names = pd.DataFrame(locals()['var_function-call-14197994293323210524'])
average_ratings = pd.DataFrame(locals()['var_function-call-13088780682888447176'])

# Convert 'average_rating' to numeric type
average_ratings['average_rating'] = pd.to_numeric(average_ratings['average_rating'])

# Merge the two dataframes on 'gmap_id'
merged_df = pd.merge(business_names, average_ratings, on='gmap_id')

# Sort by average_rating in descending order
merged_df_sorted = merged_df.sort_values(by='average_rating', ascending=False)

# Format the output
result = []
for index, row in merged_df_sorted.iterrows():
    result.append(f"{row['name']} (Average Rating: {row['average_rating']:.2f})")

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-6900383694594742960': [], 'var_function-call-4467267142328516668': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-17086340762816615540': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-1175162401444206709': ['gmap_44', 'gmap_41', 'gmap_43', 'gmap_38', 'gmap_39', 'gmap_42', 'gmap_40'], 'var_function-call-13088780682888447176': [{'gmap_id': 'gmap_40', 'average_rating': '4.857142857142857'}, {'gmap_id': 'gmap_44', 'average_rating': '4.5'}, {'gmap_id': 'gmap_38', 'average_rating': '4.285714285714286'}, {'gmap_id': 'gmap_41', 'average_rating': '4.277777777777778'}, {'gmap_id': 'gmap_43', 'average_rating': '3.3333333333333335'}], 'var_function-call-6605739091957771107': ['gmap_40', 'gmap_44', 'gmap_38', 'gmap_41', 'gmap_43'], 'var_function-call-14197994293323210524': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
