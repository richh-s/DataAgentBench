code = """import json, re

# Load data files from storage variables
with open(var_call_p16NaDB2bUS5nbAwxZERhkxs, 'r') as f:
    businesses = json.load(f)
with open(var_call_eyQvzrEXIp1eFYqVVuDEr2Fp, 'r') as f:
    reviews = json.load(f)

# Helper to normalize WiFi attribute
def normalize_wifi(v):
    if v is None:
        return None
    s = str(v).lower()
    # remove python unicode prefix and quotes
    s = s.replace("u'", "").replace("u\"", "").replace("'", "").replace('"','').strip()
    s = s.strip()
    if s in ('none','no','false','0','n/a','none'):
        return None
    return s

# Extract WiFi value from attributes dict by finding keys containing 'wifi'

def get_wifi_from_attributes(attrs):
    if not isinstance(attrs, dict):
        return None
    for k, v in attrs.items():
        if 'wifi' in k.lower():
            return normalize_wifi(v)
    return None

# Extract state from description using regex
state_pattern1 = re.compile(r"in [^,]+,\s*([A-Z]{2})")
state_pattern2 = re.compile(r",\s*([A-Z]{2})[,\.]")
state_pattern3 = re.compile(r",\s*([A-Z]{2})$")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern1.search(desc)
    if m:
        return m.group(1)
    m = state_pattern2.search(desc)
    if m:
        return m.group(1)
    m = state_pattern3.search(desc)
    if m:
        return m.group(1)
    # fallback: find any two-letter uppercase token
    m = re.search(r"\b([A-Z]{2})\b", desc)
    if m:
        return m.group(1)
    return None

# Build mapping of business_ref -> state for businesses that offer WiFi
businessref_to_state = {}
state_to_businessrefs = {}
for b in businesses:
    attrs = b.get('attributes')
    wifi = get_wifi_from_attributes(attrs)
    if wifi is None:
        continue
    desc = b.get('description', '')
    state = extract_state(desc)
    if state is None:
        continue
    # convert businessid_# to businessref_#
    bid = b.get('business_id')
    if not isinstance(bid, str):
        continue
    bref = bid.replace('businessid_', 'businessref_')
    businessref_to_state[bref] = state
    state_to_businessrefs.setdefault(state, set()).add(bref)

# Count businesses per state
state_counts = {st: len(s) for st, s in state_to_businessrefs.items()}
if not state_counts:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    # find state with max businesses
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    max_count = state_counts[max_state]
    # Collect ratings for reviews of businesses in that state
    ratings = []
    refs_in_state = state_to_businessrefs[max_state]
    for r in reviews:
        bref = r.get('business_ref')
        if bref in refs_in_state:
            try:
                ratings.append(float(r.get('rating')))
            except:
                pass
    if ratings:
        avg_rating = sum(ratings)/len(ratings)
        avg_rating = round(avg_rating, 2)
    else:
        avg_rating = None
    result = {"state": max_state, "business_count": max_count, "average_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3F18PzBdn7mPPg16eOgjp959': ['business', 'checkin'], 'var_call_VvYPO0uIr7doTD60TQ9cZ4Rw': ['review', 'tip', 'user'], 'var_call_p16NaDB2bUS5nbAwxZERhkxs': 'file_storage/call_p16NaDB2bUS5nbAwxZERhkxs.json', 'var_call_eyQvzrEXIp1eFYqVVuDEr2Fp': 'file_storage/call_eyQvzrEXIp1eFYqVVuDEr2Fp.json'}

exec(code, env_args)
