code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_XGxTr6c5AlQTKrVZLLc1Xw61, 'r') as f:
    biz_data = json.load(f)
with open(var_call_ueo11QglsWkIsuDo4M1qrKp3, 'r') as f:
    rev_data = json.load(f)

biz_df = pd.DataFrame(biz_data)
# Ensure attributes and description present
biz_df['attributes'] = biz_df.get('attributes', None)
biz_df['description'] = biz_df.get('description', None)

# Function to extract wifi value
def parse_wifi(attr):
    if not attr or attr is None:
        return None
    # attr may be dict or string
    if isinstance(attr, dict):
        wifi = attr.get('WiFi') or attr.get('wifi')
    else:
        # try to find WiFi entry in string representation
        s = str(attr)
        m = re.search(r"WiFi\s*[:=]\s*([^,}\n]+)", s)
        if m:
            wifi = m.group(1)
        else:
            # try to find 'WiFi': 'u'free'' style
            m2 = re.search(r"WiFi\'\s*:\s*([^,}]+)", s)
            wifi = m2.group(1) if m2 else None
    if wifi is None:
        return None
    # normalize
    wifi_str = str(wifi)
    # remove unicode markers and quotes and non letters
    wifi_norm = re.sub("[^a-zA-Z0-9]", "", wifi_str).lower()
    return wifi_norm

biz_df['wifi_norm'] = biz_df['attributes'].apply(parse_wifi)

# Determine wifi offered: include when wifi_norm not None and not 'no' and not empty and not 'none'
biz_df['has_wifi'] = biz_df['wifi_norm'].apply(lambda x: False if x in (None, '', 'no', 'none') else True)

# Extract state from description
def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    # try common patterns
    # pattern: ', ST,' or ', ST.' or ', ST' at end
    m = re.search(r',\s*([A-Z]{2})(?:[,\.\s]|$)', desc)
    if m:
        return m.group(1)
    # pattern: ' in City, ST,'
    m2 = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m2:
        return m2.group(1)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Keep only businesses in US states (2-letter uppercase) and has_wifi True
wifi_biz = biz_df[biz_df['has_wifi'] & biz_df['state'].notnull()].copy()

# Count unique businesses by state
state_counts = wifi_biz.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top = state_counts.sort_values('wifi_business_count', ascending=False).iloc[0]
    top_state = top['state']
    top_count = int(top['wifi_business_count'])

    # Load reviews
    rev_df = pd.DataFrame(rev_data)
    # Ensure rating numeric
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

    # Map business_id to business_ref format
    wifi_biz['business_ref'] = wifi_biz['business_id'].astype(str).str.replace('businessid_', 'businessref_')

    # Reviews for businesses in top_state
    top_refs = set(wifi_biz[wifi_biz['state'] == top_state]['business_ref'].unique())
    rev_top = rev_df[rev_df['business_ref'].isin(top_refs)].copy()

    if rev_top.empty:
        avg_rating = None
    else:
        avg_rating = float(rev_top['rating'].mean())

    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pBdzrYsd4HKArKkzG6VdAe1S': ['checkin', 'business'], 'var_call_BDsqebDO9LTX5MKNwA0JzAUC': ['review', 'tip', 'user'], 'var_call_XGxTr6c5AlQTKrVZLLc1Xw61': 'file_storage/call_XGxTr6c5AlQTKrVZLLc1Xw61.json', 'var_call_ueo11QglsWkIsuDo4M1qrKp3': 'file_storage/call_ueo11QglsWkIsuDo4M1qrKp3.json'}

exec(code, env_args)
