code = """import json
# var_call_FwQgesuWmafnHorTy9rMLtv3 is a list of business records
business_records = var_call_FwQgesuWmafnHorTy9rMLtv3
# var_call_jo2xmMrAaE1YGx2vks7NCkqb is a file path to the reviews JSON
with open(var_call_jo2xmMrAaE1YGx2vks7NCkqb, 'r') as f:
    review_records = json.load(f)

import re

# Build mapping from business_id to state
biz_state = {}
for b in business_records:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    state = None
    # Try regex: 'in City, ST'
    m = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
    if m:
        state = m.group(1)
    else:
        # try find ', ST,' or ', ST.' or at end
        m2 = re.search(r",\s*([A-Z]{2})(?:[,\.\s]|$)", desc)
        if m2:
            state = m2.group(1)
    if state:
        biz_state[bid] = state

# Aggregate reviews per state
from collections import defaultdict
state_counts = defaultdict(int)
state_rating_sum = defaultdict(float)

for r in review_records:
    bref = r.get('business_ref')
    rating = r.get('rating')
    try:
        rating = float(rating)
    except:
        continue
    # convert businessref_X to businessid_X
    if isinstance(bref, str) and bref.startswith('businessref_'):
        bid = 'businessid_' + bref.split('_',1)[1]
    else:
        continue
    state = biz_state.get(bid)
    if not state:
        continue
    state_counts[state] += 1
    state_rating_sum[state] += rating

if not state_counts:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # find state with max reviews
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    cnt = state_counts[max_state]
    avg = state_rating_sum[max_state] / cnt if cnt>0 else None
    # round to 2 decimals
    if avg is not None:
        avg = round(avg, 2)
    result = {"state": max_state, "review_count": cnt, "average_rating": avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_21inqTO3MZDgnYm44Oecfm1o': ['business', 'checkin'], 'var_call_6b7ub2rK3jo1RqQ2TdnzyBSL': ['review', 'tip', 'user'], 'var_call_FwQgesuWmafnHorTy9rMLtv3': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_jo2xmMrAaE1YGx2vks7NCkqb': 'file_storage/call_jo2xmMrAaE1YGx2vks7NCkqb.json'}

exec(code, env_args)
