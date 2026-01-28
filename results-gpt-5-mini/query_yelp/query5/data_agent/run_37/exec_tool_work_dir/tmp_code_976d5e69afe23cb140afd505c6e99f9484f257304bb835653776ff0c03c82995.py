code = """import json
import pandas as pd
import re

# Load query results from storage variables
# var_call_NRgSOxDLNAaPj7RHjFUjTSpC and var_call_zCgw7szMwCttFJTfI5o2QQlr are provided by previous tool calls

businesses_path = var_call_NRgSOxDLNAaPj7RHjFUjTSpC
reviews_path = var_call_zCgw7szMwCttFJTfI5o2QQlr

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize fields
bdf['business_id'] = bdf.get('business_id')
# Ensure attributes column exists
bdf['attributes'] = bdf.get('attributes')

# Function to determine wifi availability
import math

def has_wifi(attr):
    if attr is None:
        return False
    # If it's a dict
    if isinstance(attr, dict):
        # try common keys
        val = None
        for k in attr.keys():
            if str(k).lower().replace('-', '') == 'wifi' or 'wifi' in str(k).lower():
                val = attr[k]
                break
        if val is None:
            # some dicts may have nested string representations
            s = json.dumps(attr)
        else:
            s = str(val)
    else:
        s = str(attr)
    s = s.lower()
    # If it contains 'wifi' and then a value like 'free' or 'no'
    # Check for indicators of offering
    if 'free' in s or 'paid' in s or "yes" in s or 'limited' in s or 'spotty' in s or 'paid' in s:
        return True
    # If explicitly says no
    if "no" in s and 'no wifi' in s or "u'no'" in s or "'no'" in s:
        return False
    # If contains wifi but no explicit no, consider as offering
    if 'wifi' in s:
        # try to see if context implies no
        if 'no' in s and not ('free' in s or 'paid' in s or 'yes' in s):
            return False
        return True
    return False

# Extract US state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # common pattern: ' in CITY, ST,' or ' in CITY, ST.' or ' in CITY, ST '
    m = re.search(r" in [^,]+,\s*([A-Z]{2})(?:\b|,|\.)", desc)
    if m:
        return m.group(1)
    # fallback: last occurrence of comma then space and two letters
    m2 = re.search(r",\s*([A-Z]{2})[,\.]?\s", desc)
    if m2:
        return m2.group(1)
    return None

# Apply
bdf['has_wifi'] = bdf['attributes'].apply(has_wifi)
bdf['state'] = bdf['description'].apply(extract_state)

# Filter businesses that offer wifi and have a state
wifi_biz = bdf[(bdf['has_wifi'] == True) & (bdf['state'].notnull())].copy()

# Map business_id to business_ref
wifi_biz['business_ref'] = wifi_biz['business_id'].astype(str).str.replace('businessid_', 'businessref_')

# Count per state
state_counts = wifi_biz.groupby('state').size().reset_index(name='count')
if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    state_counts = state_counts.sort_values('count', ascending=False)
    top_state = state_counts.iloc[0]['state']
    top_count = int(state_counts.iloc[0]['count'])

    # Get reviews for businesses in that state
    biz_refs = set(wifi_biz[wifi_biz['state']==top_state]['business_ref'].tolist())
    rdf = rdf[rdf['business_ref'].isin(biz_refs)].copy()
    # Convert rating to numeric
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
    # Compute average rating across all reviews for these businesses
    if rdf['rating'].count() == 0:
        avg_rating = None
    else:
        avg_rating = float(rdf['rating'].mean())
    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4Rh4sBmIXcEGrGmSrzMLUeeE': ['business', 'checkin'], 'var_call_cwihfXd0wJ8W2rVCS2RLBXUW': ['review', 'tip', 'user'], 'var_call_NRgSOxDLNAaPj7RHjFUjTSpC': 'file_storage/call_NRgSOxDLNAaPj7RHjFUjTSpC.json', 'var_call_zCgw7szMwCttFJTfI5o2QQlr': 'file_storage/call_zCgw7szMwCttFJTfI5o2QQlr.json'}

exec(code, env_args)
