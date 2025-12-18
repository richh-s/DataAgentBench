code = """import json

review_data = locals()['var_function-call-17591554314280437685']
business_data = locals()['var_function-call-5388630985925995340']

gmap_ids = review_data['gmap_ids']
review_counts = {k: int(v) for k, v in review_data['review_counts'].items()}

business_names = {item['gmap_id']: item['name'] for item in business_data}

result = []
for gmap_id in gmap_ids:
    if gmap_id in business_names and gmap_id in review_counts:
        business_name = business_names[gmap_id]
        count = review_counts[gmap_id]
        result.append(business_name + ': ' + str(count) + ' high-rating reviews')

final_answer = '\n'.join(result)

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-11092242839921597371': [{'gmap_id': 'gmap_20', 'high_rating_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_review_count': '6'}], 'var_function-call-17591554314280437685': {'gmap_ids': ['gmap_20', 'gmap_53', 'gmap_40'], 'review_counts': {'gmap_20': '8', 'gmap_53': '7', 'gmap_40': '6'}}, 'var_function-call-5388630985925995340': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
