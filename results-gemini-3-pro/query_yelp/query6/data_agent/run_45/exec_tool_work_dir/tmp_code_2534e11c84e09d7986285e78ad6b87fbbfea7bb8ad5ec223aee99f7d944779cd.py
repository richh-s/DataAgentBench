code = """import pandas as pd
import json
import datetime

# Load the file
with open(locals()['var_function-call-10301517770834398809'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse dates
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

# Pandas to_datetime is usually smart enough
# But let's verify. 'August 01, 2016 at 03:44 AM' might need format='mixed' or inference
df['dt'] = pd.to_datetime(df['date'], errors='coerce')

# Check for any NaT (parsing failures)
failed = df[df['dt'].isna()]
if not failed.empty:
    print("Failed to parse some dates:", failed['date'].head().tolist())

# Filter by date range
start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30')

# Filter
mask = (df['dt'] >= start_date) & (df['dt'] <= end_date)
filtered_df = df[mask].copy()

# Group by business_ref
# Ensure rating is int/float
filtered_df['rating'] = filtered_df['rating'].astype(float)

grouped = filtered_df.groupby('business_ref').agg(
    avg_rating=('rating', 'mean'),
    review_count=('rating', 'count')
).reset_index()

# Filter review_count >= 5
final_candidates = grouped[grouped['review_count'] >= 5].copy()

# Sort by avg_rating desc
final_candidates = final_candidates.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])

result = final_candidates.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14978894452064213954': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'cnt': '5'}], 'var_function-call-14771199447022269982': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'review_count': '53', 'is_open': '0', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '7:0-15:0', 'Tuesday': '7:0-15:0', 'Wednesday': '7:0-15:0', 'Thursday': '7:0-15:0', 'Friday': '7:0-15:0', 'Saturday': '8:30-15:0', 'Sunday': '8:30-15:0'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}], 'var_function-call-9894634119992344307': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}], 'var_function-call-1242917682017199888': [{'count_star()': '2000'}], 'var_function-call-10301517770834398809': 'file_storage/function-call-10301517770834398809.json'}

exec(code, env_args)
