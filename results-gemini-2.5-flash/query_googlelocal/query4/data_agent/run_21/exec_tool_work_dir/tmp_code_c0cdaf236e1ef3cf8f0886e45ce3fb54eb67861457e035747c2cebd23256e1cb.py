code = """import json
import re

# Extract and parse review data
raw_reviews_output_string = locals()['var_function-call-11308635617738460926']['query_db_response']['results'][0]
json_reviews_match = re.search(r'\[.*\]', raw_reviews_output_string)
reviews_data = []
if json_reviews_match:
    reviews_data = json.loads(json_reviews_match.group(0))

gmap_id_to_count = {item['gmap_id']: int(item['high_rating_review_count']) for item in reviews_data}

# Extract and parse business data
raw_business_output_string = locals()['var_function-call-5388630985925995340']['query_db_response']['results'][0]
json_business_match = re.search(r'\[.*\]', raw_business_output_string)
business_info_list = []
if json_business_match:
    business_info_list = json.loads(json_business_match.group(0))

business_name_map = {item['gmap_id']: item['name'] for item in business_info_list}

# Combine and format the results
final_results = []
for gmap_id, count in gmap_id_to_count.items():
    business_name = business_name_map.get(gmap_id, 'Unknown Business')
    final_results.append(business_name + ": " + str(count) + " high-rating reviews")

final_answer_string = "\n".join(final_results)

print('__RESULT__:')
print(json.dumps(final_answer_string))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-17591554314280437685': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'review_counts': {'gmap_20': '8', 'gmap_53': '7', 'gmap_40': '6'}}, 'var_function-call-5388630985925995340': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-11308635617738460926': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
