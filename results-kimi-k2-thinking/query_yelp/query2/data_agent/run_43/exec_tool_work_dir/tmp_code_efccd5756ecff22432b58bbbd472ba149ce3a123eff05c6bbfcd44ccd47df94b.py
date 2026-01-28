code = """import json
import re

# Load business data
business_data = var_functions.query_db:6

# Load review data from file (it's stored as a file path)
with open(var_functions.query_db:7, 'r') as f:
    review_data = json.load(f)

# Convert to DataFrame for easier processing
import pandas as pd

# Process business data
business_df = pd.DataFrame(business_data)
business_df['review_count'] = pd.to_numeric(business_df['review_count'])

# Extract state from description using regex
# Looking for pattern like "City, State" or "in State"
def extract_state(description):
    # Look for patterns like "City, CA" or "in CA"
    # Common formats: "Goleta, CA", "St. Louis, MO", "Boise, ID", etc.
    if not description or pd.isna(description):
        return None
    
    # Pattern 1: "City, ST" or "Location, ST"
    pattern1 = r',\s*([A-Z]{2})\b'
    match1 = re.search(pattern1, description)
    if match1:
        return match1.group(1)
    
    # Pattern 2: "in State Name, ST"
    pattern2 = r'in\s+[^,]+,\s*([A-Z]{2})\b'
    match2 = re.search(pattern2, description)
    if match2:
        return match2.group(1)
    
    return None

business_df['state'] = business_df['description'].apply(extract_state)

# Process review data
review_df = pd.DataFrame(review_data)
review_df['rating'] = pd.to_numeric(review_df['rating'])

# Extract numeric ID from business_ref for matching
review_df['business_num_id'] = review_df['business_ref'].str.extract('businessref_(\d+)')
business_df['business_num_id'] = business_df['business_id'].str.extract('businessid_(\d+)')

# Merge review data with business data to get state information
merged_df = pd.merge(review_df, business_df[['business_num_id', 'state', 'review_count']], 
                     left_on='business_num_id', right_on='business_num_id', how='left')

# Remove rows where state is None
merged_df = merged_df[merged_df['state'].notna()]

# Calculate total reviews per state (using actual review counts from business collection)
state_reviews = business_df.groupby('state')['review_count'].sum().reset_index()
state_reviews.columns = ['state', 'total_reviews']

# Calculate average rating per state
state_ratings = merged_df.groupby('state')['rating'].mean().reset_index()
state_ratings.columns = ['state', 'avg_rating']

# Find state with highest number of reviews
max_reviews_state = state_reviews.loc[state_reviews['total_reviews'].idxmax()]
max_state = max_reviews_state['state']
max_reviews = int(max_reviews_state['total_reviews'])

# Get average rating for this state
avg_rating = state_ratings[state_ratings['state'] == max_state]['avg_rating'].iloc[0]

# Format result
result = f"{max_state} {max_reviews} {avg_rating:.2f}"

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:6': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
