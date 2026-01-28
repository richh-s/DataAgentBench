code = """import json
import re
import pandas as pd

# Load data from storage files
with open(var_call_ZHYt4lVjjiVCKbxoHNoaMZtI, 'r') as f:
    businesses = json.load(f)
with open(var_call_a1lRN9cHPEZ1ZENKngXFDt5u, 'r') as f:
    reviews = json.load(f)

# Build mapping from review business_ref to state
state_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    # Try to extract state abbreviation
    m = re.search(r'in\s+[^,]+,\s*([A-Z]{2})', desc)
    if not m:
        m = re.search(r',\s*([A-Z]{2})\b', desc)
    state = m.group(1) if m else None
    if bid:
        # map review prefix form to state
        state_map[bid.replace('businessid_','businessref_')] = state

# Aggregate reviews by state
rows = []
for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    try:
        rating = float(rating)
    except:
        continue
    state = state_map.get(bref)
    if state:
        rows.append({'state': state, 'rating': rating})

if not rows:
    result = {'state': None, 'review_count': 0, 'average_rating': None}
else:
    df = pd.DataFrame(rows)
    grp = df.groupby('state').agg(review_count=('rating','count'), avg_rating=('rating','mean')).reset_index()
    best = grp.sort_values(['review_count','avg_rating'], ascending=[False,False]).iloc[0]
    result = {'state': best['state'], 'review_count': int(best['review_count']), 'average_rating': round(float(best['avg_rating']), 3)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZHYt4lVjjiVCKbxoHNoaMZtI': 'file_storage/call_ZHYt4lVjjiVCKbxoHNoaMZtI.json', 'var_call_a1lRN9cHPEZ1ZENKngXFDt5u': 'file_storage/call_a1lRN9cHPEZ1ZENKngXFDt5u.json'}

exec(code, env_args)
