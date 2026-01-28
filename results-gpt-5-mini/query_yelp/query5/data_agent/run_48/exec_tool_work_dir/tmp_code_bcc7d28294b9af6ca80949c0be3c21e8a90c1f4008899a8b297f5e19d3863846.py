code = """import json
import pandas as pd

# Load data file paths from storage
business_file = var_call_dfaaQ6ETCmxISzGElNjMUdBB
reviews_file = var_call_pQm8djdkb0TBExSSZGoM746i

with open(business_file, 'r') as f:
    businesses = json.load(f)
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

b_df = pd.DataFrame(businesses)
r_df = pd.DataFrame(reviews)

# normalize ratings
r_df['rating'] = pd.to_numeric(r_df['rating'], errors='coerce')

# extract state from description by splitting on commas and finding two-letter token
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    parts = [p.strip() for p in desc.split(',') if p.strip()]
    for p in parts:
        if len(p) == 2 and p.isalpha() and p.isupper():
            return p
    # fallback: look for last part that is two-letter at end of a token
    for p in parts:
        if len(p) >= 2 and p[-2:].isalpha() and p[-2:].isupper():
            cand = p[-2:]
            return cand
    return None

# detect wifi offered from attributes string or dict
def wifi_offered(attr):
    if attr is None:
        return False
    s = str(attr).lower()
    if 'wifi' not in s:
        return False
    # if contains 'no' and does not contain 'free' or 'paid' or 'yes', consider not offered
    if 'no' in s and not any(x in s for x in ('free', 'paid', 'yes')):
        return False
    return True

b_df['state'] = b_df['description'].apply(extract_state)
b_df['wifi'] = b_df['attributes'].apply(wifi_offered)

wifi_biz = b_df[(b_df['wifi'] == True) & (b_df['state'].notna())].copy()

state_counts = wifi_biz['state'].value_counts()
if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top_state = state_counts.idxmax()
    top_count = int(state_counts.max())
    # map businessid_ -> businessref_
    def to_ref(bid):
        if isinstance(bid, str) and bid.startswith('businessid_'):
            return 'businessref_' + bid.split('_',1)[1]
        return bid
    wifi_biz['business_ref'] = wifi_biz['business_id'].apply(to_ref)
    target_refs = set(wifi_biz[wifi_biz['state']==top_state]['business_ref'].tolist())
    target_reviews = r_df[r_df['business_ref'].isin(target_refs)].copy()
    if target_reviews.empty:
        avg_rating = None
    else:
        avg_rating = float(target_reviews['rating'].mean())
    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uBUX7xwocOEhQftURPAM6eSb': ['checkin', 'business'], 'var_call_uebD51MzhowRRBqWtQFiQWb6': ['review', 'tip', 'user'], 'var_call_dfaaQ6ETCmxISzGElNjMUdBB': 'file_storage/call_dfaaQ6ETCmxISzGElNjMUdBB.json', 'var_call_pQm8djdkb0TBExSSZGoM746i': 'file_storage/call_pQm8djdkb0TBExSSZGoM746i.json'}

exec(code, env_args)
