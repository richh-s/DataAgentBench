code = """import pandas as pd
import re
import json

# Load business data from file
file_path = locals()['var_function-call-12053795473695309539']
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Regex to extract state
# Format examples:
# "Located at ... in Goleta, CA, this..." -> CA
# "This Philadelphia, PA location offers..." -> PA
# "Located in Pennsauken, NJ, this..." -> NJ
# Pattern: looks for 2 uppercase letters followed by comma, or before "location" or before "this".
# Robust pattern: `, ([A-Z]{2})[,\s]` or `\s([A-Z]{2})\s+location`?
# Most common format: `in [City], [State],`
# Or `This [City], [State] location`
# Let's try to find the state code using a comprehensive regex.
# It seems the state is always 2 uppercase letters.
# It is usually followed by a comma or space.
# It is often preceded by a city name (which is variable).

parsed_data = []
# Compile regexes
# 1. Standard: "in City, ST," or "in City, ST "
p1 = re.compile(r"in\s+[^,]+,\s+([A-Z]{2})")
# 2. "This City, ST location"
p2 = re.compile(r"This\s+[^,]+,\s+([A-Z]{2})\s+location")
# 3. "Located in City, ST, this"
p3 = re.compile(r"Located\s+in\s+[^,]+,\s+([A-Z]{2}),\s+this")
# 4. Fallback: Look for ", ST," or " ST " where ST is a known US state code?
# Let's rely on p1 and p3 mostly as per examples.
# Example: "Located at ... in Goleta, CA, this" -> p1 matches "in Goleta, CA" -> CA.

for b in businesses:
    desc = b.get('description', '')
    state = None
    
    # Try patterns
    m1 = p1.search(desc)
    if m1:
        state = m1.group(1)
    else:
        m2 = p2.search(desc)
        if m2:
            state = m2.group(1)
        else:
            m3 = p3.search(desc)
            if m3:
                state = m3.group(1)
    
    # Special handling if needed (e.g. if regex catches something else)
    # Valid US states are 2 chars.
    
    if state:
        try:
            rc = int(b.get('review_count', 0))
        except:
            rc = 0
        parsed_data.append({
            'business_id': b['business_id'],
            'state': state,
            'review_count': rc
        })

df = pd.DataFrame(parsed_data)

if df.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No states parsed"}))
else:
    # Find state with highest number of reviews
    state_stats = df.groupby('state')['review_count'].sum().sort_values(ascending=False)
    top_state = state_stats.index[0]
    top_reviews = int(state_stats.iloc[0])

    # Get business IDs for that state
    top_state_businesses = df[df['state'] == top_state]['business_id'].tolist()
    # Convert IDs
    top_state_business_refs = [bid.replace('businessid_', 'businessref_') for bid in top_state_businesses]

    print("__RESULT__:")
    print(json.dumps({
        "top_state": top_state,
        "total_reviews": top_reviews,
        "business_refs": top_state_business_refs
    }))"""

env_args = {'var_function-call-2115877791251207599': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-17228529360697607691': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-11517960609545175320': {'top_state': 'MO', 'total_reviews': 81, 'business_refs': ['businessref_47']}, 'var_function-call-12053795473695309539': 'file_storage/function-call-12053795473695309539.json'}

exec(code, env_args)
