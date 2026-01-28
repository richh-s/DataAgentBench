code = """import json
import pandas as pd
import re

with open(var_call_m68jbtLvI9WvM3SmwBlWUERr, 'r') as f:
    businesses = json.load(f)
with open(var_call_fVDfhyKnkuzxg50suzqi10DB, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)

def offers_wifi(attr):
    if attr is None:
        return False
    # if it's a dict or other, convert to str
    s = str(attr).lower()
    if "no" in s and "'no'" in s:
        return False
    if any(k in s for k in ["free","paid","yes","unlimited"):]
        return True
    # fallback: if contains no or unknown -> False
    if 'no' in s:
        return False
    return False

# extract wifi value

def get_wifi(a):
    if isinstance(a, dict):
        return a.get('WiFi')
    return a


US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r",\s*([A-Za-z]{2})\b", desc)
    if m:
        st = m.group(1).upper()
        if st in US_STATES:
            return st
    m = re.search(r"in [^,]+,\s*([A-Za-z]{2})\b", desc)
    if m:
        st = m.group(1).upper()
        if st in US_STATES:
            return st
    return None

# compute

df_b['wifi_attr'] = df_b['attributes'].apply(get_wifi)
df_b['wifi_attr_str'] = df_b['wifi_attr'].astype(str)
df_b['offers_wifi'] = df_b['wifi_attr_str'].str.lower().str.contains('free|paid|yes|unlimited') & (~df_b['wifi_attr_str'].str.lower().str.contains('no'))
df_b['state'] = df_b['description'].apply(extract_state)

wifi_biz = df_b[(df_b['offers_wifi']) & (df_b['state'].notnull())].copy()

state_counts = wifi_biz.groupby('state')['business_id'].nunique().sort_values(ascending=False)

# Prepare sample outputs
result = {
    'total_business_rows': len(df_b),
    'wifi_biz_rows': len(wifi_biz),
    'top_states': state_counts.head(10).to_dict(),
    'sample_wifi_biz': wifi_biz.head(10)[['business_id','wifi_attr_str','state']].to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_m68jbtLvI9WvM3SmwBlWUERr': 'file_storage/call_m68jbtLvI9WvM3SmwBlWUERr.json', 'var_call_fVDfhyKnkuzxg50suzqi10DB': 'file_storage/call_fVDfhyKnkuzxg50suzqi10DB.json', 'var_call_AWI9RmHFlqMTNIVAjP60tCps': {'state': None, 'wifi_business_count': 0, 'average_rating': None}}

exec(code, env_args)
