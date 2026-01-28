code = """import json
import pandas as pd

# Load the review data
reviews = [{"business_ref": "businessref_16", "rating": "1"}, {"business_ref": "businessref_23", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_96", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_47", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_8", "rating": "4"}, {"business_ref": "businessref_43", "rating": "4"}, {"business_ref": "businessref_14", "rating": "3"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_16", "rating": "3"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_30", "rating": "2"}, {"business_ref": "businessref_81", "rating": "1"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_99", "rating": "5"}, {"business_ref": "businessref_40", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_11", "rating": "5"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_8", "rating": "3"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_88", "rating": "5"}, {"business_ref": "businessref_9", "rating": "2"}, {"business_ref": "businessref_71", "rating": "1"}, {"business_ref": "businessref_28", "rating": "5"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_9", "rating": "3"}, {"business_ref": "businessref_17", "rating": "5"}, {"business_ref": "businessref_82", "rating": "4"}]

# Convert to DataFrame
df_reviews = pd.DataFrame(reviews)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Group by business_ref and calculate metrics
business_stats = df_reviews.groupby('business_ref').agg({
    'rating': ['count', 'mean']
}).round(2)

business_stats.columns = ['review_count', 'avg_rating']
business_stats = business_stats.reset_index()

# Filter businesses with at least 5 reviews
filtered_businesses = business_stats[business_stats['review_count'] >= 5]

print('Number of businesses with at least 5 reviews:', len(filtered_businesses))
print('\nAll businesses with >= 5 reviews:')
print(filtered_businesses.sort_values('avg_rating', ascending=False))

# Find the business with highest average rating
if not filtered_businesses.empty:
    top_business = filtered_businesses.loc[filtered_businesses['avg_rating'].idxmax()]
    print('\nTop business:')
    print(top_business)
    
    print('__RESULT__:')
    print(json.dumps({
        'top_business_ref': top_business['business_ref'],
        'avg_rating': float(top_business['avg_rating']),
        'review_count': int(top_business['review_count'])
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No businesses with at least 5 reviews found'}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['review', 'tip', 'user'], 'var_functions.query_db:8': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
