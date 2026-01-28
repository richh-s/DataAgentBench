code = """import json
import pandas as pd
import re

def load_json_var(v):
    import json
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

business_records = load_json_var(var_call_UVZR7709LPZF23DgUxE2dmxz)
review_records = load_json_var(var_call_a7dKfCyZqiBGcFKsysbkg3Rk)

bdf = pd.DataFrame(business_records)

# same helpers
state_re = re.compile(r',\s*([A-Z]{2})\b')
def extract_state(desc):
    try:
        if not desc or not isinstance(desc, str):
            return None
        m = state_re.search(desc)
        if m:
            return m.group(1)
    except Exception:
        return None
    return None

def has_wifi(attrs):
    if not attrs or attrs == 'None':
        return False
    if isinstance(attrs, dict):
        for k in attrs.keys():
            if k.lower() == 'wifi':
                val = attrs[k]
                if val is None:
                    return False
                sval = str(val).lower()
                if 'no' in sval:
                    return False
                return True
        return False
    else:
        s = str(attrs).lower()
        if 'wifi' in s and 'no' not in s:
            return True
        return False

bdf['state'] = bdf['description'].apply(extract_state)
bdf['has_wifi'] = bdf['attributes'].apply(has_wifi)

# diagnostics
total = len(bdf)
states_present = sorted([s for s in bdf['state'].dropna().unique()])
wifi_count = int(bdf['has_wifi'].sum())

# sample wifi rows
sample_wifi = bdf[bdf['has_wifi']].head(10)[['business_id','attributes','description','state']].to_dict(orient='records')

res = {
    'total_business_records': total,
    'states_found_count': len(states_present),
    'states_sample': states_present[:10],
    'wifi_businesses_detected': wifi_count,
    'sample_wifi_businesses': sample_wifi
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_TXbD5C2P6pEcS4aWn6Z30ewF': ['checkin', 'business'], 'var_call_UVZR7709LPZF23DgUxE2dmxz': 'file_storage/call_UVZR7709LPZF23DgUxE2dmxz.json', 'var_call_a7dKfCyZqiBGcFKsysbkg3Rk': 'file_storage/call_a7dKfCyZqiBGcFKsysbkg3Rk.json', 'var_call_T5OsPZHrNmbYXs0kBPfXFVFf': {'state': None, 'wifi_business_count': 0, 'average_rating': None}}

exec(code, env_args)
