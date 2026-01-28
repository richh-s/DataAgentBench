code = """import json

result_file = locals()['var_functions.query_db:2']
print('Result file path:', result_file)

with open(result_file, 'r') as f:
    reviews_data = json.load(f)

print('Total reviews:', len(reviews_data))

if reviews_data:
    print('First review:', reviews_data[0])

from collections import defaultdict

business_ratings = defaultdict(list)

for review in reviews_data:
    business_ref = review.get('business_ref')
    rating = review.get('rating')
    if business_ref and rating is not None:
        business_ratings[business_ref].append(int(rating))

print('Number of unique businesses:', len(business_ratings))

# Calculate average ratings and filter businesses with >= 5 reviews
business_avg_ratings = {}
for business_ref, ratings in business_ratings.items():
    if len(ratings) >= 5:
        avg_rating = sum(ratings) / len(ratings)
        business_avg_ratings[business_ref] = {
            'avg_rating': avg_rating,
            'review_count': len(ratings)
        }

print('Businesses with >=5 reviews:', len(business_avg_ratings))

if business_avg_ratings:
    sorted_businesses = sorted(business_avg_ratings.items(), key=lambda x: x[1]['avg_rating'], reverse=True)
    print('Top 5 businesses by avg rating:')
    for i, (business_ref, stats) in enumerate(sorted_businesses[:5]):
        print(f"{i+1}. {business_ref}: avg={stats['avg_rating']:.2f}, count={stats['review_count']}")
    
    # Get the top business
    top_business_ref = sorted_businesses[0][0]
    top_stats = sorted_businesses[0][1]
    print('Top business_ref:', top_business_ref)
    
    # Convert businessref_X to businessid_X for MongoDB
    business_id = 'businessid_' + top_business_ref.split('_', 1)[1]
    print('Corresponding business_id:', business_id)
    
    output = {
        'top_business_ref': top_business_ref,
        'top_business_id': business_id,
        'avg_rating': top_stats['avg_rating'],
        'review_count': top_stats['review_count']
    }
    
    print('__RESULT__:')
    print(json.dumps(output))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No businesses with >=5 reviews found'}))"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
