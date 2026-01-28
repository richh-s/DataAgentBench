code = """import json

# Business data with names
business_names = [{"name": "Aurora Massage", "gmap_id": "gmap_20"}, {"name": "The Boochyard @ Local Roots", "gmap_id": "gmap_53"}, {"name": "Encino Dermatology & Laser: Alex Khadavi MD", "gmap_id": "gmap_35"}]

# Review counts data
review_counts = [{"gmap_id": "gmap_35", "count": 19}, {"gmap_id": "gmap_53", "count": 17}, {"gmap_id": "gmap_20", "count": 14}]

# Combine the data
result = []
for name_data in business_names:
    for count_data in review_counts:
        if name_data['gmap_id'] == count_data['gmap_id']:
            result.append({
                'business_name': name_data['name'],
                'high_rating_reviews_count': count_data['count']
            })

# Sort by count descending
result = sorted(result, key=lambda x: x['high_rating_reviews_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_41', 'rating': '5', 'time': 'March 07, 2019 at 12:56 AM'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': '18 Jan 2019, 03:19'}, {'gmap_id': 'gmap_41', 'rating': '5', 'time': '06 Jan 2019, 02:45'}, {'gmap_id': 'gmap_43', 'rating': '5', 'time': '14 Jan 2019, 18:29'}, {'gmap_id': 'gmap_38', 'rating': '5', 'time': 'November 07, 2019 at 04:55 PM'}, {'gmap_id': 'gmap_38', 'rating': '5', 'time': 'June 21, 2019 at 10:02 AM'}, {'gmap_id': 'gmap_17', 'rating': '5', 'time': '2019-03-27 20:30:42'}, {'gmap_id': 'gmap_17', 'rating': '5', 'time': '2019-04-04 01:42:28'}, {'gmap_id': 'gmap_17', 'rating': '5', 'time': '29 Nov 2019, 22:57'}, {'gmap_id': 'gmap_17', 'rating': '5', 'time': 'February 15, 2019 at 11:29 AM'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [{'gmap_id': 'gmap_35', 'count': 19}, {'gmap_id': 'gmap_53', 'count': 17}, {'gmap_id': 'gmap_20', 'count': 14}], 'var_functions.query_db:16': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'gmap_id': 'gmap_35'}]}

exec(code, env_args)
