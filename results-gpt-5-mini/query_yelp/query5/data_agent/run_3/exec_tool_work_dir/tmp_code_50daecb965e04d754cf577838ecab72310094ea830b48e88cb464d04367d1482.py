code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_C8nEh286Vq6d6XQ5y6YD5KYW, 'r') as f:
    businesses = json.load(f)
with open(var_call_AMha1bjdNtmr27cv7nl3OWGb, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrames
df_b = pd.DataFrame(businesses)
# Some entries might have attributes as None; ensure column exists
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

# Filter businesses that have a WiFi attribute and whose value does NOT contain 'no'
def offers_wifi(val):
    if val is None:
        return False
    s = str(val).lower()
    # treat anything containing 'no' as not offering wifi; everything else as offering
    if 'no' in s:
        return False
    return True

mask = df_b['attributes'].apply(lambda a: isinstance(a, dict) and 'WiFi' in a and offers_wifi(a.get('WiFi')))
df_wifi = df_b[mask].copy()

# Extract state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # try pattern: 'in City, ST' or look for ', ST,'
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    m2 = re.search(r',\s*([A-Z]{2})[,\s]', desc)
    if m2:
        return m2.group(1)
    return None

df_wifi['state'] = df_wifi['description'].apply(extract_state)
# drop rows without state
df_wifi = df_wifi[df_wifi['state'].notnull()].copy()

# Map business_id to business_ref
df_wifi['business_ref'] = df_wifi['business_id'].str.replace('businessid_', 'businessref_')

# Prepare reviews dataframe
df_r = pd.DataFrame(reviews)
# ensure rating numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Join reviews for businesses that offer wifi
wifi_refs = set(df_wifi['business_ref'].tolist())
df_r_wifi = df_r[df_r['business_ref'].isin(wifi_refs)].copy()

# Merge review rows with business state
df_merge = df_r_wifi.merge(df_wifi[['business_ref','business_id','state']], on='business_ref', how='left')

# Compute counts of businesses with wifi per state (unique businesses)
state_counts = df_wifi.groupby('state')['business_id'].nunique().to_dict()

# Compute average rating per state across all reviews of wifi businesses
state_avg_rating = df_merge.groupby('state')['rating'].mean().to_dict()

# Determine state with highest number of wifi-offering businesses
if not state_counts:
    result = {'state': None, 'business_count': 0, 'average_rating': None}
else:
    # find max count; if ties, pick the one with highest average rating among them
    max_count = max(state_counts.values())
    candidates = [s for s,c in state_counts.items() if c==max_count]
    if len(candidates)==1:
        chosen = candidates[0]
    else:
        # choose candidate with highest avg rating (NaN treated as -inf)
        best = None
        best_rating = float('-inf')
        for s in candidates:
            r = state_avg_rating.get(s)
            if r is None or (isinstance(r,float) and pd.isna(r)):
                continue
            if r>best_rating:
                best_rating = r
                best = s
        chosen = best if best is not None else candidates[0]
    avg = state_avg_rating.get(chosen)
    # Round avg to 3 decimals if not None
    if avg is None or (isinstance(avg,float) and pd.isna(avg)):
        avg_val = None
    else:
        avg_val = round(float(avg),3)
    result = {'state': chosen, 'business_count': int(max_count), 'average_rating': avg_val}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Fb7YxfcNUpXWLBXphdjT60Z5': ['business', 'checkin'], 'var_call_vFVBqroOxKnmGaHZ3BaMjOE2': ['review', 'tip', 'user'], 'var_call_C8nEh286Vq6d6XQ5y6YD5KYW': 'file_storage/call_C8nEh286Vq6d6XQ5y6YD5KYW.json', 'var_call_AMha1bjdNtmr27cv7nl3OWGb': 'file_storage/call_AMha1bjdNtmr27cv7nl3OWGb.json'}

exec(code, env_args)
