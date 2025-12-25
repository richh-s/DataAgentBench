code = """import pandas as pd
import json
reviews_data = locals()['var_function-call-2246860594945943576']
df_reviews = pd.DataFrame(reviews_data)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
business_stats = df_reviews.groupby('business_ref').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count'))
filtered_businesses = business_stats[business_stats['review_count'] >= 5]
highest_rated_business = filtered_businesses.loc[filtered_businesses['average_rating'].idxmax()]
business_ref_highest_rated = highest_rated_business.name
business_id_highest_rated = business_ref_highest_rated.replace("businessref_", "businessid_")
print("__RESULT__:")
print(json.dumps(business_id_highest_rated))"""

env_args = {'var_function-call-2246860594945943576': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
