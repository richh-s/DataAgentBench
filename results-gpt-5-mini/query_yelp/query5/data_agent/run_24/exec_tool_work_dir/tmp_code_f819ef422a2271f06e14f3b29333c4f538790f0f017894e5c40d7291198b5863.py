code = """import json
import pandas as pd
import re

with open(var_call_m68jbtLvI9WvM3SmwBlWUERr, 'r') as f:
    businesses = json.load(f)
with open(var_call_fVDfhyKnkuzxg50suzqi10DB, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# get wifi attribute

def get_wifi(a):
    if isinstance(a, dict):
        return a.get('WiFi')
    return a

def offers_wifi(val):
    if val is None:
        return False
    s = str(val).lower()
    if 'no' in s:
        return False
    if any(k in s for k in ['free','paid','yes','unlimited','wifi']):
        return True
    return False

# robust state extraction using multiple patterns
US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # try multiple regexes
    patterns = [
        r"in [^,]+,\s*([A-Za-z]{2})\b",
        r",\s*([A-Za-z]{2})[\.,]",
        r",\s*([A-Za-z]{2})\s",
        r"\b([A-Za-z]{2})\b,\s*this",
        r"\b([A-Za-z]{2})\b\s+this",
    ]
    for p in patterns:
        m = re.search(p, desc)
        if m:
            st = m.group(1).upper()
            if st in US_STATES:
                return st
    # fallback: look for any two-letter uppercase token in desc
    tokens = re.findall(r"\b([A-Z]{2})\b", desc)
    for t in tokens:
        if t in US_STATES:
            return t
    return None

# apply

df_b['wifi_attr'] = df_b['attributes'].apply(get_wifi)
df_b['offers_wifi'] = df_b['wifi_attr'].apply(offers_wifi)
df_b['state'] = df_b['description'].apply(extract_state)

# filter wifi businesses in US states
wifi_biz = df_b[(df_b['offers_wifi']) & (df_b['state'].notnull())].copy()

# map business_id to business_ref
wifi_biz['business_ref'] = wifi_biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# prepare reviews
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.to_numeric(df_r.get('stars', []), errors='coerce')

# merge
merged = pd.merge(df_r, wifi_biz[['business_ref','business_id','state']], left_on='business_ref', right_on='business_ref', how='inner')

# counts
state_counts = wifi_biz.groupby('state')['business_id'].nunique()

if state_counts.empty:
    result = {"state": None, "wifi_business_count": 0, "average_rating": None}
else:
    max_count = int(state_counts.max())
    top_states = state_counts[state_counts == state_counts.max()].index.tolist()
    top_state = sorted(top_states)[0]
    top_reviews = merged[merged['state'] == top_state]
    if not top_reviews.empty:
        avg_rating = round(float(top_reviews['rating'].mean()), 2)
    else:
        avg_rating = None
    result = {"state": top_state, "wifi_business_count": max_count, "average_rating": avg_rating}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_m68jbtLvI9WvM3SmwBlWUERr': 'file_storage/call_m68jbtLvI9WvM3SmwBlWUERr.json', 'var_call_fVDfhyKnkuzxg50suzqi10DB': 'file_storage/call_fVDfhyKnkuzxg50suzqi10DB.json', 'var_call_AWI9RmHFlqMTNIVAjP60tCps': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_51hd07zFeCaSF0tNTAAqBGBW': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_k3CMmxNhl4ezuT4CvxbSEa4O': 'file_storage/call_k3CMmxNhl4ezuT4CvxbSEa4O.json', 'var_call_sxonNH5V3f4iX9WCqTkvRGs0': {'rows': [{'business_id': 'businessid_49', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_92', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_64', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_54', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_91', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_93', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_24', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_26', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_89', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_32', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_97', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_27', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_67', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_7', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_51', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_5', 'wifi_attr_str': "'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_6', 'wifi_attr_str': "'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_87', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_55', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_96', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_77', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_86', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_40', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_44', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_43', 'wifi_attr_str': "'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_9', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_20', 'wifi_attr_str': "'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_94', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_85', 'wifi_attr_str': "'no'", 'offers_wifi': False, 'state': None}, {'business_id': 'businessid_25', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_82', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_12', 'wifi_attr_str': "u'paid'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_16', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_46', 'wifi_attr_str': "u'free'", 'offers_wifi': True, 'state': None}, {'business_id': 'businessid_36', 'wifi_attr_str': "u'no'", 'offers_wifi': False, 'state': None}], 'total': 35, 'wifi_offered_count': 22}}

exec(code, env_args)
