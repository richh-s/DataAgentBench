code = """import pandas as pd
import json
import re

def parse_query_result(result_string):
    # Extract the JSON array string using regex
    match = re.search(r'\[.*\]', result_string, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            return []
    return []

review_data_raw_str = locals()['var_function-call-1719386802118099141']['query_db_response']['results'][0]
business_data_raw_str = locals()['var_function-call-3226297274026103404']['query_db_response']['results'][0]

review_data = parse_query_result(review_data_raw_str)
business_data = parse_query_result(business_data_raw_str)

df_reviews = pd.DataFrame(review_data)
df_business = pd.DataFrame(business_data)

merged_df = pd.merge(df_reviews, df_business, on='gmap_id')
merged_df['high_rating_reviews'] = merged_df['high_rating_reviews'].astype(int)
merged_df_sorted = merged_df.sort_values(by='high_rating_reviews', ascending=False)

result_list = merged_df_sorted[['name', 'high_rating_reviews']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-1719386802118099141': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_function-call-3226297274026103404': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
