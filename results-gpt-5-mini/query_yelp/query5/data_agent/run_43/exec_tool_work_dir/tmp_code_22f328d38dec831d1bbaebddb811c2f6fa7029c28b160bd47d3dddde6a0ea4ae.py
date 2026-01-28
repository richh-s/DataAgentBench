code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_i4wav3mXYs0io55KqQ4VdFcI, 'r') as f:
    businesses = json.load(f)
with open(var_call_IqSqwnwqxvDxfJ0ibxT1RqLF, 'r') as f:
    reviews = json.load(f)

# DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure columns exist
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None
if 'description' not in df_b.columns:
    df_b['description'] = ''

# Simple WiFi detection

def wifi_offered(attr):
    if not attr or attr == 'None':
        return False
    s = str(attr).lower()
    if 'wifi' not in s:
        return False
    # If contains explicit no/none/false near wifi, treat as not offered
    # check contexts
    if re.search(r"wifi\W{0,10}(no|none|false)", s) or re.search(r"(no|none|false)\W{0,10}wifi", s):
        return False
    return True

# Extract state from description

def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    # look for patterns like 'in City, ST' or ', ST,'
    m = re.search(r"in\s+[^,]+,\s*([A-Z]{2})", desc)
    if m:
        return m.group(1)
    m2 = re.search(r",\s*([A-Z]{2})[,\s]", desc)
    if m2:
        return m2.group(1)
    # also try at end like ', ST' before end
    m3 = re.search(r",\s*([A-Z]{2})\s*$", desc)
    if m3:
        return m3.group(1)
    return None

# Apply

df_b['wifi_offered'] = df_b['attributes'].apply(wifi_offered)
df_b['state'] = df_b['description'].apply(extract_state)

# Filter
df_wifi = df_b[(df_b['wifi_offered']) & (df_b['state'].notnull())].copy()

# Map business_id to business_ref

def to_businessref(bid):
    if not isinstance(bid, str):
        return None
    if bid.startswith('businessid_'):
        return 'businessref_' + bid.split('_', 1)[1]
    return 'businessref_' + bid

df_wifi['business_ref'] = df_wifi['business_id'].apply(to_businessref)

# Prepare reviews
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Counts per state
state_business_counts = df_wifi.groupby('state')['business_id'].nunique().reset_index()
state_business_counts.columns = ['state', 'business_count']

# Filter reviews to wifi businesses
wifi_refs = set(df_wifi['business_ref'].dropna().unique())
df_r_wifi = df_r[df_r['business_ref'].isin(wifi_refs)].copy()

# Map business_ref to state
ref_state = df_wifi.set_index('business_ref')['state'].to_dict()
df_r_wifi['state'] = df_r_wifi['business_ref'].map(ref_state)

# Average rating per state
state_rating = df_r_wifi.groupby('state')['rating'].mean().reset_index()
state_rating.columns = ['state', 'average_rating']

# Combine

df_state = pd.merge(state_business_counts, state_rating, on='state', how='left')
if not df_state.empty:
    df_state['average_rating'] = df_state['average_rating'].round(2)

# Top state by business_count
if df_state.empty:
    result = {'state': None, 'business_count': 0, 'average_rating': None}
else:
    df_state_sorted = df_state.sort_values(by=['business_count', 'average_rating'], ascending=[False, False])
    top = df_state_sorted.iloc[0]
    ar = None if pd.isna(top['average_rating']) else float(top['average_rating'])
    result = {'state': str(top['state']), 'business_count': int(top['business_count']), 'average_rating': ar}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_B2Hf52GyCTdOYYXvLTth8DWx': ['business', 'checkin'], 'var_call_mzh7NS609g6GTQTQMhez9ZGm': ['review', 'tip', 'user'], 'var_call_i4wav3mXYs0io55KqQ4VdFcI': 'file_storage/call_i4wav3mXYs0io55KqQ4VdFcI.json', 'var_call_IqSqwnwqxvDxfJ0ibxT1RqLF': 'file_storage/call_IqSqwnwqxvDxfJ0ibxT1RqLF.json'}

exec(code, env_args)
