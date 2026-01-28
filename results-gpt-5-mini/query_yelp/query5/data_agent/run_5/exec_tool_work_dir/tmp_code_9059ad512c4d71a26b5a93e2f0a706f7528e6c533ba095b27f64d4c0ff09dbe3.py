code = """import json
import pandas as pd
import re

# Load data from previous tool calls
# var_call_UVZR7709LPZF23DgUxE2dmxz and var_call_a7dKfCyZqiBGcFKsysbkg3Rk are provided in storage

def load_json_var(v):
    if isinstance(v, str):
        # assume it's a file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

business_records = load_json_var(var_call_UVZR7709LPZF23DgUxE2dmxz)
review_records = load_json_var(var_call_a7dKfCyZqiBGcFKsysbkg3Rk)

# Create DataFrames
bdf = pd.DataFrame(business_records)
rdf = pd.DataFrame(review_records)

# Normalize reviews: ratings to numeric
if 'rating' in rdf.columns:
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
else:
    rdf['rating'] = pd.NA

# Helper to extract state from description
state_re = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    try:
        if not desc or not isinstance(desc, str):
            return None
        m = state_re.search(desc)
        if m:
            return m.group(1)
    except Exception:
        return None
    return None

# Helper to determine if business offers WiFi

def has_wifi(attrs):
    if not attrs or attrs == 'None':
        return False
    # attrs may be a dict or string representation
    if isinstance(attrs, dict):
        # Keys may include 'WiFi' or 'wifi'
        for k in attrs.keys():
            if k.lower() == 'wifi':
                val = attrs[k]
                if val is None:
                    return False
                sval = str(val).lower()
                if 'no' in sval:
                    return False
                return True
        return False
    else:
        # string representation, check for wifi patterns
        s = str(attrs).lower()
        if 'wifi' in s and 'no' not in s:
            return True
        return False

# Build processed business dataframe
bdf['state'] = bdf['description'].apply(extract_state)
if 'attributes' in bdf.columns:
    bdf['has_wifi'] = bdf['attributes'].apply(has_wifi)
else:
    bdf['has_wifi'] = False

# Filter to businesses in US states (2-letter codes) and with wifi
wifi_biz = bdf[bdf['has_wifi'] & bdf['state'].notna()].copy()

# Count businesses offering wifi per state (unique business_id)
state_counts = wifi_biz.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

# Map business_id to business_ref for joining with reviews
wifi_biz['business_ref'] = wifi_biz['business_id'].str.replace('businessid_', 'businessref_')

# Filter reviews for wifi businesses
wifi_review = rdf[rdf['business_ref'].isin(wifi_biz['business_ref'])].copy()

# Merge to get state for each review
merged = wifi_review.merge(wifi_biz[['business_ref','state']], on='business_ref', how='left')

# Compute average rating per state (across all reviews for wifi businesses)
avg_rating = merged.groupby('state')['rating'].mean().reset_index(name='average_rating')

# Combine counts and avg
summary = state_counts.merge(avg_rating, on='state', how='left')

# If some wifi businesses have no reviews, their average_rating will be NaN; that's fine

# Find state with max wifi_business_count
if not summary.empty:
    max_row = summary.sort_values(['wifi_business_count','average_rating'], ascending=[False, False]).iloc[0]
    result = {
        'state': max_row['state'],
        'wifi_business_count': int(max_row['wifi_business_count']),
        'average_rating': None if pd.isna(max_row['average_rating']) else float(round(max_row['average_rating'], 3))
    }
else:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TXbD5C2P6pEcS4aWn6Z30ewF': ['checkin', 'business'], 'var_call_UVZR7709LPZF23DgUxE2dmxz': 'file_storage/call_UVZR7709LPZF23DgUxE2dmxz.json', 'var_call_a7dKfCyZqiBGcFKsysbkg3Rk': 'file_storage/call_a7dKfCyZqiBGcFKsysbkg3Rk.json'}

exec(code, env_args)
