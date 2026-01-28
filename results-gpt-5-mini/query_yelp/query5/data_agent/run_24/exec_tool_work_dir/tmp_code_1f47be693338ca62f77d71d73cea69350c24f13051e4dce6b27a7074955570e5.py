code = """import json
import pandas as pd
import re

with open(var_call_m68jbtLvI9WvM3SmwBlWUERr, 'r') as f:
    businesses = json.load(f)
with open(var_call_fVDfhyKnkuzxg50suzqi10DB, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# helper to extract wifi attribute value
def get_wifi(a):
    if isinstance(a, dict):
        return a.get('WiFi')
    return a

# helper to determine if wifi is offered
def offers_wifi_val(val):
    if val is None:
        return False
    s = str(val).lower()
    # If explicitly no -> False
    # check common patterns 'no' possibly with quotes
    if re.search(r"\bno\b", s):
        return False
    # If contains indicators of offered wifi
    if any(k in s for k in ['free', 'paid', 'yes', 'unlimited', 'wifi']):
        return True
    # otherwise False
    return False

US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

# extract state from description
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # common pattern: 'in City, ST,' or 'in City, ST.'
    m = re.search(r"in [^,]+,\s*([A-Za-z]{2})\b", desc)
    if m:
        st = m.group(1).upper()
        if st in US_STATES:
            return st
    # pattern: ', ST,' or ', ST.'
    m2 = re.search(r",\s*([A-Za-z]{2})[\.,]\b", desc)
    if m2:
        st = m2.group(1).upper()
        if st in US_STATES:
            return st
    # pattern: ends with 'City, ST' without trailing punctuation
    m3 = re.search(r",\s*([A-Za-z]{2})\s*$", desc)
    if m3:
        st = m3.group(1).upper()
        if st in US_STATES:
            return st
    return None

# apply

df_b['wifi_attr'] = df_b['attributes'].apply(get_wifi)
df_b['offers_wifi'] = df_b['wifi_attr'].apply(offers_wifi_val)
df_b['state'] = df_b['description'].apply(extract_state)

# filter to businesses offering wifi and with US state
wifi_biz = df_b[(df_b['offers_wifi']) & (df_b['state'].notnull())].copy()

# map to business_ref
wifi_biz['business_ref'] = wifi_biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# prepare reviews
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.to_numeric(df_r.get('stars', []), errors='coerce')

# merge reviews with wifi businesses
merged = pd.merge(df_r, wifi_biz[['business_ref','business_id','state']], left_on='business_ref', right_on='business_ref', how='inner')

# count unique wifi businesses per state
state_counts = wifi_biz.groupby('state')['business_id'].nunique()

if state_counts.empty:
    result = {"state": None, "wifi_business_count": 0, "average_rating": None}
else:
    max_count = int(state_counts.max())
    top_states = state_counts[state_counts == state_counts.max()].index.tolist()
    # choose alphabetically first if tie
    top_state = sorted(top_states)[0]
    # compute average rating for reviews of businesses in that state
    top_reviews = merged[merged['state'] == top_state]
    if not top_reviews.empty:
        avg_rating = round(float(top_reviews['rating'].mean()), 2)
    else:
        avg_rating = None
    result = {"state": top_state, "wifi_business_count": max_count, "average_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_m68jbtLvI9WvM3SmwBlWUERr': 'file_storage/call_m68jbtLvI9WvM3SmwBlWUERr.json', 'var_call_fVDfhyKnkuzxg50suzqi10DB': 'file_storage/call_fVDfhyKnkuzxg50suzqi10DB.json', 'var_call_AWI9RmHFlqMTNIVAjP60tCps': {'state': None, 'wifi_business_count': 0, 'average_rating': None}}

exec(code, env_args)
