code = """import pandas as pd
import json
import re

high_rating_reviews_full_str = locals()['var_function-call-4277610702218006162']['query_db_response']['results'][0]
business_names_full_str = locals()['var_function-call-10945428614472258574']['query_db_response']['results'][0]

# Use regex to find the JSON array part
high_rating_reviews_match = re.search(r'\[.*\]', high_rating_reviews_full_str, re.DOTALL)
business_names_match = re.search(r'\[.*\]', business_names_full_str, re.DOTALL)

if high_rating_reviews_match and business_names_match:
    high_rating_reviews_json_str = high_rating_reviews_match.group(0)
    business_names_json_str = business_names_match.group(0)

    high_rating_reviews = json.loads(high_rating_reviews_json_str)
    business_names = json.loads(business_names_json_str)

    df_reviews = pd.DataFrame(high_rating_reviews)
    df_businesses = pd.DataFrame(business_names)

    df_reviews['high_rating_reviews_count'] = df_reviews['high_rating_reviews_count'].astype(int)

    merged_df = pd.merge(df_reviews, df_businesses, on='gmap_id')

    merged_df = merged_df.sort_values(by='high_rating_reviews_count', ascending=False)

    result = merged_df[['name', 'high_rating_reviews_count']].to_dict(orient='records')

    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not extract JSON from database query results.'}))"""

env_args = {'var_function-call-4277610702218006162': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-10945428614472258574': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
