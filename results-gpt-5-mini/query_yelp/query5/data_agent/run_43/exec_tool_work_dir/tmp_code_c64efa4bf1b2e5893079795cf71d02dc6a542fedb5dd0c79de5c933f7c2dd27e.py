code = """import json
import pandas as pd
import re

# Load the query results from storage paths
with open(var_call_i4wav3mXYs0io55KqQ4VdFcI, 'r') as f:
    businesses = json.load(f)
with open(var_call_IqSqwnwqxvDxfJ0ibxT1RqLF, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None
if 'description' not in df_b.columns:
    df_b['description'] = ''

# Function to determine if WiFi is offered
def wifi_offered(attr):
    if not attr or attr == 'None':
        return False
    # attr could be dict or string representation
    if isinstance(attr, dict):
        val = attr.get('WiFi')
    else:
        # try to parse if string looks like a dict
        try:
            # not safe to eval; just search for WiFi key
            m = re.search(r"\'WiFi\'\s*:\s*([^,}]+)", str(attr))
            if m:
                val = m.group(1)
            else:
                # fallback: if 'WiFi' not present
                val = None
        except Exception:
            val = None
    if val is None:
        return False
    s = str(val).lower()
    # remove leading u' and surrounding quotes
    s = re.sub(r"^u?['\"]|['\"]$", '', s)
    s = s.strip()
    # Consider wifi offered unless it explicitly says no/none/false
    if re.search(r"\b(no|none|false)\b", s):
        return False
    # If empty string, treat as not offered
    if s == '':
        return False
    return True

# Extract state from description
def extract_state(desc):
    if not desc:
        return None
    # Try pattern: in City, ST,
    m = re.search(r"in\s+[^,]+,\s*([A-Z]{2})", desc)
    if m:
        return m.group(1)
    # Fallback: find any , ST,
    m2 = re.search(r",\s*([A-Z]{2})[,\s]", desc)
    if m2:
        return m2.group(1)
    return None

# Apply functions
df_b['wifi_offered'] = df_b['attributes'].apply(wifi_offered)
# Some attributes may be nested strings; also ensure proper types

df_b['state'] = df_b['description'].apply(extract_state)
# Filter businesses that offer wifi and have a state
df_wifi = df_b[(df_b['wifi_offered']) & (df_b['state'].notnull())].copy()

# Map business_id to business_ref
def to_businessref(bid):
    if not isinstance(bid, str):
        return None
    if bid.startswith('businessid_'):
        return 'businessref_' + bid.split('_', 1)[1]
    # fallback
    return 'businessref_' + bid

df_wifi['business_ref'] = df_wifi['business_id'].apply(to_businessref)

# Load reviews
df_r = pd.DataFrame(reviews)
# Ensure rating numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Compute per-state business counts
state_business_counts = df_wifi.groupby('state')['business_id'].nunique().reset_index()
state_business_counts.columns = ['state', 'business_count']

# Compute average rating for reviews of WiFi businesses per state
# Filter reviews to those in df_wifi
wifi_refs = set(df_wifi['business_ref'].dropna().unique())
df_r_wifi = df_r[df_r['business_ref'].isin(wifi_refs)].copy()

# Merge reviews with business state
# Need mapping from business_ref to state
ref_state = df_wifi.set_index('business_ref')['state'].to_dict()
df_r_wifi['state'] = df_r_wifi['business_ref'].map(ref_state)

# Now aggregate average rating per state
state_rating = df_r_wifi.groupby('state')['rating'].mean().reset_index()
state_rating.columns = ['state', 'average_rating']

# Combine counts and ratings
df_state = pd.merge(state_business_counts, state_rating, on='state', how='left')
# If some states have no reviews, average_rating will be NaN; keep as None

df_state['average_rating'] = df_state['average_rating'].round(2)

# Find the state with highest number of businesses offering WiFi
if df_state.empty:
    result = {'state': None, 'business_count': 0, 'average_rating': None}
else:
    df_state_sorted = df_state.sort_values(by=['business_count', 'average_rating'], ascending=[False, False])
    top = df_state_sorted.iloc[0]
    ar = None if pd.isna(top['average_rating']) else float(top['average_rating'])
    result = {'state': str(top['state']), 'business_count': int(top['business_count']), 'average_rating': ar}

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_B2Hf52GyCTdOYYXvLTth8DWx': ['business', 'checkin'], 'var_call_mzh7NS609g6GTQTQMhez9ZGm': ['review', 'tip', 'user'], 'var_call_i4wav3mXYs0io55KqQ4VdFcI': 'file_storage/call_i4wav3mXYs0io55KqQ4VdFcI.json', 'var_call_IqSqwnwqxvDxfJ0ibxT1RqLF': 'file_storage/call_IqSqwnwqxvDxfJ0ibxT1RqLF.json'}

exec(code, env_args)
