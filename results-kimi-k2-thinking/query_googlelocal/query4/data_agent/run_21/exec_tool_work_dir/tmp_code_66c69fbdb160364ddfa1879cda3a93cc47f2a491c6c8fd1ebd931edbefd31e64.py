code = """review_result = [{"gmap_id": "gmap_20", "high_review_count": "8"}, {"gmap_id": "gmap_53", "high_review_count": "7"}, {"gmap_id": "gmap_40", "high_review_count": "6"}]

business_result = [{"gmap_id": "gmap_20", "name": "Aurora Massage"}, {"gmap_id": "gmap_53", "name": "The Boochyard @ Local Roots"}, {"gmap_id": "gmap_40", "name": "Widows Peak Salon"}]

review_dict = {item['gmap_id']: int(item['high_review_count']) for item in review_result}
business_dict = {item['gmap_id']: item['name'] for item in business_result}

combined = []
for gmap_id, count in review_dict.items():
    if gmap_id in business_dict:
        combined.append({'name': business_dict[gmap_id], 'count': count})

combined.sort(key=lambda x: x['count'], reverse=True)

result_str = ''
for idx, item in enumerate(combined, 1):
    result_str = result_str + str(idx) + '. ' + item['name'] + ': ' + str(item['count']) + ' reviews\n'

result_str = result_str.strip()

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:2': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_functions.query_db:4': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:12': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:14': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}]}

exec(code, env_args)
