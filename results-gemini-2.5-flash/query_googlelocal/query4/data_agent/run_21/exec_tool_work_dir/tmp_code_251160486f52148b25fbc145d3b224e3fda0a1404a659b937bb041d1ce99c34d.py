code = """import json
import re

# Access raw string output from the first query_db call for reviews
raw_output_string_reviews = locals()['var_function-call-11092242839921597371']['query_db_response']['results'][0]

# Extract the JSON array string for reviews using regex
json_array_match_reviews = re.search(r'\[.*\]', raw_output_string_reviews)

parsed_reviews_data = []
if json_array_match_reviews:
    parsed_reviews_data = json.loads(json_array_match_reviews.group(0))

gmap_ids = [item['gmap_id'] for item in parsed_reviews_data]
review_counts = {item['gmap_id']: int(item['high_rating_review_count']) for item in parsed_reviews_data}

# Access raw string output from the second query_db call for business info
raw_output_string_business = locals()['var_function-call-5388630985925995340']['query_db_response']['results'][0]

# Extract the JSON array string for business info using regex
json_array_match_business = re.search(r'\[.*\]', raw_output_string_business)

parsed_business_data = []
if json_array_match_business:
    parsed_business_data = json.loads(json_array_match_business.group(0))

# Create a dictionary for easy lookup of business names by gmap_id
business_names_map = {item['gmap_id']: item['name'] for item in parsed_business_data}

# Construct the final answer
final_result_parts = []
for gmap_id in gmap_ids:
    business_name = business_names_map.get(gmap_id, 'Unknown Business') # Use .get to handle missing IDs safely
    count = review_counts.get(gmap_id, 0) # Use .get to handle missing counts safely
    final_result_parts.append(business_name + ": " + str(count) + " high-rating reviews")

final_answer_string = "\n".join(final_result_parts)

print('__RESULT__:')
print(json.dumps(final_answer_string))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-17591554314280437685': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'review_counts': {'gmap_20': '8', 'gmap_53': '7', 'gmap_40': '6'}}, 'var_function-call-5388630985925995340': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
