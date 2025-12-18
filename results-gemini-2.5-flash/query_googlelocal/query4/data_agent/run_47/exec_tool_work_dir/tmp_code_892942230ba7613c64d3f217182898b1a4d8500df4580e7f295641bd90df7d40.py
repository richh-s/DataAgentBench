code = """import json
import pandas as pd

# Load data from the previous steps
review_summary_data = locals()['var_function-call-13414491774617247265']['extracted_data']
business_names_data = locals()['var_function-call-5890151419183436796']

# Convert to pandas DataFrames
df_reviews = pd.DataFrame(review_summary_data)
df_businesses = pd.DataFrame(business_names_data)

# Merge the two DataFrames on gmap_id
merged_df = pd.merge(df_reviews, df_businesses, on='gmap_id', how='inner')

# Select and rename columns for the final output
final_result = merged_df[['name', 'high_rating_review_count']].rename(columns={'name': 'Business Name', 'high_rating_review_count': 'High-Rating Review Count'})

# Convert the result to a JSON string
print('__RESULT__:')
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-16734970030880208519': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-13414491774617247265': {'extracted_data': [{'gmap_id': 'gmap_20', 'high_rating_review_count': 8}, {'gmap_id': 'gmap_53', 'high_rating_review_count': 7}, {'gmap_id': 'gmap_40', 'high_rating_review_count': 6}], 'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40']}, 'var_function-call-5890151419183436796': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
