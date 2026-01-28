code = """import json

review_result = [{"gmap_id": "gmap_20", "high_review_count": "8"}, {"gmap_id": "gmap_53", "high_review_count": "7"}, {"gmap_id": "gmap_40", "high_review_count": "6"}]

business_result = [{"gmap_id": "gmap_20", "name": "Aurora Massage"}, {"gmap_id": "gmap_53", "name": "The Boochyard @ Local Roots"}, {"gmap_id": "gmap_40", "name": "Widows Peak Salon"}]

review_dict = {item['gmap_id']: int(item['high_review_count']) for item in review_result}
business_dict = {item['gmap_id']: item['name'] for item in business_result}

final_list = []
for gmap_id, count in review_dict.items():
    if gmap_id in business_dict:
        final_list.append({
            'business_name': business_dict[gmap_id],
            'high_rating_review_count': count
        })

final_list.sort(key=lambda x: x['high_rating_review_count'], reverse=True)

output = []
for i, business in enumerate(final_list, 1):
    output.append(str(i) + '. ' + business['business_name'] + ': ' + str(business['high_rating_review_count']) + ' reviews')

result = '\n'.join(output)

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:2': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_functions.query_db:4': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:12': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_functions.query_db:14': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}]}

exec(code, env_args)
