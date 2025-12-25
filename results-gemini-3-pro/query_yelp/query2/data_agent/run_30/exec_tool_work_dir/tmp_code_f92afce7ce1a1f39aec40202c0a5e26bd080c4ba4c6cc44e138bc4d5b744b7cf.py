code = """import json
import re
import pandas as pd

file_path = locals()['var_function-call-7772097550043372298']
with open(file_path, 'r') as f:
    data = json.load(f)

# Valid US States
us_states = set([
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
])

def extract_state(desc):
    # Pattern 1: " in City, ST," or " in City, ST"
    # We look for ", ST" where ST is in us_states
    # Regex: `, ([A-Z]{2})`
    matches = re.findall(r", ([A-Z]{2})", desc)
    for m in matches:
        if m in us_states:
            return m
            
    # Pattern 2: "This City, ST location"
    # Matches `City, ST`
    matches = re.findall(r" ([A-Z]{2}) location", desc)
    for m in matches:
        if m in us_states:
            return m
            
    return None

results = []
for entry in data:
    desc = entry.get('description', '')
    review_count = int(entry.get('review_count', 0))
    bid = entry.get('business_id')
    
    state = extract_state(desc)
    if state:
        results.append({'state': state, 'review_count': review_count, 'business_id': bid})

df = pd.DataFrame(results)

if df.empty:
    print("__RESULT__:")
    print(json.dumps({'error': 'No data found'}))
else:
    state_stats = df.groupby('state')['review_count'].sum().reset_index()
    top_state_row = state_stats.sort_values(by='review_count', ascending=False).iloc[0]
    top_state = top_state_row['state']
    total_reviews = top_state_row['review_count']
    
    # Get business_refs for the top state
    top_state_businesses = df[df['state'] == top_state]['business_id'].tolist()
    business_refs = [bid.replace('businessid_', 'businessref_') for bid in top_state_businesses]

    print("__RESULT__:")
    print(json.dumps({'top_state': top_state, 'total_reviews': int(total_reviews), 'num_businesses': len(business_refs), 'business_refs': business_refs}))"""

