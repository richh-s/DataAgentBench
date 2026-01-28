code = """import json, re

# Load the data from storage variables which are file paths
bpath = var_call_gCco11Qxl6IA7Otuqc4Ddf96
rpath = var_call_Bk4Jivcw3PJuKBbVnCyASGft

with open(bpath, 'r') as f:
    businesses = json.load(f)
with open(rpath, 'r') as f:
    reviews = json.load(f)

# Helper to extract state from description
state_regex = re.compile(r',\s*([A-Z]{2})(?:\b|,)', re.UNICODE)

def extract_state(desc):
    if not desc:
        return None
    matches = state_regex.findall(desc)
    if matches:
        return matches[-1]
    # fallback
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    return None

# Build mapping from business numeric id (tail) to state
biz_state = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description')
    if not bid:
        continue
    tail = bid.rsplit('_', 1)[-1]
    st = extract_state(desc)
    if st:
        biz_state[tail] = st

# Aggregate reviews by state
state_counts = {}
state_rating_sum = {}

for rv in reviews:
    bref = rv.get('business_ref')
    rating = rv.get('rating')
    if bref is None or rating is None:
        continue
    tail = bref.rsplit('_', 1)[-1]
    st = biz_state.get(tail)
    if not st:
        continue
    try:
        r = float(rating)
    except:
        continue
    state_counts[st] = state_counts.get(st, 0) + 1
    state_rating_sum[st] = state_rating_sum.get(st, 0.0) + r

if not state_counts:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # Find state with max reviews
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    cnt = state_counts[top_state]
    avg = state_rating_sum[top_state] / cnt if cnt else None
    # round to 2 decimals
    avg = round(avg, 2) if avg is not None else None
    result = {"state": top_state, "review_count": cnt, "average_rating": avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gCco11Qxl6IA7Otuqc4Ddf96': 'file_storage/call_gCco11Qxl6IA7Otuqc4Ddf96.json', 'var_call_Bk4Jivcw3PJuKBbVnCyASGft': 'file_storage/call_Bk4Jivcw3PJuKBbVnCyASGft.json'}

exec(code, env_args)
