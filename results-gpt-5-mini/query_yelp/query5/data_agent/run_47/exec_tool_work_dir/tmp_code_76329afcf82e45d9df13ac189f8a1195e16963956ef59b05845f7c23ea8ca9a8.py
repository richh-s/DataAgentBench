code = """import json
import pandas as pd

# load the WiFi-specific query results
with open(var_call_xfYZPHwEXj2HeWIXEkVA3mkT, 'r') as f:
    wifi_docs = json.load(f)

# Count by state in this subset as a cross-check
import re
state_regex = re.compile(r',\s*([A-Z]{2})(?:\b|,|$)')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_regex.search(desc)
    if m:
        return m.group(1)
    return None

rows = []
for d in wifi_docs:
    bids = d.get('business_id')
    desc = d.get('description')
    state = extract_state(desc)
    rows.append({'business_id': bids, 'state': state, 'wifi_val': d.get('attributes', {}).get('WiFi') if isinstance(d.get('attributes'), dict) else None})

df = pd.DataFrame(rows)
counts = df[df['state'].notnull()].groupby('state')['business_id'].nunique().reset_index(name='cnt').sort_values('cnt', ascending=False)
print('__RESULT__:')
print(json.dumps(counts.to_dict(orient='records')))"""

env_args = {'var_call_dN2JuewUADycIK9fd1n5g06L': ['business', 'checkin'], 'var_call_m3teTuDAOvNmpwr4YK3rMjWx': ['review', 'tip', 'user'], 'var_call_7dr5SRMBkApBL3tOjutkL1x7': 'file_storage/call_7dr5SRMBkApBL3tOjutkL1x7.json', 'var_call_opnFEcPgJzaAR3lRvcVMz2DI': 'file_storage/call_opnFEcPgJzaAR3lRvcVMz2DI.json', 'var_call_SEhndpyOCax4bJVGXTt6Q05b': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_Bi4RcdoSHpu6OvPMErSxQt9F': {'state': 'PA', 'wifi_business_count': 8, 'average_rating': 3.484}, 'var_call_xfYZPHwEXj2HeWIXEkVA3mkT': 'file_storage/call_xfYZPHwEXj2HeWIXEkVA3mkT.json'}

exec(code, env_args)
