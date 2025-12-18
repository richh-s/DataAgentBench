code = """import json
import re

# Extract and parse review data from the first query result
raw_reviews_output_string = locals()['var_function-call-16409944149724071246']['query_db_response']['results'][0]
json_reviews_match = re.search(r'\[.*\]', raw_reviews_output_string)
reviews_data = []
if json_reviews_match:
    reviews_data = json.loads(json_reviews_match.group(0))

gmap_id_to_count = {item['gmap_id']: int(item['high_rating_review_count']) for item in reviews_data}

# Prepare gmap_ids for the next query
gmap_ids_for_business_query = list(gmap_id_to_count.keys())

print('__RESULT__:')
print(json.dumps({'gmap_ids': gmap_ids_for_business_query, 'review_counts': gmap_id_to_count}))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-17591554314280437685': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'review_counts': {'gmap_20': '8', 'gmap_53': '7', 'gmap_40': '6'}}, 'var_function-call-5388630985925995340': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-11308635617738460926': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-10952425463756548415': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-14387941342019670648': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-10814174147177858831': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-16409944149724071246': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
