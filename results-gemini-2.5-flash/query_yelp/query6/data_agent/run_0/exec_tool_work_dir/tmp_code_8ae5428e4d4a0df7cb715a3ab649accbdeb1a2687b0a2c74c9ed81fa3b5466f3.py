code = """import pandas as pd
df_reviews = pd.DataFrame(locals()['var_function-call-95200278783529102'])
df_reviews['rating'] = df_reviews['rating'].astype(int)

business_ratings = df_reviews.groupby('business_ref').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count'))
filtered_businesses = business_ratings[business_ratings['review_count'] >= 5]

if not filtered_businesses.empty:
    top_business = filtered_businesses.sort_values(by='average_rating', ascending=False).iloc[0]
    top_business_ref = top_business.name
    print("__RESULT__:")
    print(pd.Series({'business_ref': top_business_ref, 'average_rating': top_business['average_rating']}).to_json())
else:
    print("__RESULT__:")
    print(pd.Series({'business_ref': None, 'average_rating': None}).to_json())"""

env_args = {'var_function-call-95200278783529102': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
