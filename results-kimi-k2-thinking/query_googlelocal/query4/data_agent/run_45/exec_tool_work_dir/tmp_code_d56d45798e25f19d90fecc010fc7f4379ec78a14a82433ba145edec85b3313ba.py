code = """import json

# Get the stored results
review_results = locals().get('var_functions.query_db:6', [])
business_results = locals().get('var_functions.query_db:8', [])

# Create a mapping of gmap_id to business name
business_map = {biz['gmap_id']: biz['name'] for biz in business_results}

# Combine the data
final_results = []
for review in review_results:
    gmap_id = review['gmap_id']
    count = int(review['high_rating_count'])
    name = business_map.get(gmap_id, 'Unknown')
    final_results.append({
        'business_name': name,
        'high_rating_review_count': count
    })

# Sort by count descending (should already be sorted, but just to be safe)
final_results.sort(key=lambda x: x['high_rating_review_count'], reverse=True)

# Print in the required format
print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'gmap_id': 'gmap_35', 'high_rating_count': '19'}, {'gmap_id': 'gmap_53', 'high_rating_count': '17'}, {'gmap_id': 'gmap_20', 'high_rating_count': '14'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}]}

exec(code, env_args)
