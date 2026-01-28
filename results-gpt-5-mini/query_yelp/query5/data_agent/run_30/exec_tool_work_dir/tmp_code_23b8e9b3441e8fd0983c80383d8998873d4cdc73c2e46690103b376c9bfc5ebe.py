code = """import json
import pandas as pd
import re

with open(var_call_gbwHwSqbysbBryWZr9Ne041T, 'r') as f:
    businesses = json.load(f)
with open(var_call_jLB6pH4qk33x9BnnCCX5Ho4f, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# parse wifi
def parse_wifi(attr):
    if attr is None or attr == 'None':
        return None
    if isinstance(attr, dict):
        v = attr.get('WiFi') or attr.get('wifi')
    else:
        s = str(attr)
        if 'wifi' in s.lower():
            s2 = s.lower()
            for token in ['free', 'paid', 'yes', 'no', 'none']:
                if token in s2:
                    v = token
                    break
            else:
                v = None
        else:
            v = None
    if v is None:
        return None
    v = str(v).lower().replace("u'", '').replace("'", '').replace('"', '').strip()
    return v

bdf['attributes'] = bdf.get('attributes', None)
bdf['description'] = bdf.get('description', '')

bdf['wifi_raw'] = bdf['attributes'].apply(parse_wifi)

def offers_wifi(v):
    if v is None:
        return False
    if any(x in v for x in ['no', 'none']):
        return False
    return True

bdf['offers_wifi'] = bdf['wifi_raw'].apply(offers_wifi)

# extract state
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r",\s*([A-Z]{2})\b", desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

wifi_biz = bdf[(bdf['offers_wifi']) & (bdf['state'].notnull())].copy()
if 'business_id' not in wifi_biz.columns:
    wifi_biz['business_id'] = None
wifi_biz['business_ref'] = wifi_biz['business_id'].astype(str).str.replace('businessid_', 'businessref_')

# prepare reviews
if 'business_ref' not in rdf.columns or 'rating' not in rdf.columns:
    rdf = pd.DataFrame(columns=['business_ref', 'rating'])
else:
    rdf = rdf[['business_ref', 'rating']].copy()
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# merge
merged = pd.merge(rdf, wifi_biz[['business_ref', 'state']], on='business_ref', how='inner')

state_counts = wifi_biz.groupby('state')['business_id'].nunique().rename('wifi_business_count')
state_avg = merged.groupby('state')['rating'].mean().rename('average_rating')

summary = pd.concat([state_counts, state_avg], axis=1).reset_index()
summary['average_rating'] = summary['average_rating'].apply(lambda x: None if pd.isna(x) else float(round(float(x), 3)))
summary['wifi_business_count'] = summary['wifi_business_count'].astype(int)

if summary.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    maxc = summary['wifi_business_count'].max()
    cand = summary[summary['wifi_business_count'] == maxc].copy()
    cand['avg_sort'] = cand['average_rating'].apply(lambda x: x if x is not None else -999)
    cand = cand.sort_values(by=['avg_sort', 'state'], ascending=[False, True])
    top = cand.iloc[0]
    result = {'state': top['state'], 'wifi_business_count': int(top['wifi_business_count']), 'average_rating': top['average_rating']}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_o67tVfb3ILfk4WUAiMTMgalH': ['checkin', 'business'], 'var_call_8mPFtwEhbfv4OhNqKH5qEJnN': ['review', 'tip', 'user'], 'var_call_gbwHwSqbysbBryWZr9Ne041T': 'file_storage/call_gbwHwSqbysbBryWZr9Ne041T.json', 'var_call_jLB6pH4qk33x9BnnCCX5Ho4f': 'file_storage/call_jLB6pH4qk33x9BnnCCX5Ho4f.json'}

exec(code, env_args)
