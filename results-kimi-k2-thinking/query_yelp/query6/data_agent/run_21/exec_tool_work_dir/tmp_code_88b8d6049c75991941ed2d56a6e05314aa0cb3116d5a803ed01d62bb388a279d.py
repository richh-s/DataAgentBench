code = """import json

# Load the review data
reviews = [{"business_ref": "businessref_16", "rating": "1"}, {"business_ref": "businessref_23", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_96", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_47", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_8", "rating": "4"}, {"business_ref": "businessref_43", "rating": "4"}, {"business_ref": "businessref_14", "rating": "3"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_16", "rating": "3"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_30", "rating": "2"}, {"business_ref": "businessref_81", "rating": "1"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_99", "rating": "5"}, {"business_ref": "businessref_40", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_11", "rating": "5"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_8", "rating": "3"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_88", "rating": "5"}, {"business_ref": "businessref_9", "rating": "2"}, {"business_ref": "businessref_71", "rating": "1"}, {"business_ref": "businessref_28", "rating": "5"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_9", "rating": "3"}, {"business_ref": "businessref_17", "rating": "5"}, {"business_ref": "businessref_82", "rating": "4"}]

# Calculate business statistics
business_stats = {}
for review in reviews:
    business_ref = review['business_ref']
    rating = int(review['rating'])
    
    if business_ref not in business_stats:
        business_stats[business_ref] = {'total_rating': 0, 'review_count': 0}
    
    business_stats[business_ref]['total_rating'] += rating
    business_stats[business_ref]['review_count'] += 1

# Calculate average ratings and filter businesses with at least 5 reviews
eligible_businesses = []
for business_ref, stats in business_stats.items():
    if stats['review_count'] >= 5:
        avg_rating = stats['total_rating'] / stats['review_count']
        eligible_businesses.append({
            'business_ref': business_ref,
            'avg_rating': round(avg_rating, 2),
            'review_count': stats['review_count']
        })

# Find the business with the highest average rating
if eligible_businesses:
    top_business = max(eligible_businesses, key=lambda x: x['avg_rating'])
    result = top_business
else:
    result = {'error': 'No businesses with at least 5 reviews found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['review', 'tip', 'user'], 'var_functions.query_db:8': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
