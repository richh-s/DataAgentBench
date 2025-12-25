code = """import json

# Get previous result
prev_res = json.loads('{"top_state": "MO", "total_reviews": 2243, "num_businesses": 9, "sample_refs": ["businessref_47", "businessref_64", "businessref_10", "businessref_24", "businessref_30"]}')
# The full list of refs isn't in the output string, I need to regenerate it or pass it.
# I'll regenerate it from the file since I can't access the variable from the previous scope directly if not persisted?
# Wait, "Variables created in execute_python are not persisted between calls unless you explicitly print them?" 
# No, "All previous tool results are available as variables." 
# But the previous execution defined `business_refs` inside the script scope. It didn't output the full list.
# So I need to re-process the file or output the full list in the previous step. 
# Since I only output sample_refs, I must re-process or trust the logic.
# Re-processing is safer.

with open(locals()['var_function-call-5120153937471768802'], 'r') as f:
    businesses = json.load(f)

import re
import pandas as pd

data = []
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
state_stats = df.groupby('state')['review_count'].sum().sort_values(ascending=False)
top_state = state_stats.idxmax()
top_state_businesses = df[df['state'] == top_state]
business_ids = top_state_businesses['business_id'].tolist()
business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids]

# Construct SQL query
refs_str = "', '".join(business_refs)
query = f"SELECT AVG(rating) as avg_rating FROM review WHERE business_ref IN ('{refs_str}')"
# Also considering "average of businesses", let's get avg per business first
query_per_biz = f"SELECT business_ref, AVG(rating) as avg_rating FROM review WHERE business_ref IN ('{refs_str}') GROUP BY business_ref"

print("__RESULT__:")
print(json.dumps({
    "query": query_per_biz,
    "refs": business_refs
}))"""

env_args = {'var_function-call-12519791703274818244': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-11762948561723273781': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-16969636810727459354': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-11283997609679586964': {'top_state': 'MO', 'total_reviews': 81, 'num_businesses': 1, 'sample_refs': ['businessref_47']}, 'var_function-call-5120153937471768802': 'file_storage/function-call-5120153937471768802.json', 'var_function-call-7801183918335796440': {'top_state': 'MO', 'total_reviews': 2243, 'num_businesses': 9, 'sample_refs': ['businessref_47', 'businessref_64', 'businessref_10', 'businessref_24', 'businessref_30']}}

exec(code, env_args)
