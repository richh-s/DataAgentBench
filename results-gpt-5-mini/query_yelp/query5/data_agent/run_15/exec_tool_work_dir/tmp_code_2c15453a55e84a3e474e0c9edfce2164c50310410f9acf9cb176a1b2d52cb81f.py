code = """import json, re

# Load data from storage-provided file paths
with open(var_call_cKAUvs32jTulvBxlVKm3UG9A, 'r') as f:
    businesses = json.load(f)
with open(var_call_HqfVjLmSpm2LUwUZsWZG8Qg2, 'r') as f:
    reviews = json.load(f)

# Build mapping of business_ref -> list of ratings
ratings_by_ref = {}
for r in reviews:
    br = r.get('business_ref')
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    if br not in ratings_by_ref:
        ratings_by_ref[br] = []
    ratings_by_ref[br].append(rating)

# Helper to determine if attributes indicate WiFi offered
def offers_wifi(attr_dict):
    if not isinstance(attr_dict, dict):
        return False
    # find any key that looks like wifi
    for k,v in attr_dict.items():
        if k is None:
            continue
        if 'wifi' in k.lower() or 'wi-fi' in k.lower():
            if v is None:
                return False
            sval = str(v).lower()
            # treat as NOT offering if contains 'no'
            if 'no' in sval:
                return False
            # if contains free/paid/yes/unknown/connection/limited treat as offering
            if any(x in sval for x in ('free', 'paid', 'yes', 'limited', 'optional', 'u\'free\'', "u'free'", "u'paid'", 'paid wifi', 'wifi')):
                return True
            # if it's some other truthy-looking value
            if sval.strip() not in ('none', 'null', 'false', '0', '', "u'none'", "none"):
                return True
            return False
    return False

# Extract state from description using regex
state_by_business_ref = {}
wifi_businesses_by_state = {}
for b in businesses:
    attrs = b.get('attributes')
    if not attrs:
        continue
    if not offers_wifi(attrs):
        continue
    desc = b.get('description') or ''
    # regex to find pattern ' in City, ST' or ', City, ST'
    m = re.search(r' in [^,]+,\s*([A-Z]{2})', desc)
    if not m:
        m = re.search(r',\s*([A-Z]{2})[,\s]', desc)
    if not m:
        # skip if can't find state
        continue
    state = m.group(1)
    # convert businessid_xxx to businessref_xxx
    bid = b.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_', 'businessref_')
    state_by_business_ref[bref] = state
    wifi_businesses_by_state.setdefault(state, set()).add(bref)

# Compute counts and average ratings per state
results = []
for state, bref_set in wifi_businesses_by_state.items():
    count = len(bref_set)
    total_ratings = 0.0
    ratings_count = 0
    for bref in bref_set:
        rlist = ratings_by_ref.get(bref, [])
        if rlist:
            total_ratings += sum(rlist)
            ratings_count += len(rlist)
    avg_rating = None
    if ratings_count > 0:
        avg_rating = total_ratings / ratings_count
    results.append({'state': state, 'wifi_business_count': count, 'avg_rating': avg_rating, 'ratings_count': ratings_count})

# Find state with max wifi_business_count
if not results:
    out = {'error': 'No WiFi businesses found or no parsable state info.'}
else:
    results_sorted = sorted(results, key=lambda x: (-x['wifi_business_count'], x['state']))
    top = results_sorted[0]
    # Round average rating to 2 decimals if present
    if top['avg_rating'] is None:
        avg = None
    else:
        avg = round(top['avg_rating'], 2)
    out = {'state': top['state'], 'wifi_business_count': top['wifi_business_count'], 'average_rating': avg, 'ratings_count': top['ratings_count']}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_cKAUvs32jTulvBxlVKm3UG9A': 'file_storage/call_cKAUvs32jTulvBxlVKm3UG9A.json', 'var_call_HqfVjLmSpm2LUwUZsWZG8Qg2': 'file_storage/call_HqfVjLmSpm2LUwUZsWZG8Qg2.json'}

exec(code, env_args)