env_args = {'var_function-call-8761496496221904381': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-4665636635101342260': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-12189166839412624490': {'top_state': 'MO', 'total_reviews': 81, 'business_refs': ['businessref_47']}, 'var_function-call-2429887257282210447': [{'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047'}], 'var_function-call-41528085617227584': [{'_id': '6859a000fe8b31cd7362e2ab'}, {'_id': '6859a000fe8b31cd7362e2ac'}, {'_id': '6859a000fe8b31cd7362e2ad'}, {'_id': '6859a000fe8b31cd7362e2ae'}, {'_id': '6859a000fe8b31cd7362e2af'}, {'_id': '6859a000fe8b31cd7362e2b0'}, {'_id': '6859a000fe8b31cd7362e2b1'}, {'_id': '6859a000fe8b31cd7362e2b2'}, {'_id': '6859a000fe8b31cd7362e2b3'}, {'_id': '6859a000fe8b31cd7362e2b4'}, {'_id': '6859a000fe8b31cd7362e2b5'}, {'_id': '6859a000fe8b31cd7362e2b6'}, {'_id': '6859a000fe8b31cd7362e2b7'}, {'_id': '6859a000fe8b31cd7362e2b8'}, {'_id': '6859a000fe8b31cd7362e2b9'}, {'_id': '6859a000fe8b31cd7362e2ba'}, {'_id': '6859a000fe8b31cd7362e2bb'}, {'_id': '6859a000fe8b31cd7362e2bc'}, {'_id': '6859a000fe8b31cd7362e2bd'}, {'_id': '6859a000fe8b31cd7362e2be'}, {'_id': '6859a000fe8b31cd7362e2bf'}, {'_id': '6859a000fe8b31cd7362e2c0'}, {'_id': '6859a000fe8b31cd7362e2c1'}, {'_id': '6859a000fe8b31cd7362e2c2'}, {'_id': '6859a000fe8b31cd7362e2c3'}, {'_id': '6859a000fe8b31cd7362e2c4'}, {'_id': '6859a000fe8b31cd7362e2c5'}, {'_id': '6859a000fe8b31cd7362e2c6'}, {'_id': '6859a000fe8b31cd7362e2c7'}, {'_id': '6859a000fe8b31cd7362e2c8'}, {'_id': '6859a000fe8b31cd7362e2c9'}, {'_id': '6859a000fe8b31cd7362e2ca'}, {'_id': '6859a000fe8b31cd7362e2cb'}, {'_id': '6859a000fe8b31cd7362e2cc'}, {'_id': '6859a000fe8b31cd7362e2cd'}, {'_id': '6859a000fe8b31cd7362e2ce'}, {'_id': '6859a000fe8b31cd7362e2cf'}, {'_id': '6859a000fe8b31cd7362e2d0'}, {'_id': '6859a000fe8b31cd7362e2d1'}, {'_id': '6859a000fe8b31cd7362e2d2'}, {'_id': '6859a000fe8b31cd7362e2d3'}, {'_id': '6859a000fe8b31cd7362e2d4'}, {'_id': '6859a000fe8b31cd7362e2d5'}, {'_id': '6859a000fe8b31cd7362e2d6'}, {'_id': '6859a000fe8b31cd7362e2d7'}, {'_id': '6859a000fe8b31cd7362e2d8'}, {'_id': '6859a000fe8b31cd7362e2d9'}, {'_id': '6859a000fe8b31cd7362e2da'}, {'_id': '6859a000fe8b31cd7362e2db'}, {'_id': '6859a000fe8b31cd7362e2dc'}, {'_id': '6859a000fe8b31cd7362e2dd'}, {'_id': '6859a000fe8b31cd7362e2de'}, {'_id': '6859a000fe8b31cd7362e2df'}, {'_id': '6859a000fe8b31cd7362e2e0'}, {'_id': '6859a000fe8b31cd7362e2e1'}, {'_id': '6859a000fe8b31cd7362e2e2'}, {'_id': '6859a000fe8b31cd7362e2e3'}, {'_id': '6859a000fe8b31cd7362e2e4'}, {'_id': '6859a000fe8b31cd7362e2e5'}, {'_id': '6859a000fe8b31cd7362e2e6'}, {'_id': '6859a000fe8b31cd7362e2e7'}, {'_id': '6859a000fe8b31cd7362e2e8'}, {'_id': '6859a000fe8b31cd7362e2e9'}, {'_id': '6859a000fe8b31cd7362e2ea'}, {'_id': '6859a000fe8b31cd7362e2eb'}, {'_id': '6859a000fe8b31cd7362e2ec'}, {'_id': '6859a000fe8b31cd7362e2ed'}, {'_id': '6859a000fe8b31cd7362e2ee'}, {'_id': '6859a000fe8b31cd7362e2ef'}, {'_id': '6859a000fe8b31cd7362e2f0'}, {'_id': '6859a000fe8b31cd7362e2f1'}, {'_id': '6859a000fe8b31cd7362e2f2'}, {'_id': '6859a000fe8b31cd7362e2f3'}, {'_id': '6859a000fe8b31cd7362e2f4'}, {'_id': '6859a000fe8b31cd7362e2f5'}, {'_id': '6859a000fe8b31cd7362e2f6'}, {'_id': '6859a000fe8b31cd7362e2f7'}, {'_id': '6859a000fe8b31cd7362e2f8'}, {'_id': '6859a000fe8b31cd7362e2f9'}, {'_id': '6859a000fe8b31cd7362e2fa'}, {'_id': '6859a000fe8b31cd7362e2fb'}, {'_id': '6859a000fe8b31cd7362e2fc'}, {'_id': '6859a000fe8b31cd7362e2fd'}, {'_id': '6859a000fe8b31cd7362e2fe'}, {'_id': '6859a000fe8b31cd7362e2ff'}, {'_id': '6859a000fe8b31cd7362e300'}, {'_id': '6859a000fe8b31cd7362e301'}, {'_id': '6859a000fe8b31cd7362e302'}, {'_id': '6859a000fe8b31cd7362e303'}, {'_id': '6859a000fe8b31cd7362e304'}, {'_id': '6859a000fe8b31cd7362e305'}, {'_id': '6859a000fe8b31cd7362e306'}, {'_id': '6859a000fe8b31cd7362e307'}, {'_id': '6859a000fe8b31cd7362e308'}, {'_id': '6859a000fe8b31cd7362e309'}, {'_id': '6859a000fe8b31cd7362e30a'}, {'_id': '6859a000fe8b31cd7362e30b'}, {'_id': '6859a000fe8b31cd7362e30c'}, {'_id': '6859a000fe8b31cd7362e30d'}, {'_id': '6859a000fe8b31cd7362e30e'}], 'var_function-call-7772097550043372298': 'file_storage/function-call-7772097550043372298.json'}

exec(code, env_args)
