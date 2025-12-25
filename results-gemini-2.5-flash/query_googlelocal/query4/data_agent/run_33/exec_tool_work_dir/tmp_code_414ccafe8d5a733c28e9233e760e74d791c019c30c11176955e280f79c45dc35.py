code = """import pandas as pd
import json

# Directly access the lists of dictionaries from the tool call results
review_data = locals()['var_function-call-1719386802118099141']['query_db_response']['results']
business_data = locals()['var_function-call-3226297274026103404']['query_db_response']['results']

# Create DataFrames from the lists of dictionaries
df_reviews = pd.DataFrame(review_data)
df_business = pd.DataFrame(business_data)

# Ensure 'high_rating_reviews' is numeric for proper sorting
# It's initially a string as seen from the debug output, so convert to int
if not df_reviews.empty and 'high_rating_reviews' in df_reviews.columns:
    df_reviews['high_rating_reviews'] = pd.to_numeric(df_reviews['high_rating_reviews'])

# Merge the dataframes on 'gmap_id'
merged_df = pd.merge(df_reviews, df_business, on='gmap_id', how='inner')

# Sort by 'high_rating_reviews' in descending order and get the top 3
final_result_df = merged_df.sort_values(by='high_rating_reviews', ascending=False).head(3)

# Select the required columns and convert to a list of dictionaries
result_list = final_result_df[['name', 'high_rating_reviews']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-1719386802118099141': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_function-call-3226297274026103404': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-15806951639241683485': {'review_db_full_output_type': "<class 'list'>", 'review_db_full_output': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'business_db_full_output_type': "<class 'list'>", 'business_db_full_output': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}}

exec(code, env_args)
