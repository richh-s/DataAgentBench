code = """import json
import pandas as pd

# Load the review data
ratings_data = [{"business_ref": "businessref_16", "rating": "1"}, {"business_ref": "businessref_23", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_96", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_47", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_8", "rating": "4"}, {"business_ref": "businessref_43", "rating": "4"}, {"business_ref": "businessref_14", "rating": "3"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_16", "rating": "3"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_30", "rating": "2"}, {"business_ref": "businessref_81", "rating": "1"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_99", "rating": "5"}, {"business_ref": "businessref_40", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_11", "rating": "5"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_8", "rating": "3"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_88", "rating": "5"}, {"business_ref": "businessref_9", "rating": "2"}, {"business_ref": "businessref_71", "rating": "1"}, {"business_ref": "businessref_28", "rating": "5"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_9", "rating": "3"}, {"business_ref": "businessref_17", "rating": "5"}, {"business_ref": "businessref_82", "rating": "4"}]

# Convert to DataFrame
df = pd.DataFrame(ratings_data)
df['rating'] = df['rating'].astype(int)

# Group by business_ref and calculate stats
grouped = df.groupby('business_ref').agg({
    'rating': ['count', 'mean']
}).round(2)

grouped.columns = ['review_count', 'avg_rating']
grouped = grouped.reset_index()

# Filter businesses with at least 5 reviews
filtered = grouped[grouped['review_count'] >= 5]

# Find the business with highest average rating
if not filtered.empty:
    best_business = filtered.loc[filtered['avg_rating'].idxmax()]
    # Debug: Print the filtered businesses sorted by avg_rating
    print("__RESULT__:")
    print(json.dumps({
        'best_business_ref': best_business['business_ref'],
        'best_avg_rating': float(best_business['avg_rating']),
        'best_review_count': int(best_business['review_count']),
        'all_candidates': filtered.sort_values('avg_rating', ascending=False).to_dict('records')
    }, default=str))
else:
    print("__RESULT__:")
    print(json.dumps({'error': 'No business with at least 5 reviews found in the data'}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'review_id': 'reviewid_76', 'user_id': 'userid_793', 'business_ref': 'businessref_16', 'rating': '1', 'useful': '1', 'funny': '1', 'cool': '0', 'text': "Very disappointed. ...here for a News Year's bash and they have no staff to cook and really not even enough servers to take care of everyone. Said 3 cooks didn't show up. Management did not handle well and my guess is that the management is the reason 3 cooks did not show up.", 'date': '2016-01-01 02:46:00'}, {'review_id': 'reviewid_459', 'user_id': 'userid_1397', 'business_ref': 'businessref_23', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "I'm so glad my cousin told me about this place. He said that rather than going to Lowe's or Home Depot, I can find what I need for better price here. It was so true. I bought many things here to work on my car for really good price. I was so lucky. The day I went there they have their 3 days weekend sale. So awesome!", 'date': '2016-06-28 02:18:33'}, {'review_id': 'reviewid_78', 'user_id': 'userid_643', 'business_ref': 'businessref_8', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Uber rocks!! They saved my daughter from being stranded from calling another taxi company that I will never call again. Thank you Uber!!!!', 'date': '2016-03-12 14:19:00'}, {'review_id': 'reviewid_1383', 'user_id': 'userid_938', 'business_ref': 'businessref_9', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Cute, delicious. and cosy. You should go to brunch you there! Friendly service.if you live close to, it is a nice place to meet friends or joy with your love. The veggie  eggs sandwich is delicious!', 'date': '2016-05-24 23:15:00'}, {'review_id': 'reviewid_190', 'user_id': 'userid_144', 'business_ref': 'businessref_96', 'rating': '5', 'useful': '1', 'funny': '1', 'cool': '1', 'text': 'If you want local!!!! Amazing night with great service and a menu that speaks for it self! I really recommend asking for a wine suggestion, Myles will not steer you wrong, nor will any thing from the kitchen! Great food, great drink, great people, means great night! Thank you Farmhaus!!!', 'date': '2016-02-25 04:58:04'}], 'var_functions.query_db:5': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}]}

exec(code, env_args)
