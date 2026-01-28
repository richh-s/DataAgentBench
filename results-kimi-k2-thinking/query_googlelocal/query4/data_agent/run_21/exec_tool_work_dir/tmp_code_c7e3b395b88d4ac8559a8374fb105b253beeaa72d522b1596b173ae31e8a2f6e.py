code = """import json

# Get the review counts
review_result = [{"gmap_id": "gmap_20", "high_review_count": "8"}, {"gmap_id": "gmap_53", "high_review_count": "7"}, {"gmap_id": "gmap_40", "high_review_count": "6"}]

# Get the business names
business_result = [{"gmap_id": "gmap_20", "name": "Aurora Massage"}, {"gmap_id": "gmap_53", "name": "The Boochyard @ Local Roots"}, {"gmap_id": "gmap_40", "name": "Widows Peak Salon"}]

# Create dictionaries for lookup
review_dict = {item['gmap_id']: int(item['high_review_count']) for item in review_result}
business_dict = {item['gmap_id']: item['name'] for item in business_result}

# Combine and sort
combined = []
for gmap_id in review_dict:
    if gmap_id in business_dict:
        combined.append({
            'name': business_dict[gmap_id],
            'count': review_dict[gmap_id]
        })

combined.sort(key=lambda x: x['count'], reverse=True)

# Build result string
result_lines = []
for idx, item in enumerate(combined, 1):
    line = str(idx) + '. ' + item['name'] + ': ' + str(item['count']) + ' reviews'
    result_lines.append(line)

final_answer = '\n'.join(result_lines)

print('__RESULT__:')
print(final_answer)"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:2': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_functions.query_db:4': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:12': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:14': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}]}

exec(code, env_args)
