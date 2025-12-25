code = """import pandas as pd
df = pd.DataFrame(locals()['var_function-call-17796315957228115629'])
df['rating'] = df['rating'].astype(int)
agg_df = df.groupby('business_ref').agg(average_rating=('rating', 'mean'), review_count=('rating', 'count'))
filtered_df = agg_df[agg_df['review_count'] >= 5]
if not filtered_df.empty:
    highest_rated_business = filtered_df.sort_values(by='average_rating', ascending=False).iloc[0]
    business_ref = highest_rated_business.name
    average_rating = highest_rated_business['average_rating']
    result = {'business_ref': business_ref, 'average_rating': average_rating}
else:
    result = {'business_ref': None, 'average_rating': None}
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-17796315957228115629': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
