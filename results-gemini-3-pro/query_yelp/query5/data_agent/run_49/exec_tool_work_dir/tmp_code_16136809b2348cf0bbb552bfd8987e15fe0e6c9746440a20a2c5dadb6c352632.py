code = """import json
import re
import pandas as pd

# Load business data
with open(locals()['var_function-call-155350076985845784'], 'r') as f:
    business_list = json.load(f)

# Load review data
with open(locals()['var_function-call-5223981229576103887'], 'r') as f:
    review_list = json.load(f)

valid_states = set([
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
])

business_wifi_map = {}
wifi_businesses = []

for b in business_list:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    desc = b.get('description', '')
    
    # Check WiFi
    has_wifi = False
    if isinstance(attrs, dict):
        wifi = attrs.get('WiFi')
        if wifi:
            w_str = str(wifi).lower()
            if 'free' in w_str or 'paid' in w_str:
                has_wifi = True
    
    if has_wifi:
        # Extract State: Robust Tokenization
        # Replace commas, periods, etc with space
        cleaned = re.sub(r'[^a-zA-Z\s]', ' ', desc)
        tokens = cleaned.split()
        
        found_state = None
        for token in tokens:
            if token in valid_states:
                found_state = token
                break # First one is likely the address state
        
        if found_state:
            business_wifi_map[bid] = found_state
            wifi_businesses.append(bid)

# Aggregate ratings
business_ratings = {}

for r in review_list:
    ref = r.get('business_ref')
    if not ref: continue
    bid = ref.replace("businessref_", "businessid_")
    
    if bid in business_wifi_map:
        if bid not in business_ratings:
            business_ratings[bid] = []
        try:
            val = float(r['rating'])
            business_ratings[bid].append(val)
        except:
            pass

# Compute stats
state_stats = {}

for bid in wifi_businesses:
    # Only count if it has reviews? 
    # The question asks for "average rating for those businesses".
    # If a business has no reviews, it has no rating. 
    # Should I count it in "number of businesses" but ignore for average?
    # "Which U.S. state has the highest number of businesses that offer WiFi, and what is the average rating for those businesses?"
    # If I count it, the denominator for average rating might be different?
    # Usually, we count the business. If it has no rating, we can't average it.
    # I'll count all matching businesses for the "highest number" part.
    # For average rating, I'll average the ratings of those that have ratings.
    
    # Check if business has ratings
    has_ratings = (bid in business_ratings and len(business_ratings[bid]) > 0)
    
    state = business_wifi_map[bid]
    if state not in state_stats:
        state_stats[state] = {'count': 0, 'rating_sum': 0, 'rated_count': 0}
    
    state_stats[state]['count'] += 1
    
    if has_ratings:
        avg_rating = sum(business_ratings[bid]) / len(business_ratings[bid])
        state_stats[state]['rating_sum'] += avg_rating
        state_stats[state]['rated_count'] += 1

results = []
for state, stats in state_stats.items():
    # Average rating for the businesses in the state
    # Sum of avg ratings / Number of rated businesses? 
    # Or Sum of avg ratings / Total businesses (treating others as 0)? 
    # Standard is Avg of those with ratings.
    if stats['rated_count'] > 0:
        final_avg = stats['rating_sum'] / stats['rated_count']
    else:
        final_avg = 0
        
    results.append({
        'state': state,
        'wifi_business_count': stats['count'],
        'average_rating': final_avg
    })

df = pd.DataFrame(results)

if not df.empty:
    df = df.sort_values(by=['wifi_business_count', 'average_rating'], ascending=[False, False])
    print("__RESULT__:")
    print(df.to_json(orient='records'))
else:
    print("__RESULT__:")
    print(json.dumps([]))"""

env_args = {'var_function-call-12018729063848673288': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-18383129836885151947': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-5223981229576103887': 'file_storage/function-call-5223981229576103887.json', 'var_function-call-16152523920283954550': 'Diagnostic run', 'var_function-call-75235322487439254': {'wifi_business_count': 0, 'sample_wifi_map': [], 'matched_reviews_count': 0, 'business_with_ratings_count': 0, 'results': []}, 'var_function-call-10646439285732067685': [{'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}], 'var_function-call-2132553317398968165': ["u'no'"], 'var_function-call-3353983675127029725': 5, 'var_function-call-155350076985845784': 'file_storage/function-call-155350076985845784.json', 'var_function-call-4042586431904707363': {'total_businesses': 100, 'wifi_found': 22, 'state_found': 0, 'matched_reviews': 0, 'sample_desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, 'var_function-call-3386967100850435731': {'matches': [], 'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, 'var_function-call-629527393816129343': [], 'var_function-call-15043502344735440064': [{'desc': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'matches': [], 'valid_overlap': []}, {'desc': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.', 'matches': [], 'valid_overlap': []}, {'desc': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.', 'matches': [], 'valid_overlap': []}, {'desc': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'matches': [], 'valid_overlap': []}, {'desc': 'Located at 7003 Seminole Blvd in Seminole, FL, this establishment specializes in a variety of offerings, including Fast Food, Restaurants, Coffee & Tea, Food, and Burgers, making it a convenient stop for a quick meal or a refreshing beverage.', 'matches': [], 'valid_overlap': []}], 'var_function-call-1549345042865468126': {'desc': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'matches_simple': ['MO'], 'matches_boundary': [], 'split': ['Located at 12337 Olive Blvd in Creve Coeur', ' MO', ' this establishment offers a range of services in Nail Salons', ' Beauty & Spas.']}}

exec(code, env_args)
