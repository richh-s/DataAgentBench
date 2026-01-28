code = """import json
import pandas as pd
import re

# Load business data
with open(var_call_2jAw3fRCyl7WALelgzrDx8Vm, 'r') as f:
    businesses = json.load(f)

# Load reviews
with open(var_call_P2Hh6iznqB54L95Xt31bwNNm, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure fields
bdf['description'] = bdf.get('description', '')

state_pattern = re.compile(r',\s*([A-Z]{2})(?:\b|,|$)')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    matches = state_pattern.findall(desc)
    if not matches:
        return None
    return matches[-1]

bdf['state'] = bdf['description'].apply(extract_state)

# Determine if offers wifi
def offers_wifi(attr):
    if attr is None:
        return False
    s = str(attr).lower()
    if 'wifi' not in s:
        return False
    pos = s.find('wifi')
    window = s[pos:pos+30]
    if any(x in window for x in ['no', 'none', "false"]):
        return False
    return True

bdf['offers_wifi'] = bdf['attributes'].apply(offers_wifi)

wifi_biz = bdf[(bdf['offers_wifi'] == True) & (bdf['state'].notna())]

state_counts = wifi_biz['state'].value_counts()

if state_counts.empty:
    result = {'state': None, 'business_count': 0, 'average_rating': None}
else:
    top_state = state_counts.idxmax()
    top_count = int(state_counts.max())

    def bizid_to_ref(bid):
        if not isinstance(bid, str):
            return None
        return bid.replace('businessid_', 'businessref_')

    wifi_biz_in_top = wifi_biz[wifi_biz['state'] == top_state]
    refs = wifi_biz_in_top['business_id'].apply(bizid_to_ref).dropna().unique().tolist()

    if 'rating' in rdf.columns:
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
    else:
        rdf['rating'] = pd.Series(dtype=float)

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
