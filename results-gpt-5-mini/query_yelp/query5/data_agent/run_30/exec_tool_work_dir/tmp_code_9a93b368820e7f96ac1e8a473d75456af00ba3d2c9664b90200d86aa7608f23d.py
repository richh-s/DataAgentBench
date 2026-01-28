code = """import json
import pandas as pd
import re

with open(var_call_gbwHwSqbysbBryWZr9Ne041T, 'r') as f:
    businesses = json.load(f)

bdf = pd.DataFrame(businesses)

# helper functions from prior code
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

def offers_wifi(v):
    if v is None:
        return False
    if any(x in v for x in ['no', 'none']):
        return False
    return True

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r",\s*([A-Z]{2})\b", desc)
    if m:
        return m.group(1)
    return None

bdf['attributes'] = bdf.get('attributes', None)
bdf['description'] = bdf.get('description', '')

bdf['wifi_raw'] = bdf['attributes'].apply(parse_wifi)
bdf['offers_wifi'] = bdf['wifi_raw'].apply(offers_wifi)
bdf['state'] = bdf['description'].apply(extract_state)

# aggregate counts
total = len(bdf)
wifi_total = int(bdf['offers_wifi'].sum())
with_state_total = int(bdf['state'].notnull().sum())
wifi_with_state = int(bdf[bdf['offers_wifi'] & bdf['state'].notnull()].shape[0])

# top example rows where offers_wifi True
examples = []
for i, row in bdf[bdf['offers_wifi']].head(20).iterrows():
    examples.append({'business_id': row.get('business_id'), 'wifi_raw': row.get('wifi_raw'), 'state': row.get('state'), 'description': row.get('description')})

# counts per state for all businesses and for wifi businesses
state_counts_all = bdf['state'].value_counts().to_dict()
state_counts_wifi = bdf[bdf['offers_wifi']]['state'].value_counts(dropna=True).to_dict()

result = {
    'total_businesses': total,
    'wifi_businesses': wifi_total,
    'businesses_with_state': with_state_total,
    'wifi_businesses_with_state': wifi_with_state,
    'state_counts_all_sample': state_counts_all,
    'state_counts_wifi_sample': state_counts_wifi,
    'examples_wifi': examples
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_o67tVfb3ILfk4WUAiMTMgalH': ['checkin', 'business'], 'var_call_8mPFtwEhbfv4OhNqKH5qEJnN': ['review', 'tip', 'user'], 'var_call_gbwHwSqbysbBryWZr9Ne041T': 'file_storage/call_gbwHwSqbysbBryWZr9Ne041T.json', 'var_call_jLB6pH4qk33x9BnnCCX5Ho4f': 'file_storage/call_jLB6pH4qk33x9BnnCCX5Ho4f.json', 'var_call_A07fBOARjLBcYKJ7Nik9b73r': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_VX3hHmjijjX4rZoOLHenNa7n': 'file_storage/call_VX3hHmjijjX4rZoOLHenNa7n.json'}

exec(code, env_args)
