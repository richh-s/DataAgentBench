code = """import json

# Get the high rating counts from the previous execute_python step
high_rating_data = json.loads(locals()['var_function-call-17183965750744105237'])
high_rating_counts = high_rating_data['high_rating_counts']

# Get the business names from the query_db step
business_names = locals()['var_function-call-4839898090558093684']

final_results = []
for business in business_names:
    gmap_id = business['gmap_id']
    name = business['name']
    count = high_rating_counts.get(gmap_id, 0) # Use .get to handle cases where gmap_id might not be found
    final_results.append({'name': name, 'high_rating_reviews_count': count})

# Sort the results by count in descending order
final_results_sorted = sorted(final_results, key=lambda x: x['high_rating_reviews_count'], reverse=True)

output_string = ""
for item in final_results_sorted:
    output_string += f"{item['name']}: {item['high_rating_reviews_count']} high-rating reviews\n"

print('__RESULT__:')
print(json.dumps(output_string.strip()))"""

env_args = {'var_function-call-2342706987370194765': [{'gmap_id': 'gmap_20', 'high_rating_reviews_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews_count': '6'}], 'var_function-call-17183965750744105237': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'high_rating_counts': {'gmap_20': 8, 'gmap_53': 7, 'gmap_40': 6}}, 'var_function-call-4839898090558093684': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
