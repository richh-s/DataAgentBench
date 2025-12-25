code = """import pandas as pd
import json
import re
import os

# Load business data from file
file_path = locals()['var_function-call-13519857975883532277']
with open(file_path, 'r') as f:
    business_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(business_data)
df['review_count'] = df['review_count'].astype(int)

# Extract state
def extract_state(desc):
    # Standard: "... in City, ST, ..." or "... in City, ST."
    # Also handle "... in City, ST" at end of string? Though description usually continues.
    # Look for 2 uppercase letters preceded by ", " and followed by ", " or " ".
    # The previous regex `r", ([A-Z]{2}),"` is good if state is followed by comma.
    # Let's inspect a few samples in thought:
    # "Located at ... in Goleta, CA, this..." -> "CA" match ", CA,"
    # "Located in Pennsauken, NJ, this..." -> "NJ" match ", NJ,"
    # "This Philadelphia, PA location..." -> "PA" match ", PA " or ", PA,"?
    # Wait, sample 14: "This Philadelphia, PA location offers..."
    # There is no "in Philadelphia, PA". It says "This Philadelphia, PA location..."
    # So searching for " in " might fail.
    # But usually it's "City, State".
    # Regex: Look for pattern `[A-Z][a-z]+, ([A-Z]{2})`? No, City can have spaces.
    # Look for `([A-Z]{2})` that is a US state code?
    # Maybe simple regex: `, ([A-Z]{2})[ ,]`
    # Let's try to find the state code (2 caps) surrounded by comma/space.
    # Warning: might match other things. But state is usually after city and comma.
    
    # Let's try to match the pattern: `Matches comma, space, 2 Upper, then space or comma or end`
    match = re.search(r', ([A-Z]{2})[\s,]', desc)
    if match:
        return match.group(1)
    
    # Fallback for "This Philadelphia, PA location..." -> "Philadelphia, PA "
    match = re.search(r' ([A-Z]{2}) location', desc) # specific case?
    if match:
         return match.group(1)

    # General fallback: Find any 2-letter uppercase word after a comma?
    # Or just `\b[A-Z]{2}\b`? No, "US", "TV" etc.
    # Let's rely on `, ([A-Z]{2})` which is most common for address.
    return None

df['state'] = df['description'].apply(extract_state)

# Check for null states
# print("Null states:", df['state'].isnull().sum())

# Group by state and sum review_count
state_reviews = df.groupby('state')['review_count'].sum().sort_values(ascending=False)

if not state_reviews.empty:
    top_state = state_reviews.index[0]
    top_state_reviews = state_reviews.iloc[0]
    
    # Get business_ids for the top state
    top_state_businesses = df[df['state'] == top_state]['business_id'].tolist()
    
    # Convert to business_ref format
    top_state_business_refs = [bid.replace('businessid_', 'businessref_') for bid in top_state_businesses]
    
    result = {
        "top_state": top_state,
        "review_count": int(top_state_reviews),
        "business_refs": top_state_business_refs,
        "business_refs_count": len(top_state_business_refs)
    }
else:
    result = {"error": "No states found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7241740819870757651': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9178618695262343574': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-10170225802164921427': {'top_state': 'MO', 'review_count': 81, 'business_refs': ['businessref_47']}, 'var_function-call-13519857975883532277': 'file_storage/function-call-13519857975883532277.json'}

exec(code, env_args)
