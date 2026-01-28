code = """import json
import pandas as pd
from datetime import datetime
import re

# The result from query_db is stored in a file
file_path = var_functions.query_db:7
print(f'Loading data from file: {file_path}')

# Load the data from the file
with open(file_path, 'r') as f:
    reviews = json.load(f)

print(f'Total reviews with rating >= 4.5: {len(reviews)}')

# Show sample of time formats
sample_times = [r['time'] for r in reviews[:5]]
print('Sample time formats:')
for t in sample_times:
    print(f'  "{t}"')

# Simple year extraction - look for year in the string
reviews_2019 = []
for review in reviews:
    time_str = review['time']
    rating = float(review['rating'])
    gmap_id = review['gmap_id']
    
    # Look for 2019 in the time string
    if '2019' in str(time_str):
        reviews_2019.append({
            'gmap_id': gmap_id,
            'rating': rating,
            'time': time_str
        })

print(f'\nReviews containing "2019" with rating >= 4.5: {len(reviews_2019)}')

# Count by gmap_id
from collections import Counter
business_counts = Counter([r['gmap_id'] for r in reviews_2019])
top_businesses = business_counts.most_common(10)

print('\nTop 10 businesses by high-rating review count (2019):')
for gmap_id, count in top_businesses:
    print(f'  {gmap_id}: {count}')

# Get the top business IDs to query
result = {
    'gmap_ids_to_query': [b[0] for b in top_businesses],
    'business_counts': dict(business_counts)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
