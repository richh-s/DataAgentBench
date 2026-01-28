code = """import json

# Get review data from storage
reviews_data = locals()['var_functions.query_db:4']

# Convert to DataFrame
import pandas as pd
df = pd.DataFrame(reviews_data)

# Convert rating to numeric
df['rating'] = pd.to_numeric(df['rating'])

# Group by business_ref and calculate avg rating and review count
grouped = df.groupby('business_ref').agg({
    'rating': ['mean', 'count']
}).round(2)

grouped.columns = ['avg_rating', 'review_count']
grouped = grouped.reset_index()

# Filter for businesses with at least 5 reviews
eligible_businesses = grouped[grouped['review_count'] >= 5].copy()

# Sort by avg_rating descending and get top business
top_business = eligible_businesses.sort_values('avg_rating', ascending=False).head(1)

result_dict = {
    'business_ref': top_business['business_ref'].iloc[0],
    'avg_rating': float(top_business['avg_rating'].iloc[0]),
    'review_count': int(top_business['review_count'].iloc[0])
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.list_db:2': ['review', 'tip', 'user'], 'var_functions.query_db:4': [{'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}, {'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}]}

exec(code, env_args)
