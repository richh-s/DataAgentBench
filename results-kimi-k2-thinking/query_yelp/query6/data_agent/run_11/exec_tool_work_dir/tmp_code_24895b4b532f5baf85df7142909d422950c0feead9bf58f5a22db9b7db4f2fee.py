code = """import json
import pandas as pd

# Get review data from storage
reviews = locals().get('var_functions.query_db:2', [])

if isinstance(reviews, str):
    # If it's a file path, read the file
    with open(reviews, 'r') as f:
        reviews = json.load(f)

# Convert to DataFrame
df_reviews = pd.DataFrame(reviews)

# Show first few rows
print('Review data preview:')
print(df_reviews.head())
print('Total reviews: ' + str(len(df_reviews)))
print('Unique businesses: ' + str(df_reviews['business_ref'].nunique()))

# Calculate average rating and review count per business
business_stats = df_reviews.groupby('business_ref').agg({
    'rating': ['count', 'mean']
}).round(2)

business_stats.columns = ['review_count', 'avg_rating']
business_stats = business_stats.reset_index()

# Filter businesses with at least 5 reviews
filtered_businesses = business_stats[business_stats['review_count'] >= 5]

print('Businesses with >= 5 reviews: ' + str(len(filtered_businesses)))

# Find business with highest average rating
if not filtered_businesses.empty:
    highest_rated = filtered_businesses.loc[filtered_businesses['avg_rating'].idxmax()]
    print('Highest rated business:')
    print(highest_rated)
    
    # Get top 5 for verification
    top_5 = filtered_businesses.nlargest(5, 'avg_rating')
    print('Top 5 businesses:')
    print(top_5)
    
    result = {
        'total_reviews': len(df_reviews),
        'unique_businesses': df_reviews['business_ref'].nunique(),
        'businesses_with_5plus_reviews': len(filtered_businesses),
        'highest_rated_business': highest_rated.to_dict(),
        'top_5_businesses': top_5.to_dict('records')
    }
else:
    print('No businesses with >= 5 reviews found')
    result = {
        'total_reviews': len(df_reviews),
        'unique_businesses': df_reviews['business_ref'].nunique(),
        'businesses_with_5plus_reviews': 0,
        'highest_rated_business': None,
        'top_5_businesses': None
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
