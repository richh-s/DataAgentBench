code = """import json
import pandas as pd

# Read the reviews from storage
review_data = locals()['var_functions.query_db:2']

# It's a file path string, so read it
with open(review_data, 'r') as f:
    reviews_2016_raw = json.load(f)

# Convert to DataFrame
df_reviews = pd.DataFrame(reviews_2016_raw)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Convert date to datetime
df_reviews['date'] = pd.to_datetime(df_reviews['date'])

# Filter dates between Jan 1 and Jun 30, 2016
start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30 23:59:59')
df_filtered = df_reviews[(df_reviews['date'] >= start_date) & (df_reviews['date'] <= end_date)]

# Group by business and calculate stats
business_stats = df_filtered.groupby('business_ref').agg({
    'rating': ['count', 'mean']
}).round(2)

business_stats.columns = ['review_count', 'avg_rating']

# Filter businesses with at least 5 reviews in this period
businesses_with_5plus = business_stats[business_stats['review_count'] >= 5]

if not businesses_with_5plus.empty:
    # Get business with highest average rating
    best_business_ref = businesses_with_5plus['avg_rating'].idxmax()
    best_business = businesses_with_5plus.loc[best_business_ref]
    
    result = {
        'business_ref': best_business_ref,
        'avg_rating': float(best_business['avg_rating']),
        'review_count': int(best_business['review_count'])
    }
else:
    result = None

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'review_id': 'reviewid_76', 'user_id': 'userid_793', 'business_ref': 'businessref_16', 'rating': '1', 'useful': '1', 'funny': '1', 'cool': '0', 'text': "Very disappointed. ...here for a News Year's bash and they have no staff to cook and really not even enough servers to take care of everyone. Said 3 cooks didn't show up. Management did not handle well and my guess is that the management is the reason 3 cooks did not show up.", 'date': '2016-01-01 02:46:00'}, {'review_id': 'reviewid_459', 'user_id': 'userid_1397', 'business_ref': 'businessref_23', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "I'm so glad my cousin told me about this place. He said that rather than going to Lowe's or Home Depot, I can find what I need for better price here. It was so true. I bought many things here to work on my car for really good price. I was so lucky. The day I went there they have their 3 days weekend sale. So awesome!", 'date': '2016-06-28 02:18:33'}, {'review_id': 'reviewid_78', 'user_id': 'userid_643', 'business_ref': 'businessref_8', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Uber rocks!! They saved my daughter from being stranded from calling another taxi company that I will never call again. Thank you Uber!!!!', 'date': '2016-03-12 14:19:00'}, {'review_id': 'reviewid_1383', 'user_id': 'userid_938', 'business_ref': 'businessref_9', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Cute, delicious. and cosy. You should go to brunch you there! Friendly service.if you live close to, it is a nice place to meet friends or joy with your love. The veggie  eggs sandwich is delicious!', 'date': '2016-05-24 23:15:00'}, {'review_id': 'reviewid_190', 'user_id': 'userid_144', 'business_ref': 'businessref_96', 'rating': '5', 'useful': '1', 'funny': '1', 'cool': '1', 'text': 'If you want local!!!! Amazing night with great service and a menu that speaks for it self! I really recommend asking for a wine suggestion, Myles will not steer you wrong, nor will any thing from the kitchen! Great food, great drink, great people, means great night! Thank you Farmhaus!!!', 'date': '2016-02-25 04:58:04'}, {'review_id': 'reviewid_31', 'user_id': 'userid_321', 'business_ref': 'businessref_8', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Uber is like Mana from Heaven. Quick, cheap and haven't had one bad experience yet. A huge burden has been lifted from dealing with crummy ass All three's", 'date': '2016-05-15 04:34:00'}, {'review_id': 'reviewid_1588', 'user_id': 'userid_1987', 'business_ref': 'businessref_47', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': 'Beautiful place and great service! I got a repair my hair treatment, blowout and makeup! I loved it all. Ask for Tori!', 'date': '2016-06-24 19:38:03'}, {'review_id': 'reviewid_1447', 'user_id': 'userid_306', 'business_ref': 'businessref_37', 'rating': '5', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "I only joined OTF about two weeks ago but I am already obsessed! The workouts are challenging but exiting, each day it's something totally new. I love being held accountable by signing up in advance, I've worked out more in the past two weeks than I have all year long. The trainers are so nice and keep you motivated throughout the class. It's so worth it!", 'date': '2016-06-02 18:48:00'}, {'review_id': 'reviewid_1715', 'user_id': 'None', 'business_ref': 'businessref_8', 'rating': '4', 'useful': '4', 'funny': '1', 'cool': '0', 'text': 'I have never had a problem with Uber in Philadelphia. A couple of times the drivers have gotten lost or been a little unsafe, but nothing major. Uber customer service has been good too, once my driver had no seatbelts in the back seat, and when I reported this they comped my ride. I definitely prefer Uber to taxi drivers who drive very recklessly, talk on the phone, smell like smoke or cologne, etc.', 'date': '2016-02-24 18:52:00'}, {'review_id': 'reviewid_1075', 'user_id': 'userid_1820', 'business_ref': 'businessref_43', 'rating': '4', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Gr8 4 L8 night nosh.  Quick and dependably consistent Mexi-American fast food. Yes, it's the basic items but a very reasonable cost. The wide range of sauce options lets you tailor it to your palate.", 'date': '2016-05-16 22:46:00'}]}

exec(code, env_args)
