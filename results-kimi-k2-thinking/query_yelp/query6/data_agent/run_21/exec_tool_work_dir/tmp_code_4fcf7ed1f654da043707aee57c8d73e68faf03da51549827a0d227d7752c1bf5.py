code = """import json
import pandas as pd

# Load the review data from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as file:
    reviews = json.load(file)

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

# Find the business with highest average rating
if not filtered_businesses.empty:
    top_business = filtered_businesses.loc[filtered_businesses['avg_rating'].idxmax()]
    print('__RESULT__:')
    print(json.dumps({
        'top_business_ref': top_business['business_ref'],
        'avg_rating': float(top_business['avg_rating']),
        'review_count': int(top_business['review_count'])
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No businesses with at least 5 reviews found'}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
