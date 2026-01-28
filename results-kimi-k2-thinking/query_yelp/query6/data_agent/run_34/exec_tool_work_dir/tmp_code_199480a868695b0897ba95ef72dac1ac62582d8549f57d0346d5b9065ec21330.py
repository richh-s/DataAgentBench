code = """import json
import pandas as pd

# Load the review data from the file
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    reviews_data = json.load(f)

# Convert to DataFrame
df_reviews = pd.DataFrame(reviews_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Group by business_ref to calculate average rating and count
grouped = df_reviews.groupby('business_ref').agg({
    'rating': ['mean', 'count']
}).round(2)

# Flatten column names
grouped.columns = ['avg_rating', 'review_count']
grouped = grouped.reset_index()

# Filter businesses with at least 5 reviews
filtered = grouped[grouped['review_count'] >= 5]

# Find business with highest average rating
if not filtered.empty:
    highest_rated = filtered.loc[filtered['avg_rating'].idxmax()]
    business_ref = highest_rated['business_ref']
    avg_rating = highest_rated['avg_rating']
    review_count = highest_rated['review_count']
    
    print('__RESULT__:')
    print(json.dumps({
        'business_ref': business_ref,
        'avg_rating': float(avg_rating),
        'review_count': int(review_count)
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No businesses with >= 5 reviews found'}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
