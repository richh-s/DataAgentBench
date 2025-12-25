code = """import json
import re
import pandas as pd
import os

data_input = locals()['var_function-call-14144035576782285829']

# Load data
with open(data_input, 'r') as f:
    businesses = json.load(f)

# Extract state and prepare dataframe
data = []
for b in businesses:
    desc = b.get('description', '')
    # Regex: Look for ", ST," where ST is 2 uppercase letters.
    # Some descriptions: "Located at ... in City, ST, ..."
    # Some: "This Philadelphia, PA location ..."
    # Pattern: comma, space, 2 uppercase letters, comma or space or end.
    # Let's try a robust regex.
    # Usually state comes after city.
    # Let's find ", [A-Z]{2}" followed by comma or end.
    match = re.search(r",\s([A-Z]{2})", desc)
    # The previous regex `r",\s([A-Z]{2}),"` might miss if it's at the end or followed by something else.
    # Let's look at the samples:
    # "... in Goleta, CA, this ..."
    # "... in St. Louis, MO, this ..."
    # "This Philadelphia, PA location ..."
    # "... in Pennsauken, NJ, this ..."
    
    # Simple regex `,\s([A-Z]{2})` captures the first occurrence. 
    # Addresses often have commas. "123 Main St, Apt 1, City, ST"
    # The state is usually the last 2-letter uppercase word preceded by a comma.
    # But wait, descriptions can be complex.
    # Let's stick to the previous one if it worked, or improve.
    # `r",\s([A-Z]{2})"`
    
    # Let's find all matches and pick the one that looks like a state?
    # Or rely on the " in City, ST" structure.
    # "Located at ... in [City], [ST], this..."
    # "Located in [City], [ST], this..."
    
    match = re.search(r" in [^,]+,\s([A-Z]{2})", desc)
    if not match:
        # Try "This [City], [ST] location"
        match = re.search(r"This [^,]+,\s([A-Z]{2}) location", desc)
    
    state = match.group(1) if match else None
    
    # Fallback: Just find ", [A-Z]{2}"
    if not state:
        # Find all ", XX" patterns
        matches = re.findall(r",\s([A-Z]{2})", desc)
        if matches:
            # Take the last one? Or the first?
            # Usually address is at the beginning.
            # "Located at ... in X, Y, ..."
            state = matches[0]

    if state:
        try:
            rc = int(b.get('review_count', 0))
        except:
            rc = 0
        data.append({
            'business_id': b['business_id'],
            'state': state,
            'review_count': rc
        })

df = pd.DataFrame(data)

# Group by state
state_reviews = df.groupby('state')['review_count'].sum().sort_values(ascending=False)

top_state = state_reviews.index[0]
top_reviews_count = state_reviews.iloc[0]

# Get business_refs
target_businesses = df[df['state'] == top_state]['business_id'].tolist()
target_business_refs = [bid.replace('businessid_', 'businessref_') for bid in target_businesses]

print("__RESULT__:")
print(json.dumps({
    "top_state": top_state,
    "total_reviews": int(top_reviews_count),
    "num_businesses": len(target_business_refs),
    "business_refs": target_business_refs
}))"""

env_args = {'var_function-call-12781526679160739795': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-18397388611199875909': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-7755409378771860359': {'top_state': 'MO', 'total_reviews': 81, 'num_businesses': 1, 'business_refs': ['businessref_47']}, 'var_function-call-5143636694605188862': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-14144035576782285829': 'file_storage/function-call-14144035576782285829.json'}

exec(code, env_args)
