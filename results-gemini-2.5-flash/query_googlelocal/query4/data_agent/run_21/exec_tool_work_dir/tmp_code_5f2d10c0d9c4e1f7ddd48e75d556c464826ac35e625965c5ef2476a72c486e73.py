code = """import json

review_data = locals()['var_function-call-17591554314280437685']
business_info = locals()['var_function-call-5388630985925995340']

# Extract gmap_ids and their review counts
gmap_ids = review_data['gmap_ids']
review_counts = {item['gmap_id']: int(item['high_rating_review_count']) for item in review_data['review_counts'].items()}

# Create a dictionary for easy lookup of business names by gmap_id
business_names_map = {item['gmap_id']: item['name'] for item in business_info}

# Construct the final answer
final_result_parts = []
for gmap_id in gmap_ids:
    business_name = business_names_map.get(gmap_id, 'Unknown Business')
    count = review_counts.get(gmap_id, 0)
    final_result_parts.append(f'{business_name}: {count} high-rating reviews')

final_answer_string = '\n'.join(final_result_parts)

print('__RESULT__:')
print(json.dumps(final_answer_string))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-17591554314280437685': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'review_counts': {'gmap_20': '8', 'gmap_53': '7', 'gmap_40': '6'}}, 'var_function-call-5388630985925995340': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
