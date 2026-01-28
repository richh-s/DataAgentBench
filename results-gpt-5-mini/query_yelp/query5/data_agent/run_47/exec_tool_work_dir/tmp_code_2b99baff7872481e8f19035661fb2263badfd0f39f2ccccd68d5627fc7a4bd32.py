code = """import json
import pandas as pd

# Load wifi docs and reviews from storage
with open(var_call_xfYZPHwEXj2HeWIXEkVA3mkT, 'r') as f:
    wifi_docs = json.load(f)
with open(var_call_opnFEcPgJzaAR3lRvcVMz2DI, 'r') as f:
    reviews = json.load(f)

# US state codes set (50 states + DC)
us_states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

# helper to parse wifi value
def offers_wifi_val(val):
    if val is None:
        return False
    s = str(val).lower()
    # treat empty as False
    if s.strip() == '':
        return False
    # explicit no/none -> False
    if any(x in s for x in ['no', "u'no'", "'no'", 'none', "u'none'", "'none'"]):
        return False
    # explicit yes/free/paid/true -> True
    if any(x in s for x in ['free','paid','yes','true', "u'free'", "'free'", "u'yes'", "'yes'", 'paid']):
        return True
    # if 'wifi' mentioned with unknown value, assume True
    if 'wifi' in s or 'wi-fi' in s:
        return True
    return False

# extract state from description
import re
state_regex = re.compile(r',\s*([A-Z]{2})(?:\b|,|$)')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_regex.search(desc)
    if m:
        code = m.group(1)
        if code in us_states:
            return code
        else:
            return code
    return None

rows = []
for d in wifi_docs:
    bid = d.get('business_id')
    attr = d.get('attributes')
    wifi_val = None
    if isinstance(attr, dict):
        wifi_val = attr.get('WiFi') if 'WiFi' in attr else None
        # Also check alternate keys
        if wifi_val is None:
            for k in attr.keys():
                if 'wifi' in str(k).lower() or 'wi-fi' in str(k).lower():
                    wifi_val = attr.get(k)
                    break
    else:
        # attributes may be string: try to find wifi substring
        if isinstance(attr, str) and ('wifi' in attr.lower() or 'wi-fi' in attr.lower()):
            wifi_val = attr
    desc = d.get('description')
    state = extract_state(desc)
    offers = offers_wifi_val(wifi_val)
    rows.append({'business_id': bid, 'state': state, 'offers_wifi': offers, 'wifi_val': wifi_val})

df = pd.DataFrame(rows)
# Consider only those that offer wifi and are in US states
df_us = df[df['offers_wifi'] & df['state'].isin(us_states)].copy()

# Count unique businesses per state
state_counts = df_us.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count').sort_values('wifi_business_count', ascending=False)

if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top = state_counts.iloc[0]
    top_state = top['state']
    top_count = int(top['wifi_business_count'])

    # prepare reviews df
    df_r = pd.DataFrame(reviews)
    if 'rating' in df_r.columns:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = pd.NA
    if 'business_ref' in df_r.columns:
        df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_')
    else:
        df_r['business_id'] = None

    wifi_bids_top = set(df_us[df_us['state'] == top_state]['business_id'].unique())
    df_top_reviews = df_r[df_r['business_id'].isin(wifi_bids_top)].copy()
    if df_top_reviews.empty or df_top_reviews['rating'].dropna().empty:
        avg_rating = None
    else:
        avg_rating = float(df_top_reviews['rating'].mean())
    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 3)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dN2JuewUADycIK9fd1n5g06L': ['business', 'checkin'], 'var_call_m3teTuDAOvNmpwr4YK3rMjWx': ['review', 'tip', 'user'], 'var_call_7dr5SRMBkApBL3tOjutkL1x7': 'file_storage/call_7dr5SRMBkApBL3tOjutkL1x7.json', 'var_call_opnFEcPgJzaAR3lRvcVMz2DI': 'file_storage/call_opnFEcPgJzaAR3lRvcVMz2DI.json', 'var_call_SEhndpyOCax4bJVGXTt6Q05b': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_Bi4RcdoSHpu6OvPMErSxQt9F': {'state': 'PA', 'wifi_business_count': 8, 'average_rating': 3.484}, 'var_call_xfYZPHwEXj2HeWIXEkVA3mkT': 'file_storage/call_xfYZPHwEXj2HeWIXEkVA3mkT.json', 'var_call_Wv75UuGWM0Dp8qWQZWmXOksY': [{'state': 'PA', 'cnt': 12}, {'state': 'FL', 'cnt': 5}, {'state': 'MO', 'cnt': 4}, {'state': 'IN', 'cnt': 4}, {'state': 'LA', 'cnt': 2}, {'state': 'AB', 'cnt': 2}, {'state': 'NV', 'cnt': 2}, {'state': 'ID', 'cnt': 2}, {'state': 'CA', 'cnt': 1}, {'state': 'IL', 'cnt': 1}]}

exec(code, env_args)
