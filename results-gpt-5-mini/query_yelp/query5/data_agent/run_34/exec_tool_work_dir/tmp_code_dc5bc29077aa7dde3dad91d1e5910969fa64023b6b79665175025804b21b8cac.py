code = """import json, re

# Load business and review data from storage file paths
with open(var_call_aC6dSIiVeQbNCxoE9mIZ8hcK, 'r') as f:
    businesses = json.load(f)
with open(var_call_H2QnrWtK5tEZPVLm1pa1nFs3, 'r') as f:
    reviews = json.load(f)

# Helper to determine if a business offers WiFi
def offers_wifi(attr):
    if not attr:
        return False
    val = attr.get('WiFi') if isinstance(attr, dict) else None
    if val is None:
        return False
    # Normalize to string
    try:
        s = str(val).lower()
    except Exception:
        return False
    # If contains "no", consider no WiFi
    if 'no' in s:
        return False
    # If contains 'free' or 'paid' or 'paid' or 'yes' or 'wifi' assume offers
    if any(k in s for k in ['free', 'paid', 'yes', 'spot', 'available', 'paid', 'wireless']):
        return True
    # Fallback: if it's not 'no', assume offers
    return True

# Extract state from description using regex
state_counts = {}
state_business_ids = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    attrs = b.get('attributes')
    if not offers_wifi(attrs):
        continue
    # Find state code pattern: a comma, space, two uppercase letters, then comma or end
    m = re.search(r",\s*([A-Z]{2})(?:[,\.\s]|$)", desc)
    state = None
    if m:
        state = m.group(1)
    else:
        # Try another pattern: 'in City, ST,'
        m2 = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
        if m2:
            state = m2.group(1)
    if not state:
        continue
    state_counts[state] = state_counts.get(state, 0) + 1
    state_business_ids.setdefault(state, []).append(bid)

# Determine state with highest count
if not state_counts:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    count = state_counts[top_state]
    # Map businessid_x to businessref_x
    business_refs = set(bid.replace('businessid_', 'businessref_') for bid in state_business_ids[top_state])
    # Collect ratings for reviews matching these business_refs
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if bref in business_refs:
            try:
                ratings.append(float(r.get('rating')))
            except Exception:
                pass
    avg = None
    if ratings:
        avg = sum(ratings) / len(ratings)
        avg = round(avg, 2)
    result = {"state": top_state, "business_count": count, "average_rating": avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SQXSpNw9kBrBEzklYZ3lMvf2': ['checkin', 'business'], 'var_call_fMeHIoYyR3u4HTP4FqZa11nq': ['review', 'tip', 'user'], 'var_call_aC6dSIiVeQbNCxoE9mIZ8hcK': 'file_storage/call_aC6dSIiVeQbNCxoE9mIZ8hcK.json', 'var_call_H2QnrWtK5tEZPVLm1pa1nFs3': 'file_storage/call_H2QnrWtK5tEZPVLm1pa1nFs3.json'}

exec(code, env_args)
