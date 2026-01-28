code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_gbwHwSqbysbBryWZr9Ne041T, 'r') as f:
    businesses = json.load(f)
with open(var_call_jLB6pH4qk33x9BnnCCX5Ho4f, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize columns
if 'attributes' not in bdf.columns:
    bdf['attributes'] = None
if 'description' not in bdf.columns:
    bdf['description'] = ''

# Function to extract WiFi attribute
def parse_wifi(attr):
    if not attr or attr=="None":
        return None
    # attr may be dict or string
    if isinstance(attr, dict):
        wifi = attr.get('WiFi') or attr.get('wifi')
    else:
        # string representation of dict or other
        s = str(attr)
        # try to find WiFi entry
        m = re.search(r"WiFi\s*\:\s*([^,}\']+|'[^']+'|\"[^\"]+\")", s)
        if m:
            wifi = m.group(1)
        else:
            # maybe pattern "\"WiFi\"\: 'free'"
            m2 = re.search(r"WiFi" + "[^\w]*([a-zA-Z']+)", s)
            wifi = m2.group(1) if m2 else None
    if wifi is None:
        return None
    w = str(wifi).lower()
    # clean common prefixes like u'free'
    w = w.replace("u'", "").replace("\"", "").replace("'", "")
    w = w.strip()
    return w

bdf['wifi_raw'] = bdf['attributes'].apply(parse_wifi)

# Determine if business offers wifi: True if wifi_raw contains not 'no' and not 'none' and not empty
def offers_wifi(val):
    if val is None:
        return False
    v = str(val).lower()
    if v in ['no', 'none', 'false', 'na', 'n']:
        return False
    # if contains 'no'
    if 'no' in v and 'free' not in v and 'paid' not in v and 'yes' not in v:
        return False
    return True

bdf['offers_wifi'] = bdf['wifi_raw'].apply(offers_wifi)

# Extract state from description using regex for two-letter state
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # look for pattern ", ST," or ", ST" near end
    m = re.search(r",\s*([A-Z]{2})(?:\b|,|\s)", desc)
    if m:
        return m.group(1)
    # fallback: last two letter before end
    m2 = re.search(r"\b([A-Z]{2})\b", desc)
    return m2.group(1) if m2 else None

bdf['state'] = bdf['description'].apply(extract_state)

# Filter businesses that offer wifi and have a US state
wifi_biz = bdf[bdf['offers_wifi'] & bdf['state'].notnull()].copy()

# Map business_id to business_ref
wifi_biz['business_ref'] = wifi_biz['business_id'].str.replace('businessid_', 'businessref_')

# Prepare reviews DF
if 'business_ref' not in rdf.columns or 'rating' not in rdf.columns:
    raise ValueError('Reviews missing expected columns')
rdf = rdf[['business_ref', 'rating']].copy()
# Convert rating to numeric
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Join reviews to wifi businesses by business_ref
merged = pd.merge(rdf, wifi_biz[['business_ref', 'state']], on='business_ref', how='inner')

# Compute per-state counts (count of distinct businesses offering wifi) and average rating (across reviews)
state_counts = wifi_biz.groupby('state')['business_id'].nunique().rename('wifi_business_count')
state_avg_rating = merged.groupby('state')['rating'].mean().rename('average_rating')

summary = pd.concat([state_counts, state_avg_rating], axis=1).fillna({'average_rating': None}).reset_index()

# Ensure numeric types and rounding average_rating to 3 decimals if not None
def safe_round(x):
    if x is None or (pd.isna(x)):
        return None
    return float(round(float(x), 3))

summary['average_rating'] = summary['average_rating'].apply(safe_round)
summary['wifi_business_count'] = summary['wifi_business_count'].astype(int)

# Find state with max wifi_business_count. If tie, choose the one with higher average_rating, then alphabetically.
if summary.shape[0] == 0:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    max_count = summary['wifi_business_count'].max()
    candidates = summary[summary['wifi_business_count'] == max_count].copy()
    # sort candidates by average_rating desc (treat None as -inf), then state
    candidates['avg_sort'] = candidates['average_rating'].apply(lambda x: x if x is not None else -999)
    candidates = candidates.sort_values(by=['avg_sort', 'state'], ascending=[False, True])
    top = candidates.iloc[0]
    result = {'state': top['state'], 'wifi_business_count': int(top['wifi_business_count']), 'average_rating': top['average_rating']}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_o67tVfb3ILfk4WUAiMTMgalH': ['checkin', 'business'], 'var_call_8mPFtwEhbfv4OhNqKH5qEJnN': ['review', 'tip', 'user'], 'var_call_gbwHwSqbysbBryWZr9Ne041T': 'file_storage/call_gbwHwSqbysbBryWZr9Ne041T.json', 'var_call_jLB6pH4qk33x9BnnCCX5Ho4f': 'file_storage/call_jLB6pH4qk33x9BnnCCX5Ho4f.json'}

exec(code, env_args)
