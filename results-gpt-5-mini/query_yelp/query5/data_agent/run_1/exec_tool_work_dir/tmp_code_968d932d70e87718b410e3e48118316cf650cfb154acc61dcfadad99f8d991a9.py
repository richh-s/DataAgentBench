code = """import json
import re
import pandas as pd

# Load data from storage file paths
business_path = var_call_WdZ0Goe0ln4Fz9Nxhju7VQTS
review_path = var_call_Be4nNd4niiBxZMMYL4xJTJMv

with open(business_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(review_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure attributes is dict where possible
# Some attributes may be strings; keep as-is but handle missing

def gets_wifi_attr(attr):
    if not isinstance(attr, dict):
        return None
    # Keys may include 'WiFi' or 'wifi'
    for k in attr.keys():
        if k.lower() == 'wifi':
            return attr[k]
    return None

bdf['wifi_val'] = bdf['attributes'].apply(gets_wifi_attr)

# Normalize wifi_val to string lower for checking
bdf['wifi_val_str'] = bdf['wifi_val'].astype(str).fillna('').str.lower()

# Consider as offering wifi if wifi_val exists and does not contain 'no' or 'none' or 'false' or 'nul'
def offers_wifi(s):
    if not s or s in ['nan', 'none', "{}"]:
        return False
    # remove leading u' or surrounding quotes
    s2 = re.sub(r"[uU]?'", "", s)
    s2 = s2.replace("'", "").replace('"','').strip()
    if not s2:
        return False
    if 'no' in s2:
        return False
    if 'false' in s2:
        return False
    # if contains free or paid or yes, consider offering
    if any(k in s2 for k in ['free','paid','yes','true']):
        return True
    # If it's a non-empty string that is not 'no', treat as offering
    return True

bdf['offers_wifi'] = bdf['wifi_val_str'].apply(offers_wifi)

# Extract state from description using regex

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Try pattern: in City, ST,
    m = re.search(r'in\s+[^,]+,\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    # Try alternative: , ST,
    m = re.search(r',\s*([A-Z]{2})\s*(?:,|$)', desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Filter businesses that offer wifi and have a state
wifi_b = bdf[(bdf['offers_wifi']==True) & (bdf['state'].notnull())]

# Count per state
state_counts = wifi_b.groupby('state').size().reset_index(name='wifi_business_count')

if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top = state_counts.sort_values('wifi_business_count', ascending=False).iloc[0]
    top_state = top['state']
    top_count = int(top['wifi_business_count'])

    # Map business_id to business_ref by replacing prefix
    def to_business_ref(bid):
        if isinstance(bid, str) and bid.startswith('businessid_'):
            return 'businessref_' + bid.split('_',1)[1]
        return bid

    wifi_b['business_ref'] = wifi_b['business_id'].apply(to_business_ref)
    wifi_refs = set(wifi_b['business_ref'].dropna().unique())

    # Filter reviews for these business_refs
    if rdf.empty:
        avg_rating = None
    else:
        # Ensure rating numeric
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
        mask = rdf['business_ref'].isin(wifi_refs)
        relevant_reviews = rdf[mask]
        if relevant_reviews.empty:
            avg_rating = None
        else:
            avg_rating = float(relevant_reviews['rating'].mean())

    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': round(avg_rating, 2) if avg_rating is not None else None}

# Print in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Kpe73YRlhqAcGQOC9LK2TNJE': ['checkin', 'business'], 'var_call_WdZ0Goe0ln4Fz9Nxhju7VQTS': 'file_storage/call_WdZ0Goe0ln4Fz9Nxhju7VQTS.json', 'var_call_HjGfsCeKZVBaxyr9F4r5ChsI': ['review', 'tip', 'user'], 'var_call_Be4nNd4niiBxZMMYL4xJTJMv': 'file_storage/call_Be4nNd4niiBxZMMYL4xJTJMv.json'}

exec(code, env_args)
