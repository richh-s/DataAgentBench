code = """import json
import re
import pandas as pd

# Load business data from file
with open(locals()['var_function-call-5120153937471768802'], 'r') as f:
    businesses = json.load(f)

# Parse state and process review counts
data = []
# Regex: " in [City], [State code]," or similar. 
# Looking at samples: "Located at ... in Goleta, CA," 
# "Located at ... in St. Louis, MO,"
# "Located in Pennsauken, NJ,"
# "This Philadelphia, PA location offers..."
# So the pattern "in [City], [State]" or " [City], [State]" is key.
# But simply looking for ", [A-Z]{2}" is safer if we assume standard US address format in description.
# Most appear to be " ... in City, ST, ..." or " ... in City, ST" or "City, ST location".
# Let's try to extract the 2-letter code preceded by a comma and space, and followed by a comma, space, or end of string.

# However, description text might have other commas. 
# Sample: "Located at 9916 Clayton Rd in St. Louis, MO, this establishment..."
# Sample: "This Philadelphia, PA location offers..."
# Sample: "Located at ... in New Orleans, LA, this vibrant..."

state_pattern = re.compile(r"[\s,]([A-Z]{2})[,\s]")

# Better approach given the "Located at ... in [City], [State]" structure:
# Find " in " followed by characters then ", " then 2 uppercase letters.
# Also handle "This [City], [State] location"
p1 = re.compile(r" in [^,]+,\s+([A-Z]{2})")
p2 = re.compile(r" ([A-Z][a-z]+),\s+([A-Z]{2}) location")

for b in businesses:
    desc = b.get('description', '')
    state = None
    
    match1 = p1.search(desc)
    if match1:
        state = match1.group(1)
    else:
        match2 = p2.search(desc)
        if match2:
            state = match2.group(2)
        else:
            # Fallback: look for ", [A-Z]{2}"
            # This is risky if description lists other things like "VA, FHA loans" etc.
            # But "Located at ... in ..., [ST]" is very consistent in generated datasets.
            # Let's try to find the state code near the "Located" part if possible.
            # Or just look for the first ", [A-Z]{2}" which often is the address.
            m3 = re.search(r",\s([A-Z]{2})[\s,]", desc)
            if m3:
                state = m3.group(1)

    if state:
        try:
            rc = int(b.get('review_count', 0))
        except:
            rc = 0
        data.append({
            'business_id': b.get('business_id'),
            'state': state,
            'review_count': rc
        })

df = pd.DataFrame(data)

# Aggregate review counts by state
state_stats = df.groupby('state')['review_count'].sum().sort_values(ascending=False)
if not state_stats.empty:
    top_state = state_stats.idxmax()
    top_state_reviews = state_stats.max()
    
    # Get businesses for the top state
    top_state_businesses = df[df['state'] == top_state]
    business_ids = top_state_businesses['business_id'].tolist()
    business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids]
else:
    top_state = None
    top_state_reviews = 0
    business_refs = []

print("__RESULT__:")
print(json.dumps({
    "top_state": top_state,
    "total_reviews": int(top_state_reviews),
    "num_businesses": len(business_refs),
    "sample_refs": business_refs[:5]
}))"""

env_args = {'var_function-call-12519791703274818244': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-11762948561723273781': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-16969636810727459354': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-11283997609679586964': {'top_state': 'MO', 'total_reviews': 81, 'num_businesses': 1, 'sample_refs': ['businessref_47']}, 'var_function-call-5120153937471768802': 'file_storage/function-call-5120153937471768802.json'}

exec(code, env_args)
