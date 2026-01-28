code = """import json
import re
from collections import defaultdict

# var_call_h7rTqn5f99tmX7zPgDZc5QrA is available as per storage
business_docs = var_call_h7rTqn5f99tmX7zPgDZc5QrA

# Reviews are stored in a JSON file path at var_call_UlBujubjiYNIdtoJPj5BpSjt
reviews_path = var_call_UlBujubjiYNIdtoJPj5BpSjt
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Helper to extract state from description
state_pattern = re.compile(r"in [^,]+,\s*([A-Z]{2})")

# Determine businesses that offer WiFi and map to states
wifi_businesses = []  # list of dicts with business_id and state
for b in business_docs:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    desc = b.get('description') or ''
    # Extract state
    state = None
    m = state_pattern.search(desc)
    if m:
        state = m.group(1)
    # Determine if offers WiFi
    has_wifi = False
    if isinstance(attrs, dict) and 'WiFi' in attrs:
        val = attrs.get('WiFi')
        if val is not None:
            s = str(val).lower()
            # if contains 'no', treat as no; otherwise if contains yes/free/paid or anything else consider as offers
            if 'no' not in s:
                has_wifi = True
    # else: attributes missing or WiFi key absent -> assume no
    if has_wifi and state:
        wifi_businesses.append({'business_id': bid, 'state': state})

# Count per state
count_by_state = defaultdict(int)
businesses_by_state = defaultdict(list)
for wb in wifi_businesses:
    count_by_state[wb['state']] += 1
    businesses_by_state[wb['state']].append(wb['business_id'])

# Prepare reviews mapping: business_ref -> list of ratings
ratings_by_businessref = defaultdict(list)
for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    # rating may be string, convert
    try:
        rating_val = float(rating)
    except:
        continue
    ratings_by_businessref[bref].append(rating_val)

# For each state, gather reviews for its wifi businesses
avg_rating_by_state = {}
for st, bids in businesses_by_state.items():
    # convert businessid_x to businessref_x
    ratings = []
    for bid in bids:
        bref = bid.replace('businessid_', 'businessref_')
        ratings.extend(ratings_by_businessref.get(bref, []))
    if ratings:
        avg = sum(ratings)/len(ratings)
    else:
        avg = None
    avg_rating_by_state[st] = avg

# Find state with highest count
if count_by_state:
    max_count = max(count_by_state.values())
    # get states with max_count
    states_with_max = [st for st, c in count_by_state.items() if c == max_count]
    # choose the first in sorted order for determinism
    chosen_state = sorted(states_with_max)[0]
    chosen_count = max_count
    chosen_avg = avg_rating_by_state.get(chosen_state)
    # Round average to 2 decimals if not None
    if chosen_avg is not None:
        chosen_avg = round(chosen_avg, 2)
else:
    chosen_state = None
    chosen_count = 0
    chosen_avg = None

result = {
    'state': chosen_state,
    'wifi_business_count': chosen_count,
    'average_rating': chosen_avg
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_h7rTqn5f99tmX7zPgDZc5QrA': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_UlBujubjiYNIdtoJPj5BpSjt': 'file_storage/call_UlBujubjiYNIdtoJPj5BpSjt.json'}

exec(code, env_args)
