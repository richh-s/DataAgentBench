code = """import pandas as pd
import json

with open(locals()['var_function-call-7312146679102699008'], 'r') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)
df['date_dt'] = pd.to_datetime(df['date'], format='mixed')

start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30')
df['date_only'] = df['date_dt'].dt.date
mask = (df['date_only'] >= start_date.date()) & (df['date_only'] <= end_date.date())

filtered_df = df[mask]

stats = filtered_df.groupby('business_ref').agg(
    avg_rating=('rating', lambda x: x.astype(int).mean()),
    count=('rating', 'count')
).reset_index()

candidates = stats[stats['count'] >= 5]
best = candidates.sort_values(by=['avg_rating', 'count'], ascending=[False, False])

print('__RESULT__:')
print(best.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-10190353216909278636': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'num_reviews': '5'}], 'var_function-call-10190353216909275933': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-12823390688900469514': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}, {'date': '21 May 2016, 18:48'}, {'date': 'November 01, 2021 at 05:11 PM'}], 'var_function-call-12823390688900469755': [{'count_star()': '38'}], 'var_function-call-8051533960699194059': [{'count_star()': '2000'}], 'var_function-call-7312146679102699008': 'file_storage/function-call-7312146679102699008.json', 'var_function-call-15945159040739690715': [{'business_ref': 'businessref_9', 'avg_rating': 4.375, 'count': 16}], 'var_function-call-11738290869539232774': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'review_count': '53', 'is_open': '0', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '7:0-15:0', 'Tuesday': '7:0-15:0', 'Wednesday': '7:0-15:0', 'Thursday': '7:0-15:0', 'Friday': '7:0-15:0', 'Saturday': '8:30-15:0', 'Sunday': '8:30-15:0'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
