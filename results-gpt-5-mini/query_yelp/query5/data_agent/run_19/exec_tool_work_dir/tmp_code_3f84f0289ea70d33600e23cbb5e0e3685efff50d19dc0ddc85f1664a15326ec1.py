code = """import json
import re
# Access storage variables
business_docs = var_call_zCBx5qUXNZqRTCqTBLSrguu9
reviews_path = var_call_UXVMOUSuszhNpLFG4ZwxQ9lx

# Load reviews from file path
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Helper to determine if WiFi offered
def offers_wifi(attr):
    if attr is None:
        return False
    # Sometimes attributes stored as string 'None'
    if isinstance(attr, str):
        if attr.strip().lower() == 'none':
            return False
        try:
            # Try to parse string representation of dict
            parsed = eval(attr)
            attr = parsed
        except Exception:
            # leave as string
            pass
    if not isinstance(attr, dict):
        return False
    if 'WiFi' not in attr:
        return False
    val = attr.get('WiFi')
    if val is None:
        return False
    # normalize
    if isinstance(val, str):
        low = val.lower()
        # strip leading u'...'
        low = low.replace("u'", "'").replace('u"', '"')
        # remove quotes
        low = low.strip(" \"'\n")
        # if contains no
        if 'no' in low:
            return False
        # otherwise if contains free or paid or yes or 'signal:...' treat as offering
        if any(k in low for k in ['free', 'paid', 'yes', 'paid']) or low != '':
            return True
        return False
    # if boolean
    if isinstance(val, bool):
        return bool(val)
    # otherwise consider as offering
    return True

# Extract state from description
state_pattern = re.compile(r",\s*([A-Z]{2})[,\.]")

wifi_businesses = []
for b in business_docs:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    # If attributes string 'None', convert to None
    if isinstance(attrs, str) and attrs.strip().lower() == 'none':
        attrs = None
    if offers_wifi(attrs):
        desc = b.get('description','') or ''
        m = state_pattern.search(desc)
        state = None
        if m:
            state = m.group(1)
        else:
            # try alternative pattern: in City, ST in
            m2 = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
            if m2:
                state = m2.group(1)
        wifi_businesses.append({'business_id': bid, 'business_ref': bid.replace('businessid_','businessref_'), 'state': state})

# Group by state
from collections import defaultdict
state_to_businesses = defaultdict(list)
for wb in wifi_businesses:
    state_to_businesses[wb['state']].append(wb)

# Compute counts
state_counts = {st: len(lst) for st,lst in state_to_businesses.items()}
# find state with max count (ignore None states)
filtered = {st:cnt for st,cnt in state_counts.items() if st is not None}
if not filtered:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    max_state = max(filtered.items(), key=lambda x: x[1])[0]
    business_refs = set([b['business_ref'] for b in state_to_businesses[max_state]])
    # collect ratings for reviews whose business_ref in business_refs
    ratings = []
    for r in reviews:
        br = r.get('business_ref')
        if br in business_refs:
            try:
                ratings.append(int(r.get('rating')))
            except:
                try:
                    ratings.append(float(r.get('rating')))
                except:
                    pass
    avg_rating = None
    if ratings:
        avg_rating = sum(ratings)/len(ratings)
    result = {"state": max_state, "business_count": filtered[max_state], "average_rating": round(avg_rating,2) if avg_rating is not None else None}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_06Q3dEcwdqakhpiKBV6DQZiA': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}, 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}], 'var_call_zCBx5qUXNZqRTCqTBLSrguu9': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_UXVMOUSuszhNpLFG4ZwxQ9lx': 'file_storage/call_UXVMOUSuszhNpLFG4ZwxQ9lx.json'}

exec(code, env_args)
