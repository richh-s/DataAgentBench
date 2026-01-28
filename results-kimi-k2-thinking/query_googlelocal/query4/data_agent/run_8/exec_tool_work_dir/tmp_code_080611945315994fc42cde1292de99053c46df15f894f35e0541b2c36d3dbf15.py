code = """import json

# Access the review data from 2019
review_file_path = locals()['var_functions.query_db:8']

if isinstance(review_file_path, str) and review_file_path.endswith('.json'):
    # Read from file if it's a file path
    with open(review_file_path, 'r') as f:
        reviews_2019 = json.load(f)
else:
    # Otherwise use the data directly
    reviews_2019 = locals()['var_functions.query_db:8']

# Filter for ratings >= 4.5
high_rating_reviews = [r for r in reviews_2019 if float(r['rating']) >= 4.5]

# Count reviews per business in 2019 with high ratings
from collections import Counter
business_review_counts = Counter([r['gmap_id'] for r in high_rating_reviews])

# Get top 10 businesses to make sure we have enough data (in case some may not have names)
top_businesses = business_review_counts.most_common(10)

result = {
    'total_high_rating_reviews': len(high_rating_reviews),
    'total_businesses': len(business_review_counts),
    'top_businesses_raw': top_businesses
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2021-04-12 17:07:52', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2018-04-23 16:24:26', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2017-07-10 22:12:19', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:6': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'num_of_reviews': '6'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'num_of_reviews': '18'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'num_of_reviews': '6'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'num_of_reviews': '7'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'num_of_reviews': '6'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
