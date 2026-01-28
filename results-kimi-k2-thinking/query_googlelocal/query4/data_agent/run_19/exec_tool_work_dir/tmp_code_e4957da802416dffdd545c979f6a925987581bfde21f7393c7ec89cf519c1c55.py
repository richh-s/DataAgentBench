code = """import json

# Get review data from the previous query
review_data = locals()['var_functions.query_db:2']

# Count reviews per gmap_id where rating >= 4.5
from collections import Counter

review_counts = Counter()
for review in review_data:
    rating = float(review['rating'])
    if rating >= 4.5:
        review_counts[review['gmap_id']] += 1

# Convert to list of dicts and sort by count descending
business_reviews = [{'gmap_id': gmap_id, 'high_rating_count': count} 
                   for gmap_id, count in review_counts.most_common()]

print("__RESULT__:")
print(json.dumps(business_reviews[:10]))  # Just print top 10 for preview"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_17', 'rating': '5'}, {'gmap_id': 'gmap_29', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_16', 'rating': '5'}, {'gmap_id': 'gmap_26', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_2', 'rating': '5'}, {'gmap_id': 'gmap_30', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_53', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_72', 'rating': '5'}, {'gmap_id': 'gmap_63', 'rating': '5'}, {'gmap_id': 'gmap_65', 'rating': '5'}, {'gmap_id': 'gmap_51', 'rating': '5'}, {'gmap_id': 'gmap_59', 'rating': '5'}, {'gmap_id': 'gmap_59', 'rating': '5'}, {'gmap_id': 'gmap_57', 'rating': '5'}, {'gmap_id': 'gmap_57', 'rating': '5'}, {'gmap_id': 'gmap_13', 'rating': '5'}, {'gmap_id': 'gmap_14', 'rating': '5'}, {'gmap_id': 'gmap_3', 'rating': '5'}, {'gmap_id': 'gmap_3', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_35', 'rating': '5'}, {'gmap_id': 'gmap_7', 'rating': '5'}, {'gmap_id': 'gmap_7', 'rating': '5'}, {'gmap_id': 'gmap_5', 'rating': '5'}, {'gmap_id': 'gmap_5', 'rating': '5'}, {'gmap_id': 'gmap_34', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_11', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_62', 'rating': '5'}, {'gmap_id': 'gmap_58', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_56', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_46', 'rating': '5'}, {'gmap_id': 'gmap_47', 'rating': '5'}, {'gmap_id': 'gmap_47', 'rating': '5'}, {'gmap_id': 'gmap_71', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_69', 'rating': '5'}, {'gmap_id': 'gmap_64', 'rating': '5'}, {'gmap_id': 'gmap_64', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}]}

exec(code, env_args)
