code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_XGxTr6c5AlQTKrVZLLc1Xw61, 'r') as f:
    biz_data = json.load(f)
with open(var_call_ueo11QglsWkIsuDo4M1qrKp3, 'r') as f:
    rev_data = json.load(f)

biz_df = pd.DataFrame(biz_data)
biz_df['attributes'] = biz_df.get('attributes', None)
biz_df['description'] = biz_df.get('description', None)

# Function to extract wifi value
def parse_wifi(attr):
    if attr is None:
        return None
    # convert to string
    s = str(attr)
    # search for wifi value
    m = re.search(r'(?i)wifi[^A-Za-z0-9]*([A-Za-z0-9]+)', s)
    if not m:
        return None
    wifi = m.group(1)
    wifi_norm = re.sub('[^A-Za-z0-9]', '', wifi).lower()
    return wifi_norm

biz_df['wifi_norm'] = biz_df['attributes'].apply(parse_wifi)

# Determine wifi offered
biz_df['has_wifi'] = biz_df['wifi_norm'].apply(lambda x: False if x in (None, '', 'no', 'none') else True)

# Extract state from description
def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})(?:[,\.\s]|$)', desc)
    if m:
        return m.group(1)
    m2 = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m2:
        return m2.group(1)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

wifi_biz = biz_df[biz_df['has_wifi'] & biz_df['state'].notnull()].copy()

state_counts = wifi_biz.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top = state_counts.sort_values('wifi_business_count', ascending=False).iloc[0]
    top_state = top['state']
    top_count = int(top['wifi_business_count'])

    rev_df = pd.DataFrame(rev_data)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

    wifi_biz['business_ref'] = wifi_biz['business_id'].astype(str).str.replace('businessid_', 'businessref_')

    top_refs = set(wifi_biz[wifi_biz['state'] == top_state]['business_ref'].unique())
    rev_top = rev_df[rev_df['business_ref'].isin(top_refs)].copy()

    if rev_top.empty:
        avg_rating = None
    else:
        avg_rating = float(rev_top['rating'].mean())

    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pBdzrYsd4HKArKkzG6VdAe1S': ['checkin', 'business'], 'var_call_BDsqebDO9LTX5MKNwA0JzAUC': ['review', 'tip', 'user'], 'var_call_XGxTr6c5AlQTKrVZLLc1Xw61': 'file_storage/call_XGxTr6c5AlQTKrVZLLc1Xw61.json', 'var_call_ueo11QglsWkIsuDo4M1qrKp3': 'file_storage/call_ueo11QglsWkIsuDo4M1qrKp3.json'}

exec(code, env_args)
