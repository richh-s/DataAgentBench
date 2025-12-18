code = """import json

# Extract the full string output from the first query_db call
raw_reviews_output_str = locals()['var_function-call-2342706987370194765']['query_db_response']['results'][0]

# Find the start and end of the JSON array within the string
json_start_index = raw_reviews_output_str.find('[')
json_end_index = raw_reviews_output_str.rfind(']') + 1

# Extract the pure JSON array string
reviews_json_array_str = raw_reviews_output_str[json_start_index:json_end_index]

# Parse the JSON string into a Python list of dictionaries
parsed_reviews_data = json.loads(reviews_json_array_str)

# Create a dictionary for easy lookup of high-rating counts by gmap_id
high_rating_counts = {item['gmap_id']: int(item['high_rating_reviews_count']) for item in parsed_reviews_data}

# Extract the list of business dictionaries from the second query_db call
business_names_list = locals()['var_function-call-4839898090558093684']['query_db_response']['results']

final_results = []
for business in business_names_list:
    gmap_id = business['gmap_id']
    name = business['name']
    # Get the count, defaulting to 0 if gmap_id is not found (though it should be for top 3)
    count = high_rating_counts.get(gmap_id, 0)
    final_results.append({'name': name, 'high_rating_reviews_count': count})

# Sort the results by count in descending order
final_results_sorted = sorted(final_results, key=lambda x: x['high_rating_reviews_count'], reverse=True)

# Format the output string for the final answer
output_strings = []
for item in final_results_sorted:
    output_strings.append(f"{item['name']}: {item['high_rating_reviews_count']} high-rating reviews")

final_answer = '\n'.join(output_strings)

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-17183965750744105237': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'high_rating_counts': {'gmap_20': 8, 'gmap_53': 7, 'gmap_40': 6}}, 'var_function-call-4839898090558093684': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
