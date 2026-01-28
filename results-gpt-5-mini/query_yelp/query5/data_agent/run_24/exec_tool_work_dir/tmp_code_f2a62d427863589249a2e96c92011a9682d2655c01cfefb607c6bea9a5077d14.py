code = """import json
import pandas as pd
import re

with open(var_call_m68jbtLvI9WvM3SmwBlWUERr, 'r') as f:
    businesses = json.load(f)

DF = pd.DataFrame(businesses)

def get_wifi(a):
    if isinstance(a, dict):
        return a.get('WiFi')
    return a

def offers_wifi_val(val):
    if val is None:
        return False
    s = str(val).lower()
    if re.search(r"\bno\b", s):
        return False
    if any(k in s for k in ['free','paid','yes','unlimited','wifi']):
        return True
    return False

US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r"in [^,]+,\s*([A-Za-z]{2})\b", desc)
    if m:
        st = m.group(1).upper()
        if st in US_STATES:
            return st
    m2 = re.search(r",\s*([A-Za-z]{2})[\.,]\b", desc)
    if m2:
        st = m2.group(1).upper()
        if st in US_STATES:
            return st
    m3 = re.search(r",\s*([A-Za-z]{2})\s*$", desc)
    if m3:
        st = m3.group(1).upper()
        if st in US_STATES:
            return st
    return None

DF['wifi_attr'] = DF['attributes'].apply(get_wifi)
DF['wifi_attr_str'] = DF['wifi_attr'].astype(str)
DF['offers_wifi'] = DF['wifi_attr_str'].apply(lambda s: offers_wifi_val(s))
DF['state'] = DF['description'].apply(extract_state)

out = DF[['business_id','wifi_attr_str','offers_wifi','state']].to_dict(orient='records')

result = {'rows': out, 'total': len(DF), 'wifi_offered_count': sum(1 for r in out if r['offers_wifi'])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_m68jbtLvI9WvM3SmwBlWUERr': 'file_storage/call_m68jbtLvI9WvM3SmwBlWUERr.json', 'var_call_fVDfhyKnkuzxg50suzqi10DB': 'file_storage/call_fVDfhyKnkuzxg50suzqi10DB.json', 'var_call_AWI9RmHFlqMTNIVAjP60tCps': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_51hd07zFeCaSF0tNTAAqBGBW': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_k3CMmxNhl4ezuT4CvxbSEa4O': 'file_storage/call_k3CMmxNhl4ezuT4CvxbSEa4O.json'}

exec(code, env_args)
