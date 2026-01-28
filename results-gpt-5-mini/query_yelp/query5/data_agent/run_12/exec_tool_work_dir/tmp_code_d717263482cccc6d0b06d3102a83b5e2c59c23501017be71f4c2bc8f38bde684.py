code = """import json
import re
import statistics

# Load large results from files provided in storage
with open(var_call_erZssGyaGbFXiIeNsXWVCDmT, 'r') as f:
    businesses = json.load(f)
with open(var_call_xj4IbcGEMiW1pGy9HBTrqudB, 'r') as f:
    reviews = json.load(f)

# Helper to extract 2-letter state code from description
def extract_state(desc):
    if not desc:
        return None
    # Try pattern: 'in City, ST' e.g., 'in King of Prussia, PA'
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    # Fallback: find patterns like ', ST,' or ', ST.'
    m = re.search(r',\s*([A-Z]{2})[,\.]', desc)
    if m:
        return m.group(1)
    return None

# Build mapping of business_ref -> list of ratings
ratings_by_business = {}
for r in reviews:
    br = r.get('business_ref')
    rt = r.get('rating')
    try:
        rt_val = float(rt)
    except Exception:
        continue
    ratings_by_business.setdefault(br, []).append(rt_val)

# Filter businesses that have WiFi (exclude values containing 'no')
wifi_businesses = []
for b in businesses:
    attrs = b.get('attributes') or {}
    wifi = attrs.get('WiFi')
    if wifi is None:
        continue
    wifi_str = str(wifi).lower()
    # Exclude explicit 'no'
    if "no" in wifi_str:
        continue
    # Otherwise treat as offering wifi
    state = extract_state(b.get('description',''))
    wifi_businesses.append({
        'business_id': b.get('business_id'),
        'business_ref': b.get('business_id').replace('businessid_', 'businessref_'),
        'wifi': wifi_str,
        'state': state
    })

# Count by state
counts = {}
for wb in wifi_businesses:
    st = wb['state'] or 'Unknown'
    counts[st] = counts.get(st, 0) + 1

# Find state with max count
if counts:
    top_state = max(counts.items(), key=lambda x: x[1])[0]
    top_count = counts[top_state]
else:
    top_state = None
    top_count = 0

# Collect ratings for businesses in top_state
business_refs_in_state = {wb['business_ref'] for wb in wifi_businesses if (wb['state'] or 'Unknown') == top_state}
all_ratings = []
for br in business_refs_in_state:
    all_ratings.extend(ratings_by_business.get(br, []))

if all_ratings:
    avg_rating = round(sum(all_ratings) / len(all_ratings), 2)
else:
    avg_rating = None

result = {
    'state': top_state,
    'wifi_business_count': top_count,
    'average_rating': avg_rating
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fvSx3t3JDkO9Qh3rEhFPFQGP': ['business', 'checkin'], 'var_call_VHpaMZxD2MzBNFnn1DCuSx48': ['review', 'tip', 'user'], 'var_call_erZssGyaGbFXiIeNsXWVCDmT': 'file_storage/call_erZssGyaGbFXiIeNsXWVCDmT.json', 'var_call_xj4IbcGEMiW1pGy9HBTrqudB': 'file_storage/call_xj4IbcGEMiW1pGy9HBTrqudB.json'}

exec(code, env_args)
