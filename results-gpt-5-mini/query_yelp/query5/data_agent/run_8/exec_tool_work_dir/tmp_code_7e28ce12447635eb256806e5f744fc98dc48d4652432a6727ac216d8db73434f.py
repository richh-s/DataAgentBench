code = """import json
import pandas as pd
import re

# Load the data from storage-provided file paths
with open(var_call_ke4csq1odDsZ5jDna6BZg10x, 'r') as f:
    businesses = json.load(f)
with open(var_call_1VRKG9ExWZfDquy9UaVQWCMk, 'r') as f:
    reviews = json.load(f)

# Create DataFrame for businesses
bdf = pd.DataFrame(businesses)
# Keep necessary columns
bdf = bdf[['business_id', 'attributes', 'description']].copy()

# Function to extract state from description
def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    # Look for patterns like 'City, ST,' or 'City, ST' or '..., ST.'
    m = re.search(r",\s*([A-Z]{2})(?:[,\.\s]|$)", desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Determine WiFi availability
def has_wifi(attr):
    if not attr or attr == 'None':
        return False
    # attr might be dict or string. Convert to string for searching.
    s = str(attr).lower()
    # If contains "no" explicitly and not other positive words, treat as no
    if "no" in s and not ("free" in s or "paid" in s or "yes" in s or "true" in s):
        return False
    # If contains free/paid/yes/true/wifi
    if any(x in s for x in ["free", "paid", "yes", "true", "wifi"]):
        # But ensure it's not like "no"
        if "no" in s and not any(x in s for x in ["free", "paid", "yes", "true"]):
            return False
        return True
    return False

bdf['has_wifi'] = bdf['attributes'].apply(has_wifi)

# Filter to wifi businesses
wifi_biz = bdf[bdf['has_wifi'] & bdf['state'].notnull()].copy()

# Build reviews DataFrame
rdf = pd.DataFrame(reviews)
# Convert rating to numeric
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
# Map business_ref to business_id (prefix change)
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_', 'businessid_')

# Join reviews to wifi businesses
merged = rdf.merge(wifi_biz[['business_id','state']], on='business_id', how='inner')

# Compute per-state counts of distinct wifi businesses
state_counts = wifi_biz.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

# Compute per-state average rating across reviews for businesses offering wifi
state_avg_rating = merged.groupby('state')['rating'].mean().reset_index(name='average_rating')

# Combine
state_stats = state_counts.merge(state_avg_rating, on='state', how='left')

# If there are no reviews for a state's wifi businesses, average_rating will be NaN; leave as None
state_stats['average_rating'] = state_stats['average_rating'].round(2)
state_stats['average_rating'] = state_stats['average_rating'].where(state_stats['average_rating'].notnull(), None)

# Find state with highest wifi_business_count
if state_stats.empty:
    result = {"state": None, "wifi_business_count": 0, "average_rating": None}
else:
    top = state_stats.sort_values(['wifi_business_count','state'], ascending=[False, True]).iloc[0]
    result = {"state": top['state'], "wifi_business_count": int(top['wifi_business_count']), "average_rating": (float(top['average_rating']) if top['average_rating'] is not None else None)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1udLSQtaLsG2M3Kh7p6SWFZK': ['checkin', 'business'], 'var_call_NEYTdzndAtVLQ2ffBjjbsN8C': ['review', 'tip', 'user'], 'var_call_ke4csq1odDsZ5jDna6BZg10x': 'file_storage/call_ke4csq1odDsZ5jDna6BZg10x.json', 'var_call_1VRKG9ExWZfDquy9UaVQWCMk': 'file_storage/call_1VRKG9ExWZfDquy9UaVQWCMk.json'}

exec(code, env_args)
