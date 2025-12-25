code = """import json
import re
import pandas as pd

data = locals()['var_function-call-13900704705305798710']
if isinstance(data, str):
    with open(data, 'r') as f:
        data = json.load(f)

# Regex to extract state: look for ", [A-Z]{2}"
# The descriptions are like "Located at ... in City, ST, ..."
# We can look for the pattern: " in [^,]+, ([A-Z]{2})[, ]"
state_pattern = re.compile(r" in [^,]+, ([A-Z]{2})")

rows = []
for entry in data:
    desc = entry.get('description', '')
    match = state_pattern.search(desc)
    state = match.group(1) if match else None
    
    # review_count is string in the sample, need to convert
    try:
        rc = int(entry.get('review_count', 0))
    except:
        rc = 0
        
    rows.append({
        'business_id': entry.get('business_id'),
        'state': state,
        'review_count': rc
    })

df = pd.DataFrame(rows)

# Filter out None states if any
df = df.dropna(subset=['state'])

# Group by state and sum review_count
state_counts = df.groupby('state')['review_count'].sum().sort_values(ascending=False)
top_state = state_counts.index[0]
top_state_reviews = state_counts.iloc[0]

# Get business_ids for the top state
top_state_businesses = df[df['state'] == top_state]['business_id'].tolist()

# Convert to business_ref format
# business_id format: "businessid_X"
# business_ref format: "businessref_X"
business_refs = [bid.replace('businessid_', 'businessref_') for bid in top_state_businesses]

print("__RESULT__:")
print(json.dumps({
    "top_state": top_state,
    "total_reviews": int(top_state_reviews),
    "business_refs": business_refs
}))"""

env_args = {'var_function-call-8537525989261350117': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-13900704705305798710': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
