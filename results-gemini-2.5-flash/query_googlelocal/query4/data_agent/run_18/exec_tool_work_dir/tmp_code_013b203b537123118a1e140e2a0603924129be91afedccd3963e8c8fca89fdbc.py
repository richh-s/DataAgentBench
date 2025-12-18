code = """import json

# Safely extract the JSON string from the first query_db call result
raw_reviews_output = locals()['var_function-call-2342706987370194765']
reviews_json_str = raw_reviews_output['query_db_response']['results'][0]
parsed_reviews_data = json.loads(reviews_json_str)

high_rating_counts = {item['gmap_id']: int(item['high_rating_reviews_count']) for item in parsed_reviews_data}

# Safely extract the business names from the second query_db call result
business_names_data = locals()['var_function-call-4839898090558093684']

final_results = []
for business in business_names_data:
    gmap_id = business['gmap_id']
    name = business['name']
    count = high_rating_counts.get(gmap_id, 0)
    final_results.append({'name': name, 'high_rating_reviews_count': count})

# Sort the results by count in descending order
final_results_sorted = sorted(final_results, key=lambda x: x['high_rating_reviews_count'], reverse=True)

# Format the output string correctly using single quotes for f-string literals
output_strings = []
for item in final_results_sorted:
    output_strings.append(f'{item['name']}: {item['high_rating_reviews_count']} high-rating reviews')

final_answer = '\n'.join(output_strings)

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-17183965750744105237': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'high_rating_counts': {'gmap_20': 8, 'gmap_53': 7, 'gmap_40': 6}}, 'var_function-call-4839898090558093684': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
