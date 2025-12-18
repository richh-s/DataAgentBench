code = """import json

# Safely access the full output from the tool calls
review_db_full_output = locals().get('var_function-call-1719386802118099141')
business_db_full_output = locals().get('var_function-call-3226297274026103404')

print('__RESULT__:')
print(json.dumps({
    'review_db_full_output_type': str(type(review_db_full_output)),
    'review_db_full_output': review_db_full_output,
    'business_db_full_output_type': str(type(business_db_full_output)),
    'business_db_full_output': business_db_full_output
}))"""

env_args = {'var_function-call-1719386802118099141': [{'gmap_id': 'gmap_20', 'high_rating_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_rating_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_rating_reviews': '6'}], 'var_function-call-3226297274026103404': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
