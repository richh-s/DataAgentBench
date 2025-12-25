code = """import json
import pandas as pd

# Load previous results
stats_json = locals()['var_function-call-9363640875484465070']
# It was printed, but not saved as a variable I can easily access if I didn't save it. 
# Wait, I can't access the stdout of previous call directly as a variable.
# I have to re-compute or trust the previous output.
# The previous output was:
# [{"state": "AB", ...}, {"state": "MO", "meta_review_count": 2243, ...}, ...]

# I will assume the previous calculation is correct, but I want to be sure about duplicates.
# I will rewrite the script to be robust and just print the final answer details.

business_file = locals()['var_function-call-9893054291285073302']
with open(business_file, 'r') as f:
    business_data = json.load(f)

review_file = locals()['var_function-call-3182767599418943263']
with open(review_file, 'r') as f:
    review_data = json.load(f)

# Extract State
import re
def extract_state(desc):
    if not desc: return None
    match = re.search(r',\s([A-Z]{2}),\sthis', desc)
    if match:
        return match.group(1)
    return None

biz_list = []
seen_bids = set()
for b in business_data:
    bid = b['business_id']
    if bid in seen_bids: continue
    seen_bids.add(bid)
    
    state = extract_state(b.get('description', ''))
    if state and state != 'AB': # Exclude non-US
        rc = int(b.get('review_count', 0)) if 'review_count' in b else 0
        biz_list.append({'business_id': bid, 'state': state, 'meta_rc': rc})

df_biz = pd.DataFrame(biz_list)

# Reviews
def fix_id(ref):
    return ref.replace('businessref_', 'businessid_')

rev_list = []
for r in review_data:
    rev_list.append({'business_id': fix_id(r['business_ref']), 'rating': int(r['rating'])})
df_rev = pd.DataFrame(rev_list)

# 1. State with highest reviews (meta)
# Sum meta_rc per state
state_reviews = df_biz.groupby('state')['meta_rc'].sum().reset_index().sort_values('meta_rc', ascending=False)
top_state = state_reviews.iloc[0]
top_state_name = top_state['state']
top_state_count = top_state['meta_rc']

# 2. Average rating for that state
# Filter businesses for that state
biz_in_state = df_biz[df_biz['state'] == top_state_name]
# Merge with reviews
merged = pd.merge(biz_in_state, df_rev, on='business_id', how='inner')

# Calculate average rating of businesses
# First, avg per business
avg_per_biz = merged.groupby('business_id')['rating'].mean()
# Then avg of those
final_avg = avg_per_biz.mean()

print("__RESULT__:")
print(json.dumps({
    "top_state": top_state_name,
    "review_count": int(top_state_count),
    "average_rating": final_avg
}))"""

env_args = {'var_function-call-16914149954444807717': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-11264158358114755094': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-14303431009496893976': [{'count_star()': '2000'}], 'var_function-call-9424179990217699425': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-3182767599418943263': 'file_storage/function-call-3182767599418943263.json', 'var_function-call-9000871186794463159': [{'state': 'CA', 'review_count_rows': 6, 'review_count_meta': 0, 'avg_rating_of_businesses': 4.1666666667}, {'state': 'FL', 'review_count_rows': 4, 'review_count_meta': 0, 'avg_rating_of_businesses': 4.0}, {'state': 'ID', 'review_count_rows': 33, 'review_count_meta': 0, 'avg_rating_of_businesses': 3.2121212121}, {'state': 'IN', 'review_count_rows': 23, 'review_count_meta': 0, 'avg_rating_of_businesses': 3.5217391304}, {'state': 'MO', 'review_count_rows': 42, 'review_count_meta': 0, 'avg_rating_of_businesses': 3.9047619048}], 'var_function-call-9893054291285073302': 'file_storage/function-call-9893054291285073302.json', 'var_function-call-9363640875484465070': [{'state': 'AB', 'meta_review_count': 45, 'review_row_count': 45, 'avg_rating_of_businesses': 3.1882478632}, {'state': 'AZ', 'meta_review_count': 11, 'review_row_count': 13, 'avg_rating_of_businesses': 3.3846153846}, {'state': 'CA', 'meta_review_count': 92, 'review_row_count': 75, 'avg_rating_of_businesses': 3.2494949495}, {'state': 'FL', 'meta_review_count': 559, 'review_row_count': 400, 'avg_rating_of_businesses': 3.182128326}, {'state': 'ID', 'meta_review_count': 209, 'review_row_count': 126, 'avg_rating_of_businesses': 3.6687145849}, {'state': 'IL', 'meta_review_count': 35, 'review_row_count': 28, 'avg_rating_of_businesses': 3.4246031746}, {'state': 'IN', 'meta_review_count': 226, 'review_row_count': 176, 'avg_rating_of_businesses': 3.4252396172}, {'state': 'LA', 'meta_review_count': 255, 'review_row_count': 125, 'avg_rating_of_businesses': 3.2432039482}, {'state': 'MO', 'meta_review_count': 2243, 'review_row_count': 213, 'avg_rating_of_businesses': 3.996022569}, {'state': 'NJ', 'meta_review_count': 31, 'review_row_count': 27, 'avg_rating_of_businesses': 4.119047619}, {'state': 'NV', 'meta_review_count': 304, 'review_row_count': 65, 'avg_rating_of_businesses': 3.6607142857}, {'state': 'PA', 'meta_review_count': 1804, 'review_row_count': 617, 'avg_rating_of_businesses': 3.6797667318}, {'state': 'TN', 'meta_review_count': 39, 'review_row_count': 39, 'avg_rating_of_businesses': 3.8055555556}]}

exec(code, env_args)
