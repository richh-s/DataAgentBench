code = """import pandas as pd
import json
reviews_data = locals()['var_function-call-12719571196467189363']
df = pd.DataFrame(reviews_data)
df['rating'] = df['rating'].astype(int)

# Group by business_ref to calculate average rating and review count
business_stats = df.groupby('business_ref').agg(
    average_rating=('rating', 'mean'),
    review_count=('business_ref', 'count')
).reset_index()

# Filter for businesses with at least 5 reviews
filtered_businesses = business_stats[business_stats['review_count'] >= 5]

# Find the business with the highest average rating
if not filtered_businesses.empty:
    top_business = filtered_businesses.sort_values(by='average_rating', ascending=False).iloc[0]
    # Extract the business_ref of the top business
    top_business_ref = top_business['business_ref']
    # Convert business_ref to business_id format for the MongoDB query
    top_business_id = top_business_ref.replace('businessref_', 'businessid_')
else:
    top_business_id = None # Handle case where no business meets criteria

print("__RESULT__:")
print(json.dumps(top_business_id))"""

env_args = {'var_function-call-12719571196467189363': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
