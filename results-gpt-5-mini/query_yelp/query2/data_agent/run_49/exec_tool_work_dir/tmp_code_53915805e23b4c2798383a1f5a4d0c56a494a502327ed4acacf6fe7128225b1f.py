code = """import json
import re
import pandas as pd

# Load data from previous tool calls
# var_call_2zESRXQokhF5Lf5iMBJbnpbn and var_call_iTkaQoBL33XRjP3WrF6keht3 are available in storage

# helper to load possibly-filepath or list

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to json
        with open(v, 'r') as f:
            return json.load(f)
    return v

business_records = load_var(var_call_2zESRXQokhF5Lf5iMBJbnpbn)
review_records = load_var(var_call_iTkaQoBL33XRjP3WrF6keht3)

# US state codes
states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

# Build mapping from business_ref to state
bizref_to_state = {}

for b in business_records:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    if not bid:
        continue
    # convert businessid_ -> businessref_
    if bid.startswith('businessid_'):
        bref = 'businessref_' + bid.split('businessid_')[-1]
    else:
        bref = bid
    # find state by searching for any state code in description
    found_state = None
    # Prefer patterns like ', XX' or ' XX,' or ' XX.'
    for m in re.findall(r'\b([A-Z]{2})\b', desc):
        if m in states:
            found_state = m
            break
    if found_state:
        bizref_to_state[bref] = found_state

# Aggregate reviews per state
from collections import defaultdict
state_counts = defaultdict(int)
state_rating_sums = defaultdict(float)

for r in review_records:
    bref = r.get('business_ref')
    rating = r.get('rating')
    try:
        rating_val = float(rating)
    except:
        continue
    st = bizref_to_state.get(bref)
    if st:
        state_counts[st] += 1
        state_rating_sums[st] += rating_val

# If no mapped reviews, return empty
if not state_counts:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    # find state with highest number of reviews
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    total = state_counts[max_state]
    avg = state_rating_sums[max_state] / total if total>0 else None
    if avg is not None:
        avg = round(avg, 3)
    result = {"state": max_state, "total_reviews": total, "average_rating": avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5WRzRpXAfI3DswmAJC6LyAJg': ['business', 'checkin'], 'var_call_TswX3NFH0hPFBvda8Rluvpwq': ['review', 'tip', 'user'], 'var_call_2YqDNDO27mXYKnAbO6OxgAPy': 'file_storage/call_2YqDNDO27mXYKnAbO6OxgAPy.json', 'var_call_2zESRXQokhF5Lf5iMBJbnpbn': 'file_storage/call_2zESRXQokhF5Lf5iMBJbnpbn.json', 'var_call_iTkaQoBL33XRjP3WrF6keht3': 'file_storage/call_iTkaQoBL33XRjP3WrF6keht3.json'}

exec(code, env_args)
