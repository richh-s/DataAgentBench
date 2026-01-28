code = """import json, re, os

# Load data from previous query results files
with open(var_call_rcKwY0tZ8gZaTyNcOYojszY5, 'r') as f:
    businesses = json.load(f)
with open(var_call_PaRLHQtNsZun6q93ETo9SRij, 'r') as f:
    reviews = json.load(f)

# US state codes
state_codes = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    # First try pattern like ', XX' or ' XX, ' or ' XX.' etc.
    m = re.search(r',\s*([A-Z]{2})(?:[,\.\s]|$)', desc)
    if m and m.group(1) in state_codes:
        return m.group(1)
    # fallback: find any two-letter uppercase tokens that are valid state codes
    tokens = re.findall(r'\b([A-Z]{2})\b', desc)
    for t in tokens:
        if t in state_codes:
            return t
    return None

# Build mapping from numeric id -> state
id_to_state = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description')
    if not bid:
        continue
    # extract numeric id after prefix
    parts = bid.split('_')
    if len(parts) >= 2:
        num = parts[1]
    else:
        num = bid
    state = extract_state(desc)
    if state:
        id_to_state[num] = state

# Aggregate review counts and rating sums per state
from collections import defaultdict
counts = defaultdict(int)
rating_sums = defaultdict(float)

for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    if not bref:
        continue
    parts = bref.split('_')
    if len(parts) >= 2:
        num = parts[1]
    else:
        num = bref
    state = id_to_state.get(num)
    if not state:
        continue
    try:
        rating_val = float(rating)
    except:
        continue
    counts[state] += 1
    rating_sums[state] += rating_val

if not counts:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # find state with max reviews
    max_state = max(counts.items(), key=lambda x: x[1])[0]
    rc = counts[max_state]
    avg = rating_sums[max_state] / rc if rc else None
    if avg is not None:
        avg = round(avg, 3)
    result = {"state": max_state, "review_count": rc, "average_rating": avg}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_r5TBeNLfoF3G31a203vGZX1V': ['business', 'checkin'], 'var_call_I03japIEsRQQKuIKyYPFf49v': ['review', 'tip', 'user'], 'var_call_rcKwY0tZ8gZaTyNcOYojszY5': 'file_storage/call_rcKwY0tZ8gZaTyNcOYojszY5.json', 'var_call_PaRLHQtNsZun6q93ETo9SRij': 'file_storage/call_PaRLHQtNsZun6q93ETo9SRij.json'}

exec(code, env_args)
