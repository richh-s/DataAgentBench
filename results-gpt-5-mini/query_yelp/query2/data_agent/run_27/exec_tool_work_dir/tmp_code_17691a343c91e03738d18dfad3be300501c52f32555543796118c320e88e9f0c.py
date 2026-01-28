code = """import json, re
# var_call_Yq4jSp6aZRlsKqapRm1fQIwa is the path to the review JSON file
# var_call_DSLDVoeoUpNvrcodL6lXRGeb is the business list

# Load reviews from file path
with open(var_call_Yq4jSp6aZRlsKqapRm1fQIwa, 'r') as f:
    reviews = json.load(f)

businesses = var_call_DSLDVoeoUpNvrcodL6lXRGeb

# Build mapping from business_id to state
state_map = {}
pattern1 = re.compile(r'in [^,]+, ([A-Z]{2})')
pattern2 = re.compile(r',\s*([A-Z]{2})[,\.]')
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    state = None
    m = pattern1.search(desc)
    if m:
        state = m.group(1)
    else:
        m2 = pattern2.search(desc)
        if m2:
            state = m2.group(1)
    state_map[bid] = state

# Aggregate reviews by state
counts = {}
sum_ratings = {}
for r in reviews:
    bref = r.get('business_ref')
    if bref is None:
        continue
    # map to businessid_
    bid = bref.replace('businessref_', 'businessid_')
    state = state_map.get(bid)
    if not state:
        continue
    try:
        rating = float(r.get('rating'))
    except:
        continue
    counts[state] = counts.get(state, 0) + 1
    sum_ratings[state] = sum_ratings.get(state, 0.0) + rating

# Find state with highest number of reviews
if not counts:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    max_state = max(counts.items(), key=lambda x: x[1])[0]
    review_count = counts[max_state]
    average_rating = sum_ratings[max_state] / review_count
    # round to 3 decimals
    average_rating = round(average_rating, 3)
    result = {"state": max_state, "review_count": review_count, "average_rating": average_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1l7zH0FwNYOwJAkfCjqlYbk0': ['business', 'checkin'], 'var_call_5OJMPycrFMKnHX6dKqWkyEiT': ['review', 'tip', 'user'], 'var_call_DSLDVoeoUpNvrcodL6lXRGeb': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_Yq4jSp6aZRlsKqapRm1fQIwa': 'file_storage/call_Yq4jSp6aZRlsKqapRm1fQIwa.json'}

exec(code, env_args)
