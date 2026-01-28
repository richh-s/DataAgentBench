code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_uJNAH2s8WNw8K1GRtW5jsGzW, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_FkGQB245PIrixYIpdVDXP80Z, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
# Ensure attributes column exists
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

# Determine WiFi presence
def has_wifi(attr):
    if not attr or attr == 'None':
        return False
    # attr may be dict or string
    if isinstance(attr, dict):
        wifi_val = attr.get('WiFi')
    else:
        # try to parse string representation for WiFi key
        # e.g., "{... 'WiFi': "u'free'", ...}"
        try:
            # crude search
            m = re.search(r"'WiFi'\s*:\s*([^,}]+)", str(attr))
            if m:
                wifi_val = m.group(1)
            else:
                m2 = re.search(r'WiFi\s*[:=]\s*([^,}]+)', str(attr))
                wifi_val = m2.group(1) if m2 else None
        except Exception:
            wifi_val = None
    if wifi_val is None:
        return False
    s = str(wifi_val).lower()
    # consider values indicating no
    if 'no' in s or 'none' in s or 'false' in s:
        return False
    # otherwise if contains free/paid/paid or any word, assume wifi offered
    if 'free' in s or 'paid' in s or 'yes' in s or 'signal' in s or 'spot' in s or "'" in s:
        return True
    # fallback: if non-empty
    return len(s.strip())>0

# extract state from description
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # look for pattern ", XX,"
    m = re.search(r',\s*([A-Z]{2})[,\s]', desc)
    if m:
        return m.group(1)
    # try pattern " in City, ST," as in examples
    m = re.search(r'in\s+[^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    # try last occurrence of ', ' then two letters then maybe end
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

# Apply
df_b['has_wifi'] = df_b['attributes'].apply(has_wifi)
# parse state
df_b['state'] = df_b['description'].apply(extract_state)
# Only consider businesses in US states (2-letter codes)
# Filter has_wifi True
df_wifi = df_b[df_b['has_wifi']==True].copy()

# Map business_id to business_ref
if 'business_id' in df_wifi.columns:
    df_wifi['business_ref'] = df_wifi['business_id'].astype(str).str.replace('businessid_', 'businessref_')
else:
    df_wifi['business_ref'] = None

# Count per state
state_counts = df_wifi.groupby('state').size().drop(index=[None], errors='ignore')
if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top_state = state_counts.idxmax()
    top_count = int(state_counts.max())

    # Load reviews into DataFrame
    df_r = pd.DataFrame(reviews)
    # ensure rating numeric
    if 'rating' in df_r.columns:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = None

    # filter reviews for businesses in top_state
    refs_in_state = set(df_wifi[df_wifi['state']==top_state]['business_ref'].dropna().unique())
    if len(refs_in_state)==0:
        avg_rating = None
    else:
        df_subset = df_r[df_r['business_ref'].isin(refs_in_state)]
        if df_subset.empty:
            avg_rating = None
        else:
            avg = float(df_subset['rating'].mean())
            avg_rating = round(avg, 2)

    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DySUhN0N4DvXJ8RoM9JUJ4v2': ['business', 'checkin'], 'var_call_5wMhIlXt1q3YEJmTslH2CkoG': ['review', 'tip', 'user'], 'var_call_tEjY5OEDXmmHHqAxrFyS4KEn': 'file_storage/call_tEjY5OEDXmmHHqAxrFyS4KEn.json', 'var_call_uJNAH2s8WNw8K1GRtW5jsGzW': 'file_storage/call_uJNAH2s8WNw8K1GRtW5jsGzW.json', 'var_call_FkGQB245PIrixYIpdVDXP80Z': 'file_storage/call_FkGQB245PIrixYIpdVDXP80Z.json'}

exec(code, env_args)
