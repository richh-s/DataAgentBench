code = """import json
import pandas as pd
import ast

# Load data
with open(locals()['var_function-call-12682746751728674462'], 'r') as f:
    reviews_data = json.load(f)

with open(locals()['var_function-call-14334677624481174662'], 'r') as f:
    business_data = json.load(f)

# 1. Process Reviews
df_reviews = pd.DataFrame(reviews_data)
# Convert date. Pandas is usually smart enough.
# Errors='coerce' to handle unparsable, though we expect valid dates.
df_reviews['dt'] = pd.to_datetime(df_reviews['date'], errors='coerce')
# Filter for 2018
df_reviews_2018 = df_reviews[df_reviews['dt'].dt.year == 2018]
# Get unique business refs
reviewed_business_refs = df_reviews_2018['business_ref'].unique()

# Convert refs to business_ids (businessref_X -> businessid_X)
reviewed_business_ids = {ref.replace('businessref_', 'businessid_') for ref in reviewed_business_refs}

# 2. Process Businesses
# We need to count businesses that are in reviewed_business_ids AND have parking
count = 0

for b in business_data:
    bid = b.get('business_id')
    if bid not in reviewed_business_ids:
        continue
        
    attrs = b.get('attributes')
    if not attrs or attrs == "None":
        continue
    
    # Check BikeParking
    # It seems to be a string "True" or "False"
    has_bike = False
    if 'BikeParking' in attrs:
        val = attrs['BikeParking']
        if val == 'True':
            has_bike = True
            
    # Check BusinessParking
    has_business_parking = False
    if 'BusinessParking' in attrs:
        val = attrs['BusinessParking']
        if val and val != 'None':
            if val == 'True':
                has_business_parking = True
            elif val.startswith('{'):
                try:
                    # It's a string representation of a dict
                    # e.g. "{'garage': False, ...}"
                    parking_dict = ast.literal_eval(val)
                    if isinstance(parking_dict, dict):
                        # If any value is True, then there is parking?
                        # Usually keys are 'garage', 'street', 'lot', 'valet', 'validated'.
                        # If any is True, it offers parking.
                        if any(v is True for v in parking_dict.values()):
                            has_business_parking = True
                except:
                    pass
    
    if has_bike or has_business_parking:
        count += 1

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-3348725125408544776': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}, {'date': '21 May 2016, 18:48'}, {'date': 'November 01, 2021 at 05:11 PM'}], 'var_function-call-16891006534027228873': [{'count_star()': '2000'}], 'var_function-call-12682746751728674462': 'file_storage/function-call-12682746751728674462.json', 'var_function-call-14334677624481174662': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
