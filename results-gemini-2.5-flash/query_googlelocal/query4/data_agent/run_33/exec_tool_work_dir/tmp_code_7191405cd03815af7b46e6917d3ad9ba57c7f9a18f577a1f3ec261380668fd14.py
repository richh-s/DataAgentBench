code = """import pandas as pd
import json

def extract_json_from_string(s):
    try:
        start_index = s.find('[')
        end_index = s.rfind(']')
        if start_index != -1 and end_index != -1:
            json_str = s[start_index : end_index + 1]
            return json.loads(json_str)
        else:
            return []
    except json.JSONDecodeError:
        return []

review_data_raw = locals()['var_function-call-1719386802118099141']['query_db_response']['results'][0]
business_data_raw = locals()['var_function-call-3226297274026103404']['query_db_response']['results'][0]

review_data = extract_json_from_string(review_data_raw)
business_data = extract_json_from_string(business_data_raw)

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
