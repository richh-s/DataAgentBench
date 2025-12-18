code = """import json
import re

# Parse review data
raw_reviews_output = locals()['var_function-call-11308635617738460926']['query_db_response']['results'][0]
json_match_reviews = re.search(r'\[.*\]', raw_reviews_output)
reviews_data = []
if json_match_reviews:
    reviews_data = json.loads(json_match_reviews.group(0))

gmap_id_to_count = {item['gmap_id']: int(item['high_rating_review_count']) for item in reviews_data}

# Parse business data
business_data = locals()['var_function-call-5388630985925995340']
business_name_map = {item['gmap_id']: item['name'] for item in business_data}

final_results = []
for gmap_id, count in gmap_id_to_count.items():
    business_name = business_name_map.get(gmap_id, 'Unknown Business')
    final_results.append(business_name + ": " + str(count) + " high-rating reviews")

print('__RESULT__:')
print(json.dumps("\n".join(final_results)))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-17591554314280437685': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'review_counts': {'gmap_20': '8', 'gmap_53': '7', 'gmap_40': '6'}}, 'var_function-call-5388630985925995340': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}], 'var_function-call-11308635617738460926': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}]}

exec(code, env_args)
