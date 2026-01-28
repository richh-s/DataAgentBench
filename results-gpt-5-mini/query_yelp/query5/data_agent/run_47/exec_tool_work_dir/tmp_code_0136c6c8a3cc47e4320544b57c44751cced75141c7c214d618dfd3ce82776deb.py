code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_7dr5SRMBkApBL3tOjutkL1x7, 'r') as f:
    businesses = json.load(f)
with open(var_call_opnFEcPgJzaAR3lRvcVMz2DI, 'r') as f:
    reviews = json.load(f)

# Create DataFrame for businesses
df_b = pd.DataFrame(businesses)
# Ensure columns exist
if 'business_id' not in df_b.columns:
    df_b['business_id'] = df_b.get('business_id', None)

# Function to determine if business offers WiFi
def offers_wifi(attr):
    if not isinstance(attr, dict):
        return False
    # possible keys
    keys = ['WiFi', 'Wi-Fi', 'wifi']
    for k in keys:
        if k in attr and attr[k] is not None:
            val = str(attr[k]).lower()
            # consider offering wifi unless explicitly 'no' or 'none'
            if 'no' in val or 'none' in val:
                return False
            # if contains free/paid/yes/true
            if any(x in val for x in ['free','paid','yes','true']):
                return True
            # fallback: if value non-empty and not 'false'
            if val.strip() not in ['', "u'no'", "false", "u'none'", "none"]:
                return True
    return False

# Extract state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Look for pattern like ', PA' or ', PA,' etc.
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

# Apply
df_b['has_wifi'] = df_b['attributes'].apply(offers_wifi)
df_b['state'] = df_b['description'].apply(extract_state)

# Filter businesses with wifi and with a state
df_wifi = df_b[df_b['has_wifi'] & df_b['state'].notnull()].copy()

# Count businesses per state
state_counts = df_wifi.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    # find state with max count
    top = state_counts.sort_values(['wifi_business_count','state'], ascending=[False, True]).iloc[0]
    top_state = top['state']
    top_count = int(top['wifi_business_count'])

    # Prepare reviews DataFrame
    df_r = pd.DataFrame(reviews)
    # Convert rating to numeric
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    # Map review business_ref to business_id by replacing prefix
    df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_')

    # Get list of wifi business ids in top state
    wifi_bids_top = set(df_wifi[df_wifi['state'] == top_state]['business_id'].unique())

    # Filter reviews for those business ids
    df_top_reviews = df_r[df_r['business_id'].isin(wifi_bids_top)].copy()

    if df_top_reviews.empty:
        avg_rating = None
    else:
        avg_rating = float(df_top_reviews['rating'].mean())

    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 3)}

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dN2JuewUADycIK9fd1n5g06L': ['business', 'checkin'], 'var_call_m3teTuDAOvNmpwr4YK3rMjWx': ['review', 'tip', 'user'], 'var_call_7dr5SRMBkApBL3tOjutkL1x7': 'file_storage/call_7dr5SRMBkApBL3tOjutkL1x7.json', 'var_call_opnFEcPgJzaAR3lRvcVMz2DI': 'file_storage/call_opnFEcPgJzaAR3lRvcVMz2DI.json'}

exec(code, env_args)
