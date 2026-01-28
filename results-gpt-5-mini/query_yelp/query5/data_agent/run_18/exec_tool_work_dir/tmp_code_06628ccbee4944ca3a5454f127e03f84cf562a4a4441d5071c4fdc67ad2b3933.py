code = """import json
import re
from collections import defaultdict

# Load the data files from storage variables
with open(var_call_y4LPO2mI1Ro0F0u3bzPyXHZS, 'r') as f:
    businesses = json.load(f)
with open(var_call_6VmKzOdRCjfXiUZME0uPZu9Z, 'r') as f:
    reviews = json.load(f)

# Map state -> set of business_ref ids (like 'businessref_64') that have WiFi
state_wifi_businesses = defaultdict(set)

for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    desc = b.get('description') or ''

    # Determine WiFi presence
    wifi_present = False
    if isinstance(attrs, dict):
        wifi_val = attrs.get('WiFi')
        if wifi_val is not None:
            # normalize to string
            try:
                wifi_str = str(wifi_val).lower()
            except Exception:
                wifi_str = ''
            # consider WiFi present unless it explicitly says 'no' or 'none'
            if 'no' in wifi_str:
                wifi_present = False
            elif 'none' in wifi_str:
                wifi_present = False
            elif wifi_str.strip() == 'false' or wifi_str.strip() == "u'no'":
                wifi_present = False
            elif wifi_str.strip() == 'true' or 'free' in wifi_str or 'paid' in wifi_str or 'yes' in wifi_str:
                wifi_present = True
            else:
                # if it's some other non-empty value, treat as present
                if wifi_str.strip() != '':
                    wifi_present = True
    # If attributes missing or WiFi key absent, treat as no

    if not wifi_present:
        continue

    # Extract state code from description using regex looking for ", XX,"
    state = None
    if isinstance(desc, str):
        m = re.search(r",\s*([A-Z]{2})\s*,", desc)
        if m:
            state = m.group(1)
        else:
            # fallback: look for pattern "in City, ST" or last occurrence of ", ST"
            m2 = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
            if m2:
                state = m2.group(1)
            else:
                m3 = re.search(r",\s*([A-Z]{2})$", desc)
                if m3:
                    state = m3.group(1)

    if state is None:
        continue

    # convert businessid_N to businessref_N
    if bid and bid.startswith('businessid_'):
        suffix = bid.split('_', 1)[1]
        bref = 'businessref_' + suffix
        state_wifi_businesses[state].add(bref)

# Now map reviews to these businesses and compute average ratings per state
state_ratings = defaultdict(list)
for r in reviews:
    bref = r.get('business_ref')
    rating_val = r.get('rating')
    # rating might be string; convert
    try:
        rating = float(rating_val)
    except Exception:
        continue
    # Find which state this business belongs to (if any)
    for st, bref_set in state_wifi_businesses.items():
        if bref in bref_set:
            state_ratings[st].append(rating)

# Compute counts and averages
state_stats = {}
for st, bref_set in state_wifi_businesses.items():
    count = len(bref_set)
    ratings = state_ratings.get(st, [])
    avg = None
    if ratings:
        avg = sum(ratings) / len(ratings)
    state_stats[st] = {'business_count': count, 'avg_rating': avg}

# Find state with highest business_count
best_state = None
best_count = -1
for st, stats in state_stats.items():
    if stats['business_count'] > best_count:
        best_state = st
        best_count = stats['business_count']

# Prepare final output
if best_state is None:
    output = {'state': None, 'business_count': 0, 'avg_rating': None}
else:
    avg = state_stats[best_state]['avg_rating']
    # round avg to 2 decimals if not None
    if avg is not None:
        avg = round(avg, 2)
    output = {'state': best_state, 'business_count': state_stats[best_state]['business_count'], 'avg_rating': avg}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Pr6gYxRZjcnB43AupaBdYmtQ': ['checkin', 'business'], 'var_call_y4LPO2mI1Ro0F0u3bzPyXHZS': 'file_storage/call_y4LPO2mI1Ro0F0u3bzPyXHZS.json', 'var_call_iPxjhs901fN8RTV3wbWlEEQ3': ['review', 'tip', 'user'], 'var_call_6VmKzOdRCjfXiUZME0uPZu9Z': 'file_storage/call_6VmKzOdRCjfXiUZME0uPZu9Z.json'}

exec(code, env_args)
