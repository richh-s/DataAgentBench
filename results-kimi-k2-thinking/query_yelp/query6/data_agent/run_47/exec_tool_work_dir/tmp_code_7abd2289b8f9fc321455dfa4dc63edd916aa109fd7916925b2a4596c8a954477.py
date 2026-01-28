code = """import pandas as pd
import json

# Load the reviews
reviews_data = [
    {"business_ref": "businessref_16", "rating": "1"}, {"business_ref": "businessref_23", "rating": "5"},
    {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"},
    {"business_ref": "businessref_96", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"},
    {"business_ref": "businessref_47", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"},
    {"business_ref": "businessref_8", "rating": "4"}, {"business_ref": "businessref_43", "rating": "4"},
    {"business_ref": "businessref_14", "rating": "3"}, {"business_ref": "businessref_21", "rating": "1"},
    {"business_ref": "businessref_16", "rating": "3"}, {"business_ref": "businessref_31", "rating": "1"},
    {"business_ref": "businessref_30", "rating": "2"}, {"business_ref": "businessref_81", "rating": "1"},
    {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_31", "rating": "1"},
    {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_99", "rating": "5"},
    {"business_ref": "businessref_40", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"},
    {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_11", "rating": "5"},
    {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_9", "rating": "5"},
    {"business_ref": "businessref_8", "rating": "3"}, {"business_ref": "businessref_46", "rating": "5"},
    {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_88", "rating": "5"},
    {"business_ref": "businessref_9", "rating": "2"}, {"business_ref": "businessref_71", "rating": "1"},
    {"business_ref": "businessref_28", "rating": "5"}, {"business_ref": "businessref_71", "rating": "5"},
    {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_9", "rating": "3"},
    {"business_ref": "businessref_17", "rating": "5"}, {"business_ref": "businessref_82", "rating": "4"}
]

reviews_df = pd.DataFrame(reviews_data)
reviews_df['rating'] = reviews_df['rating'].astype(int)

# Calculate review count and average rating per business
business_stats = reviews_df.groupby('business_ref').agg({
    'rating': ['count', 'mean']
}).round(2)

business_stats.columns = ['review_count', 'avg_rating']
business_stats = business_stats.reset_index()

# Filter businesses with at least 5 reviews
business_with_5plus = business_stats[business_stats['review_count'] >= 5]

# Find business with highest average rating
if not business_with_5plus.empty:
    highest_rated = business_with_5plus.loc[business_with_5plus['avg_rating'].idxmax()]
    result = {
        'business_ref': highest_rated['business_ref'],
        'avg_rating': float(highest_rated['avg_rating']),
        'review_count': int(highest_rated['review_count'])
    }
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
