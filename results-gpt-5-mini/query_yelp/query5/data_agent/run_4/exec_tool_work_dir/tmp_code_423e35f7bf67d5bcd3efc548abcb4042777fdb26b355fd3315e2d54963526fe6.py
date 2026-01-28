code = """import json
import re
import pandas as pd

# Load business records
bp = var_call_LpLDjVcmHyTAvdRm1XTMh1C7
if isinstance(bp, str):
    with open(bp, 'r') as f:
        businesses = json.load(f)
else:
    businesses = bp

# Load review records
rp = var_call_6Ln4lLcgGvccoyYcX9OHu5Dh
if isinstance(rp, str):
    with open(rp, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rp

# Normalize businesses into DataFrame
bdf = pd.DataFrame(businesses)
# Ensure columns exist
for col in ['business_id', 'attributes', 'description', 'name']:
    if col not in bdf.columns:
        bdf[col] = None

# Function to determine if business offers WiFi
def offers_wifi(attr):
    if not attr:
        return False
    # If attr is a dict
    if isinstance(attr, dict):
        val = attr.get('WiFi') or attr.get('wifi') or attr.get('Wi-Fi')
        if val is None:
            return False
        s = str(val).lower()
        # treat as not offering if contains 'no' explicitly
        if 'no' in s:
            return False
        # otherwise if it contains anything (free/paid/yes), treat as offering
        return True
    # If attr is a string, try to find WiFi key
    s = str(attr)
    if 'wifi' in s.lower():
        # attempt to extract value after wifi
        m = re.search(r"wifi\W*[:=']*\s*([^,}\']+)", s, flags=re.I)
        if m:
            val = m.group(1).lower()
            if 'no' in val:
                return False
            return True
        # if wifi mentioned but no 'no', assume offering
        return True
    return False

bdf['offers_wifi'] = bdf['attributes'].apply(offers_wifi)

# Function to extract state from description
def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    # Try patterns
    m = re.search(r'in [^,]+,\s*([A-Z]{2})(?:\b|,)', desc)
    if m:
        return m.group(1)
    m = re.search(r',\s*([A-Z]{2})\s', desc)
    if m:
        return m.group(1)
    # fallback: find any two-letter uppercase word
    m = re.search(r'\b([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Create business_ref by replacing prefix
bdf['business_ref'] = bdf['business_id'].astype(str).str.replace('businessid_', 'businessref_')

# Filter wifi businesses with a valid state
wifi_biz = bdf[(bdf['offers_wifi']) & (bdf['state'].notnull())].copy()

# Count businesses by state
state_counts = wifi_biz.groupby('state')['business_ref'].nunique().reset_index(name='wifi_business_count')
if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    # find state with highest count
    top = state_counts.sort_values(['wifi_business_count','state'], ascending=[False, True]).iloc[0]
    top_state = top['state']
    top_count = int(top['wifi_business_count'])

    # Load reviews DataFrame
    rdf = pd.DataFrame(reviews)
    # Ensure rating numeric
    if 'rating' in rdf.columns:
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
    else:
        rdf['rating'] = pd.Series(dtype='float')

    # Filter reviews to those for businesses offering wifi in top_state
    wifi_refs_in_top = wifi_biz[wifi_biz['state']==top_state]['business_ref'].unique().tolist()
    if wifi_refs_in_top:
        filtered_reviews = rdf[rdf['business_ref'].isin(wifi_refs_in_top)]
        if not filtered_reviews.empty:
            avg_rating = float(filtered_reviews['rating'].mean())
        else:
            avg_rating = None
    else:
        avg_rating = None

    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': avg_rating}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_3ydEMD4zWmPLNEOy72JGnEfA': ['business', 'checkin'], 'var_call_J2bCbtK65MCssI388Ak8Fsb5': ['review', 'tip', 'user'], 'var_call_LpLDjVcmHyTAvdRm1XTMh1C7': 'file_storage/call_LpLDjVcmHyTAvdRm1XTMh1C7.json', 'var_call_6Ln4lLcgGvccoyYcX9OHu5Dh': 'file_storage/call_6Ln4lLcgGvccoyYcX9OHu5Dh.json'}

exec(code, env_args)
