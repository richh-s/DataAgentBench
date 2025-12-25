code = """import json
import re
import pandas as pd

# Load business data
# var_function-call-18383129836885151947 contains the business list
business_list = locals()['var_function-call-18383129836885151947']

# Load review data
# var_function-call-5223981229576103887 contains the path to review json
with open(locals()['var_function-call-5223981229576103887'], 'r') as f:
    review_list = json.load(f)

# Step 1: Identify businesses with WiFi and their State
business_wifi_map = {} # business_id -> state

# Regex for state extraction: looks for ", CA," or " in City, CA," pattern
# Description format: "Located at ... in City, ST, ..."
# We'll split by comma and look for the part that is 2 uppercase letters.
# Example: "Located at ... in Goleta, CA, this..." -> " CA" -> strip -> "CA"

def has_wifi(attrs):
    if not attrs or attrs == "None":
        return False
    
    # attrs might be a string representation of a dict or a dict
    if isinstance(attrs, str):
        # The data preview showed "attributes": "None" (string) or a dict.
        # But wait, looking at the preview: "attributes": {"WiFi": "u'no'", ...}
        # It's a dict. But one entry was "attributes": "None". 
        # Wait, the preview showed: "attributes": "None" for one, and dict for others.
        # Let's handle both.
        if attrs == "None":
            return False
        # If it's a string looking like a dict, we might need eval, but the tool output usually gives parsed JSON.
        # The tool result said: "attributes": {"BusinessAcceptsCreditCards": ...} which is a dict.
        # One entry was "attributes": "None".
        pass
    
    if isinstance(attrs, dict):
        wifi = attrs.get("WiFi")
        if wifi:
            # Check for 'free' or 'paid'
            # Values in preview: "u'no'", presumably "u'free'", "'free'", etc.
            wifi_str = str(wifi).lower()
            if "free" in wifi_str or "paid" in wifi_str:
                return True
    return False

def get_state(desc):
    if not desc:
        return None
    # Strategy: extract text between " in " and ", this".
    # Pattern: "... in [City], [State], this..."
    # Warning: City might not be present or format might differ.
    # Reliable anchor: ", [State], this" or ", [State] " near the end.
    
    # Pattern 1: Look for 2 uppercase letters followed by ", this"
    match = re.search(r',\s([A-Z]{2}),\s(this|the|located)', desc) # "this facility", "this establishment"
    if match:
        return match.group(1)
    
    # Fallback: Look for " in [City], [State],"
    # Split by commas
    parts = desc.split(',')
    # Iterate backwards to find a 2-letter token
    for part in reversed(parts):
        part = part.strip()
        # remove possible " this..."
        if " " in part:
            subparts = part.split()
            if subparts[0].isupper() and len(subparts[0]) == 2 and (len(subparts) > 1 and subparts[1] in ['this', 'the']):
                 return subparts[0]
        
        if len(part) == 2 and part.isupper():
            return part
            
    return None

wifi_businesses = []

for b in business_list:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    desc = b.get('description')
    
    if has_wifi(attrs):
        state = get_state(desc)
        if state:
            business_wifi_map[bid] = state
            wifi_businesses.append(bid)

# Step 2: Aggregate ratings for these businesses
# We need to map review business_ref to business_id.
# review['business_ref'] = "businessref_XX" -> "businessid_XX"

business_ratings = {bid: {'sum': 0, 'count': 0} for bid in wifi_businesses}

for r in review_list:
    ref = r.get('business_ref')
    if not ref: continue
    
    # Convert ref to id
    # assuming format businessref_... -> businessid_...
    bid = ref.replace("businessref_", "businessid_")
    
    if bid in business_ratings:
        try:
            rating = float(r.get('rating', 0))
            business_ratings[bid]['sum'] += rating
            business_ratings[bid]['count'] += 1
        except:
            pass

# Step 3: Calculate stats per state
state_stats = {} # State -> {'business_count': 0, 'total_avg_rating': 0}

for bid, stats in business_ratings.items():
    if stats['count'] > 0:
        avg_rating = stats['sum'] / stats['count']
        state = business_wifi_map[bid]
        
        if state not in state_stats:
            state_stats[state] = {'business_count': 0, 'rating_sum': 0}
        
        state_stats[state]['business_count'] += 1
        state_stats[state]['rating_sum'] += avg_rating

# Find max
results = []
for state, stats in state_stats.items():
    avg_r = stats['rating_sum'] / stats['business_count']
    results.append({
        'state': state,
        'wifi_business_count': stats['business_count'],
        'avg_rating': avg_r
    })

df_results = pd.DataFrame(results).sort_values(by='wifi_business_count', ascending=False)

print("__RESULT__:")
print(df_results.to_json(orient='records'))"""

env_args = {'var_function-call-12018729063848673288': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-18383129836885151947': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-5223981229576103887': 'file_storage/function-call-5223981229576103887.json'}

exec(code, env_args)
