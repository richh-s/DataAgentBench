code = """import json
# Retrieve results from storage
review_top_counts = locals()['var_functions.query_db:4']
business_names = locals()['var_functions.query_db:2']
# Build a mapping from gmap_id to name
name_map = {b['gmap_id']: b['name'] for b in business_names}
# Combine results
combined = []
for rec in review_top_counts:
    combined.append({'name': name_map.get(rec['gmap_id'], 'Unknown'), 'high_rating_count': int(rec['high_rating_count'])})
# Sort by count descending (already sorted)
# Print result as JSON string
print('__RESULT__:')
print(json.dumps(combined, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}, {'gmap_id': 'gmap_35', 'high_rating_count': '6'}, {'gmap_id': 'gmap_72', 'high_rating_count': '5'}, {'gmap_id': 'gmap_62', 'high_rating_count': '5'}, {'gmap_id': 'gmap_46', 'high_rating_count': '5'}, {'gmap_id': 'gmap_17', 'high_rating_count': '4'}, {'gmap_id': 'gmap_69', 'high_rating_count': '3'}, {'gmap_id': 'gmap_56', 'high_rating_count': '3'}, {'gmap_id': 'gmap_2', 'high_rating_count': '3'}, {'gmap_id': 'gmap_11', 'high_rating_count': '3'}, {'gmap_id': 'gmap_7', 'high_rating_count': '2'}, {'gmap_id': 'gmap_64', 'high_rating_count': '2'}, {'gmap_id': 'gmap_59', 'high_rating_count': '2'}, {'gmap_id': 'gmap_57', 'high_rating_count': '2'}, {'gmap_id': 'gmap_5', 'high_rating_count': '2'}, {'gmap_id': 'gmap_47', 'high_rating_count': '2'}, {'gmap_id': 'gmap_3', 'high_rating_count': '2'}, {'gmap_id': 'gmap_71', 'high_rating_count': '1'}, {'gmap_id': 'gmap_65', 'high_rating_count': '1'}, {'gmap_id': 'gmap_63', 'high_rating_count': '1'}, {'gmap_id': 'gmap_58', 'high_rating_count': '1'}, {'gmap_id': 'gmap_51', 'high_rating_count': '1'}, {'gmap_id': 'gmap_34', 'high_rating_count': '1'}, {'gmap_id': 'gmap_30', 'high_rating_count': '1'}, {'gmap_id': 'gmap_29', 'high_rating_count': '1'}, {'gmap_id': 'gmap_26', 'high_rating_count': '1'}, {'gmap_id': 'gmap_16', 'high_rating_count': '1'}, {'gmap_id': 'gmap_14', 'high_rating_count': '1'}, {'gmap_id': 'gmap_13', 'high_rating_count': '1'}], 'var_functions.query_db:2': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}], 'var_functions.query_db:4': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}]}

exec(code, env_args)
