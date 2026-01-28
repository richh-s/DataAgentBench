code = """import json
import pandas as pd
import re

# Load business data
with open(var_call_2jAw3fRCyl7WALelgzrDx8Vm, 'r') as f:
    businesses = json.load(f)

# Load reviews
with open(var_call_P2Hh6iznqB54L95Xt31bwNNm, 'r') as f:
    reviews = json.load(f)

# Create DataFrame
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure columns exist
if 'business_id' not in bdf.columns:
    bdf['business_id'] = bdf.get('business_id', None)
if 'attributes' not in bdf.columns:
    bdf['attributes'] = bdf.get('attributes', None)
if 'description' not in bdf.columns:
    bdf['description'] = bdf.get('description', '')

# Helper to extract state from description
state_re1 = re.compile(r'in [^,\n]+,\s*([A-Z]{2})')
state_re2 = re.compile(r'location\s.*?,\s*([A-Z]{2})', re.IGNORECASE)
state_re_any = re.compile(r',\s*([A-Z]{2})')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_re1.search(desc)
    if m:
        return m.group(1)
    m = state_re2.search(desc)
    if m:
        return m.group(1)
    # fallback: take last two-letter uppercase after a comma
    m = state_re_any.search(desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Helper to determine if business offers WiFi
wifi_re = re.compile(r"WiFi[^:]*:\s*(u?['\"](?P<v>[^'\"]+)['\"]|(?P<v2>[^,}\n]+))", re.IGNORECASE)

def offers_wifi(attr):
    if attr is None:
        return False
    s = str(attr)
    m = wifi_re.search(s)
    if m:
        val = m.group('v') if m.group('v') is not None else m.group('v2')
        if val is None:
            return False
        val = str(val).strip().lower()
        if val == 'no' or val == 'none' or val == 'false':
            return False
        return True
    return False

bdf['offers_wifi'] = bdf['attributes'].apply(offers_wifi)

# Filter businesses that offer wifi and have state
wifi_biz = bdf[(bdf['offers_wifi'] == True) & (bdf['state'].notna())]

# Count per state
state_counts = wifi_biz['state'].value_counts()
if state_counts.empty:
    result = {'state': None, 'business_count': 0, 'average_rating': None}
else:
    top_state = state_counts.idxmax()
    top_count = int(state_counts.max())

    # Map business_id to business_ref
    def bizid_to_ref(bid):
        if not isinstance(bid, str):
            return None
        return bid.replace('businessid_', 'businessref_')

    wifi_biz_in_top = wifi_biz[wifi_biz['state'] == top_state]
    refs = wifi_biz_in_top['business_id'].apply(bizid_to_ref).dropna().unique().tolist()

    # Prepare reviews dataframe
    if 'rating' in rdf.columns:
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
    else:
        rdf['rating'] = pd.Series(dtype=float)

    # Filter reviews for these refs
    rdf_filtered = rdf[rdf['business_ref'].isin(refs)]
    if rdf_filtered.empty:
        avg_rating = None
    else:
        avg_rating = float(rdf_filtered['rating'].mean())

    result = {'state': top_state, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VjizeayzA927lItQUJe4dMH6': ['checkin', 'business'], 'var_call_Wr9aAV4pPzVcjsuAPvHOMtSq': ['review', 'tip', 'user'], 'var_call_2jAw3fRCyl7WALelgzrDx8Vm': 'file_storage/call_2jAw3fRCyl7WALelgzrDx8Vm.json', 'var_call_P2Hh6iznqB54L95Xt31bwNNm': 'file_storage/call_P2Hh6iznqB54L95Xt31bwNNm.json'}

exec(code, env_args)
