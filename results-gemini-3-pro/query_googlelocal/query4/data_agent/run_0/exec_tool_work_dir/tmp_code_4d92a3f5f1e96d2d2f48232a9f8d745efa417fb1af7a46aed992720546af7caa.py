code = """import json
import collections

# Load the reviews
with open(locals()['var_function-call-10349723468955369193'], 'r') as f:
    reviews = json.load(f)

# Filter and count
counts = collections.Counter()
for r in reviews:
    # Check rating
    try:
        rating = float(r.get('rating', 0))
    except:
        continue
    
    if rating < 4.5:
        continue

    # Check time for 2019
    # We use a simple string check because 2019 as a contiguous string likely denotes the year in a date string
    # and unlikely to be 20:19 (time) or other components.
    if '2019' in r.get('time', ''):
        counts[r['gmap_id']] += 1

# Get top 3
top_3 = counts.most_common(3)
print('__RESULT__:')
print(json.dumps(top_3))"""

env_args = {'var_function-call-15087257999464423280': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-12618490797306939002': [{'gmap_id': 'gmap_35', 'cnt': '19'}, {'gmap_id': 'gmap_53', 'cnt': '17'}, {'gmap_id': 'gmap_20', 'cnt': '14'}], 'var_function-call-12236074624300748398': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}], 'var_function-call-10007191116697790151': [{'COUNT(*)': '2000'}], 'var_function-call-10349723468955369193': 'file_storage/function-call-10349723468955369193.json'}

exec(code, env_args)
