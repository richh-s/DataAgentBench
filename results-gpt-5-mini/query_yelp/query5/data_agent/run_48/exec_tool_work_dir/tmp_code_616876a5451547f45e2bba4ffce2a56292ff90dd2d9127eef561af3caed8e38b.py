code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
business_file = var_call_dfaaQ6ETCmxISzGElNjMUdBB
reviews_file = var_call_pQm8djdkb0TBExSSZGoM746i

with open(business_file, 'r') as f:
    businesses = json.load(f)

with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrames
b_df = pd.DataFrame(businesses)
r_df = pd.DataFrame(reviews)

# Normalize reviews rating to numeric
r_df['rating'] = pd.to_numeric(r_df['rating'], errors='coerce')

# Helper functions
def extract_state(description):
    if not isinstance(description, str):
        return None
    # Try to find pattern like ', XX,' where XX is two uppercase letters
    m = re.search(r",\s*([A-Z]{2})\s*,", description)
    if m:
        return m.group(1)
    # fallback: 'in City, ST' pattern
    m = re.search(r"in [^,]+,\s*([A-Z]{2})\b", description)
    if m:
        return m.group(1)
    return None


def wifi_offered(attributes):
    # attributes may be None, string 'None', or dict
    if attributes is None:
        return False
    if isinstance(attributes, str):
        if attributes.strip().lower() == 'none':
            return False
        # sometimes the entire attributes stored as string representation of dict
        try:
            # attempt to find WiFi key using regex
            m = re.search(r"WiFi\s*[:=]\s*([^,}\n]+)", attributes)
            if m:
                val = m.group(1)
            else:
                # try to find "WiFi": "value"
                m = re.search(r"WiFi""?\s*[:=]\s*['\"]?([^'\",}]+)", attributes)
                if m:
                    val = m.group(1)
                else:
                    return False
        except Exception:
            return False
    elif isinstance(attributes, dict):
        val = attributes.get('WiFi') or attributes.get('wifi')
        if val is None:
            return False
    else:
        return False

    if val is None:
        return False
    if not isinstance(val, str):
        val = str(val)
    v = val.lower()
    # remove u' quotes and surrounding quotes and spaces
    v = re.sub(r"[^a-z0-9]", '', v)
    if v == '':
        return False
    # If contains 'no' exactly => False
    if 'no' == v or v.startswith('no') or 'no' in v and v not in ('free', 'paid', 'yes') and not v.startswith('fre'):
        # conservative: if contains 'no' and not clearly 'free' etc
        # but handle common values 'free' and 'paid'
        if 'free' in v or 'paid' in v or 'yes' in v:
            return True
        return False
    # otherwise, consider it offered
    return True

# Build DataFrame with business_id, state, wifi
b_df['state'] = b_df['description'].apply(extract_state)
# Some attributes may be actual dict or strings
b_df['wifi'] = b_df['attributes'].apply(wifi_offered)

# Filter businesses that offer wifi and have a U.S. state
wifi_biz = b_df[(b_df['wifi'] == True) & (b_df['state'].notna())].copy()

# Count per state
state_counts = wifi_biz['state'].value_counts()
if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top_state = state_counts.idxmax()
    top_count = int(state_counts.max())
    # Map business_id to business_ref
    def to_ref(bid):
        if isinstance(bid, str) and bid.startswith('businessid_'):
            return 'businessref_' + bid.split('_',1)[1]
        return bid
    wifi_biz['business_ref'] = wifi_biz['business_id'].apply(to_ref)
    # Get reviews for these business_refs
    target_refs = set(wifi_biz['business_ref'].tolist())
    target_reviews = r_df[r_df['business_ref'].isin(target_refs)].copy()
    if target_reviews.empty:
        avg_rating = None
    else:
        avg_rating = float(target_reviews['rating'].mean())
    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uBUX7xwocOEhQftURPAM6eSb': ['checkin', 'business'], 'var_call_uebD51MzhowRRBqWtQFiQWb6': ['review', 'tip', 'user'], 'var_call_dfaaQ6ETCmxISzGElNjMUdBB': 'file_storage/call_dfaaQ6ETCmxISzGElNjMUdBB.json', 'var_call_pQm8djdkb0TBExSSZGoM746i': 'file_storage/call_pQm8djdkb0TBExSSZGoM746i.json'}

exec(code, env_args)
