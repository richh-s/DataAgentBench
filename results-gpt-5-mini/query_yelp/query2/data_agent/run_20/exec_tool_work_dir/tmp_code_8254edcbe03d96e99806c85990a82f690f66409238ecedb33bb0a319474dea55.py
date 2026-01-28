code = """import json, re

# Load data files from storage variables
with open(var_call_xRvLcaXo6zgBS4eoYBt3DSFd, 'r') as f:
    businesses = json.load(f)
with open(var_call_iAS6QM9bvra6CYQwKPIcSeYA, 'r') as f:
    reviews = json.load(f)

# Build mapping from business numeric id to state abbreviation
id2state = {}
state_pattern = re.compile(r",\s*([A-Z]{2})(?:\b|,)")
for b in businesses:
    bid = b.get('business_id', '')
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    if m:
        state = m.group(1)
    else:
        m2 = re.search(r"in\s+[A-Za-z .'\-]+,\s*([A-Z]{2})", desc)
        state = m2.group(1) if m2 else None
    if not state:
        continue
    m_id = re.search(r'businessid_(\d+)', bid)
    if m_id:
        id2state[m_id.group(1)] = state

# Aggregate reviews by state
state_counts = {}
state_rating_sums = {}
for r in reviews:
    bref = r.get('business_ref', '')
    m = re.search(r'businessref_(\d+)', bref)
    if not m:
        continue
    num = m.group(1)
    state = id2state.get(num)
    if not state:
        continue
    try:
        rating = int(r.get('rating'))
    except Exception:
        continue
    state_counts[state] = state_counts.get(state, 0) + 1
    state_rating_sums[state] = state_rating_sums.get(state, 0) + rating

if not state_counts:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    count = state_counts[max_state]
    avg = state_rating_sums[max_state] / count
    result = {"state": max_state, "review_count": count, "average_rating": round(avg, 3)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_l5UUKrUOPUf3VhWQL7laIgsb': ['checkin', 'business'], 'var_call_65A5SlEdkJTI60EgG0FESMtk': ['review', 'tip', 'user'], 'var_call_xRvLcaXo6zgBS4eoYBt3DSFd': 'file_storage/call_xRvLcaXo6zgBS4eoYBt3DSFd.json', 'var_call_iAS6QM9bvra6CYQwKPIcSeYA': 'file_storage/call_iAS6QM9bvra6CYQwKPIcSeYA.json'}

exec(code, env_args)
