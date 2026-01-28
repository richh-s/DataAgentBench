code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_gbwHwSqbysbBryWZr9Ne041T, 'r') as f:
    businesses = json.load(f)
with open(var_call_jLB6pH4qk33x9BnnCCX5Ho4f, 'r') as f:
    reviews = json.load(f)

# DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure columns
bdf['attributes'] = bdf.get('attributes', None)
bdf['description'] = bdf.get('description', '')

# Parse WiFi attribute
def parse_wifi(attr):
    if attr is None or attr == 'None':
        return None
    if isinstance(attr, dict):
        wifi = attr.get('WiFi') or attr.get('wifi')
    else:
        s = str(attr)
        # Look for WiFi patterns like "WiFi": "u'free'" or "WiFi": "free" or "WiFi': 'free'"
        m = re.search(r"WiFi\s*[:=]\s*('?\w+\'?|\"?u'\w+'\"?)", s)
        if m:
            wifi = m.group(1)
        else:
            # fallback: find WiFi followed by nonword then word
            m2 = re.search(r"WiFi[^\w]*(\w+)", s)
            wifi = m2.group(1) if m2 else None
    if wifi is None:
        return None
    w = str(wifi)
    w = w.lower()
    w = w.replace("u'", "").replace("\"", "").replace("'", "").strip()
    return w

bdf['wifi_raw'] = bdf['attributes'].apply(parse_wifi)

# Determine if offers wifi
def offers_wifi(val):
    if val is None:
        return False
    v = str(val).lower()
    if v in ['no', 'none', 'false', 'n']:
        return False
    # if contains no as whole word and not free/paid/yes
    if re.search(r"\bno\b", v) and not any(x in v for x in ['free','paid','yes']):
        return False
    return True

bdf['offers_wifi'] = bdf['wifi_raw'].apply(offers_wifi)

# Extract state from description
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # common pattern: ", ST,"
    m = re.search(r",\s*([A-Z]{2})\b", desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Filter wifi businesses with state
wifi_biz = bdf[bdf['offers_wifi'] & bdf['state'].notnull()].copy()
wifi_biz['business_ref'] = wifi_biz['business_id'].str.replace('businessid_', 'businessref_')

# Prepare reviews
rdf = rdf[['business_ref', 'rating']].copy()
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Join reviews for wifi businesses
merged = pd.merge(rdf, wifi_biz[['business_ref', 'state']], on='business_ref', how='inner')

# Compute distinct wifi business count per state
state_counts = wifi_biz.groupby('state')['business_id'].nunique().rename('wifi_business_count')
# Compute average rating per state across reviews
state_avg_rating = merged.groupby('state')['rating'].mean().rename('average_rating')

summary = pd.concat([state_counts, state_avg_rating], axis=1).reset_index()

# Round average_rating
summary['average_rating'] = summary['average_rating'].apply(lambda x: None if pd.isna(x) else float(round(float(x), 3)))
summary['wifi_business_count'] = summary['wifi_business_count'].astype(int)

# Select top state by wifi_business_count, tie-breaker average_rating then state name
if summary.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    max_count = summary['wifi_business_count'].max()
    candidates = summary[summary['wifi_business_count'] == max_count].copy()
    candidates['avg_sort'] = candidates['average_rating'].apply(lambda x: x if x is not None else -999)
    candidates = candidates.sort_values(by=['avg_sort', 'state'], ascending=[False, True])
    top = candidates.iloc[0]
    result = {'state': top['state'], 'wifi_business_count': int(top['wifi_business_count']), 'average_rating': top['average_rating']}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_o67tVfb3ILfk4WUAiMTMgalH': ['checkin', 'business'], 'var_call_8mPFtwEhbfv4OhNqKH5qEJnN': ['review', 'tip', 'user'], 'var_call_gbwHwSqbysbBryWZr9Ne041T': 'file_storage/call_gbwHwSqbysbBryWZr9Ne041T.json', 'var_call_jLB6pH4qk33x9BnnCCX5Ho4f': 'file_storage/call_jLB6pH4qk33x9BnnCCX5Ho4f.json'}

exec(code, env_args)
