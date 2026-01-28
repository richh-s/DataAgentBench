code = """import json
# Load the businesses result from MongoDB stored in a file path variable
data_path = var_call_bC8pABsUSjz4LtTsWdS3euDX
with open(data_path, 'r') as f:
    businesses = json.load(f)

# Filter businesses that explicitly accept credit cards
accepting = []
for b in businesses:
    attrs = b.get('attributes') or {}
    val = attrs.get('BusinessAcceptsCreditCards')
    if isinstance(val, str) and val.strip().lower() == 'true':
        accepting.append({'business_id': b.get('business_id'), 'categories': b.get('categories')})

# Prepare mapping: categories (split by comma) -> list of business_ref (transform id prefix)
from collections import defaultdict
cat_map = defaultdict(list)
all_business_refs = set()
for b in accepting:
    bid = b['business_id']
    if not bid:
        continue
    bref = bid.replace('businessid_','businessref_')
    all_business_refs.add(bref)
    cats = b.get('categories')
    if not cats:
        continue
    # categories might be a list or a string; handle both
    if isinstance(cats, list):
        items = cats
    else:
        # split on comma
        items = [c.strip() for c in str(cats).split(',') if c.strip()]
    for c in items:
        cat_map[c].append(bref)

# Convert defaultdict to regular dict
cat_map = {k: list(set(v)) for k,v in cat_map.items()}
all_business_refs = sorted(list(all_business_refs))

out = {'business_refs': all_business_refs, 'category_to_business_refs': cat_map}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_o0m9KMh4DDuBhn2XVu2q6QDi': ['business', 'checkin'], 'var_call_lsdmMUuJCJNnxnXhv8E45hwq': ['review', 'tip', 'user'], 'var_call_bC8pABsUSjz4LtTsWdS3euDX': 'file_storage/call_bC8pABsUSjz4LtTsWdS3euDX.json'}

exec(code, env_args)
