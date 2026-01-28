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
    # Try to find pattern like ', XX,' or 'in City, ST'
    m = re.search(r",\s*([A-Z]{2})\b", description)
    if m:
        return m.group(1)
    m = re.search(r"in [^,]+,\s*([A-Z]{2})\b", description)
    if m:
        return m.group(1)
    return None


def wifi_offered(attributes):
    if attributes is None:
        return False
    s = str(attributes)
    s_low = s.lower()
    if 'wifi' not in s_low:
        return False
    # try to capture value after wifi
    m = re.search(r"wifi[^a-z0-9]*u?[\"']?([a-z]+)", s_low)
    if m:
        val = m.group(1)
        if val in ('no', 'none', 'false', 'n'):
            return False
        return True
    # if wifi present but value not found, assume offered
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
    target_refs = set(wifi_biz[wifi_biz['state']==top_state]['business_ref'].tolist())
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
