code = """import json
import pandas as pd
import re

# Load data from storage variables
# var_call_m68jbtLvI9WvM3SmwBlWUERr and var_call_fVDfhyKnkuzxg50suzqi10DB are available

with open(var_call_m68jbtLvI9WvM3SmwBlWUERr, 'r') as f:
    businesses = json.load(f)
with open(var_call_fVDfhyKnkuzxg50suzqi10DB, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# normalize wifi attribute to string

def offers_wifi(attr):
    if not isinstance(attr, str):
        return False
    s = attr.lower()
    # treat any explicit 'no' as no wifi, otherwise treat as offering wifi
    if "no" in s:
        return False
    # If contains free, paid, yes, or similar => wifi offered
    if any(k in s for k in ["free", "paid", "yes", "unlimited"]):
        return True
    # fallback: if it's some other non-empty string, assume wifi offered
    return len(s.strip()) > 0

# extract US state from description using regex
US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # try pattern: in City, ST,
    m = re.search(r"in [^,]+,\s*([A-Z]{2})\b", desc)
    if m:
        st = m.group(1)
        if st in US_STATES:
            return st
        else:
            return None
    # fallback: look for ', ST,' pattern
    m = re.search(r",\s*([A-Z]{2})\b", desc)
    if m:
        st = m.group(1)
        if st in US_STATES:
            return st
    return None

# Apply

df_b['wifi_attr'] = df_b['attributes'].apply(lambda a: a.get('WiFi') if isinstance(a, dict) else (a if isinstance(a, str) else None))
df_b['offers_wifi'] = df_b['wifi_attr'].apply(lambda x: offers_wifi(x) if x is not None else False)
df_b['state'] = df_b['description'].apply(extract_state)

# Filter businesses that offer wifi and are in US states
wifi_biz = df_b[(df_b['offers_wifi']) & (df_b['state'].notnull())].copy()

# Map business_id to business_ref
wifi_biz['business_ref'] = wifi_biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Prepare reviews df: convert rating to numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.to_numeric(df_r.get('stars', []), errors='coerce')

# Merge reviews with wifi businesses on business_ref
merged = pd.merge(df_r, wifi_biz[['business_ref','business_id','state']], left_on='business_ref', right_on='business_ref', how='inner')

# Count unique wifi businesses per state
state_counts = wifi_biz.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

if state_counts.empty:
    result = {"state": None, "wifi_business_count": 0, "average_rating": None}
else:
    # find state with highest count
    state_counts = state_counts.sort_values(['wifi_business_count','state'], ascending=[False,True])
    top_state = state_counts.iloc[0]['state']
    top_count = int(state_counts.iloc[0]['wifi_business_count'])
    # compute average rating for reviews of businesses in that state
    top_reviews = merged[merged['state'] == top_state]
    if not top_reviews.empty:
        avg_rating = float(top_reviews['rating'].mean())
        avg_rating = round(avg_rating, 2)
    else:
        avg_rating = None
    result = {"state": top_state, "wifi_business_count": top_count, "average_rating": avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_m68jbtLvI9WvM3SmwBlWUERr': 'file_storage/call_m68jbtLvI9WvM3SmwBlWUERr.json', 'var_call_fVDfhyKnkuzxg50suzqi10DB': 'file_storage/call_fVDfhyKnkuzxg50suzqi10DB.json'}

exec(code, env_args)
