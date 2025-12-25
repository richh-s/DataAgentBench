code = """import json
import re
import pandas as pd

# Load business data
with open(locals()['var_function-call-18397388611199875909'], 'r') as f:
    businesses = json.load(f)

# Extract state and prepare dataframe
data = []
for b in businesses:
    desc = b.get('description', '')
    # Regex to find state: " in City, ST,"
    # Looking for ", [A-Z]{2}," pattern.
    # The description format: "Located at ... in City, ST, this..."
    match = re.search(r",\s([A-Z]{2}),", desc)
    state = match.group(1) if match else None
    
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

# Group by state to find the one with highest review count
state_reviews = df.groupby('state')['review_count'].sum().sort_values(ascending=False)
top_state = state_reviews.index[0]
top_reviews_count = state_reviews.iloc[0]

# Get business_refs for the top state
# Convert businessid_X to businessref_X
# business_id format: "businessid_..."
# business_ref format: "businessref_..."
target_businesses = df[df['state'] == top_state]['business_id'].tolist()
target_business_refs = [bid.replace('businessid_', 'businessref_') for bid in target_businesses]

print("__RESULT__:")
print(json.dumps({
    "top_state": top_state,
    "total_reviews": int(top_reviews_count),
    "num_businesses": len(target_business_refs),
    "business_refs": target_business_refs
}))"""

env_args = {'var_function-call-12781526679160739795': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-18397388611199875909': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
