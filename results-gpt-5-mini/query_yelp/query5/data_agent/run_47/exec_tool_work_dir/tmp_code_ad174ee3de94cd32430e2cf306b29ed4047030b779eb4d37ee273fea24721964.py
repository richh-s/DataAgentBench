code = """import json
import pandas as pd
import re

with open(var_call_7dr5SRMBkApBL3tOjutkL1x7, 'r') as f:
    businesses = json.load(f)
with open(var_call_opnFEcPgJzaAR3lRvcVMz2DI, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)

def offers_wifi(attr):
    if attr is None:
        return False
    # if it's a dict-like
    if isinstance(attr, dict):
        for k, v in attr.items():
            try:
                key = str(k).lower()
            except:
                continue
            if 'wifi' in key or 'wi-fi' in key:
                val = '' if v is None else str(v).lower()
                if any(x in val for x in ['no', "u'no'", 'none']):
                    return False
                if any(x in val for x in ['free', 'paid', 'yes', 'true', "u'free'", "u'paid'", "u'yes'", 'u"free"']):
                    return True
                # otherwise if non-empty and not false
                if val.strip() not in ['', 'false']:
                    return True
                return False
        return False
    # if it's a string representation
    if isinstance(attr, str):
        s = attr.lower()
        if 'wifi' in s or 'wi-fi' in s:
            # look for no/none
            if any(x in s for x in ['no', "u'no'", 'none']):
                return False
            if any(x in s for x in ['free', 'paid', 'yes', 'true', "u'free'", "u'paid'", "u'yes'"]):
                return True
            # otherwise assume true if wifi mentioned
            return True
        return False
    return False

# extract state
state_regex = re.compile(r',\s*([A-Z]{2})(?:\b|,|$)')
alt_regex = re.compile(r'in\s+[^,]+,\s*([A-Z]{2})')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_regex.search(desc)
    if m:
        return m.group(1)
    m2 = alt_regex.search(desc)
    if m2:
        return m2.group(1)
    return None

# Apply
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None
if 'description' not in df_b.columns:
    df_b['description'] = None

df_b['has_wifi'] = df_b['attributes'].apply(offers_wifi)
df_b['state'] = df_b['description'].apply(extract_state)

# Filter
df_wifi = df_b[df_b['has_wifi'] & df_b['state'].notnull()].copy()

# Count per state
state_counts = df_wifi.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top = state_counts.sort_values(['wifi_business_count','state'], ascending=[False, True]).iloc[0]
    top_state = top['state']
    top_count = int(top['wifi_business_count'])

    df_r = pd.DataFrame(reviews)
    if 'rating' in df_r.columns:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = None
    # map business_ref to business_id
    if 'business_ref' in df_r.columns:
        df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_')
    else:
        df_r['business_id'] = None

    wifi_bids_top = set(df_wifi[df_wifi['state'] == top_state]['business_id'].unique())
    df_top_reviews = df_r[df_r['business_id'].isin(wifi_bids_top)].copy()
    if df_top_reviews.empty or df_top_reviews['rating'].dropna().empty:
        avg_rating = None
    else:
        avg_rating = float(df_top_reviews['rating'].mean())
    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 3)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dN2JuewUADycIK9fd1n5g06L': ['business', 'checkin'], 'var_call_m3teTuDAOvNmpwr4YK3rMjWx': ['review', 'tip', 'user'], 'var_call_7dr5SRMBkApBL3tOjutkL1x7': 'file_storage/call_7dr5SRMBkApBL3tOjutkL1x7.json', 'var_call_opnFEcPgJzaAR3lRvcVMz2DI': 'file_storage/call_opnFEcPgJzaAR3lRvcVMz2DI.json', 'var_call_SEhndpyOCax4bJVGXTt6Q05b': {'state': None, 'wifi_business_count': 0, 'average_rating': None}}

exec(code, env_args)
