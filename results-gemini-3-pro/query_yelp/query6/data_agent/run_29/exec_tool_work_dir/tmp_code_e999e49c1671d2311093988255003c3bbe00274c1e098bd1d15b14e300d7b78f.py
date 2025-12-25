code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-8453713206390703534'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert rating to numeric
df['rating'] = pd.to_numeric(df['rating'])

# Convert date. Using pandas to parse mixed formats.
# Try generic parsing
try:
    df['date_dt'] = pd.to_datetime(df['date'], format='mixed')
except:
    # Fallback if format='mixed' is not available (older pandas)
    # But usually plain to_datetime works for these common formats
    df['date_dt'] = pd.to_datetime(df['date'])

# Filter
start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30')

mask = (df['date_dt'] >= start_date) & (df['date_dt'] <= end_date)
df_filtered = df[mask]

# Group
stats = df_filtered.groupby('business_ref').agg(
    review_count=('rating', 'count'),
    avg_rating=('rating', 'mean')
).reset_index()

# Filter count >= 5
stats_qualified = stats[stats['review_count'] >= 5]

# Sort
stats_sorted = stats_qualified.sort_values(by='avg_rating', ascending=False)

print("__RESULT__:")
print(stats_sorted.to_json(orient='records'))"""

env_args = {'var_function-call-6588761948405980191': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_count': '5'}], 'var_function-call-6588761948405977164': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-16681823268498042599': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'review_count': '53', 'is_open': '0', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '7:0-15:0', 'Tuesday': '7:0-15:0', 'Wednesday': '7:0-15:0', 'Thursday': '7:0-15:0', 'Friday': '7:0-15:0', 'Saturday': '8:30-15:0', 'Sunday': '8:30-15:0'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}], 'var_function-call-17812053370905233802': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_count': '5'}], 'var_function-call-17281439515432103704': [{'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-8675235869546256870': [{'count_star()': '2000'}], 'var_function-call-8453713206390703534': 'file_storage/function-call-8453713206390703534.json'}

exec(code, env_args)
