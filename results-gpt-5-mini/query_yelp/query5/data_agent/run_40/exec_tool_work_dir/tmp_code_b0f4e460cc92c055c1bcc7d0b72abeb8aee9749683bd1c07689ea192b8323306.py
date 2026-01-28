code = """import json
import pandas as pd
import re

# Load the data files from storage (paths provided by previous tool calls)
with open(var_call_mWgCCFD4CvzIFr5XtKicdWSx, 'r') as f:
    businesses = json.load(f)
with open(var_call_jqDQXLnnWKUhEThCVKfHIfcx, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize attributes and extract WiFi field
def get_wifi(attr):
    if attr is None:
        return None
    if isinstance(attr, dict):
        return attr.get('WiFi')
    # sometimes attributes stored as string like "None" or other
    try:
        # attempt to eval-ish: if it's a string representation of a dict, look for WiFi key
        if isinstance(attr, str) and "WiFi" in attr:
            # crude extraction of WiFi value from string
            m = re.search(r"WiFi\W*[:=]\W*('?\w+" + "'?)", attr)
            if m:
                return m.group(1)
    except Exception:
        pass
    return None

bdf['wifi_raw'] = bdf['attributes'].apply(get_wifi)

# Determine whether business offers WiFi: wifi_raw not None and not contains 'no' or 'None'

def offers_wifi(x):
    if x is None:
        return False
    s = str(x).lower()
    if 'no' in s and 'free' not in s:  # if contains no and not free
        return False
    if 'none' in s:
        return False
    if s.strip() == "":
        return False
    return True

bdf['offers_wifi'] = bdf['wifi_raw'].apply(offers_wifi)

# Extract state from description using regex

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # common pattern: ", XX," where XX is state
    m = re.search(r',\s*([A-Z]{2})[,\s]', desc)
    if m:
        return m.group(1)
    # fallback: 'in City, ST' pattern
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Filter businesses that offer wifi and have a state
wifi_biz = bdf[(bdf['offers_wifi']) & (bdf['state'].notnull())].copy()

# Count per state
state_counts = wifi_biz['state'].value_counts().to_dict()

if not state_counts:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    # state with max businesses
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    top_count = state_counts[top_state]

    # get business_ids for that state
    biz_ids = wifi_biz[wifi_biz['state'] == top_state]['business_id'].tolist()
    # convert to business_ref format
    biz_refs = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]

    # prepare reviews df: ensure rating numeric
    if not rdf.empty:
        rdf = rdf.copy()
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
        # filter reviews for those business refs
        reviews_for_state = rdf[rdf['business_ref'].isin(biz_refs)]
        if len(reviews_for_state) == 0:
            avg_rating = None
            num_reviews = 0
        else:
            avg_rating = float(reviews_for_state['rating'].mean())
            num_reviews = int(reviews_for_state.shape[0])
    else:
        avg_rating = None
        num_reviews = 0

    # round average to 2 decimals if not None
    if avg_rating is not None:
        avg_rating = round(avg_rating, 2)

    result = {"state": top_state, "business_count": int(top_count), "average_rating": avg_rating, "num_reviews": num_reviews}

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vbuCBKzBsv1WVNlhYwgAuD7p': ['checkin', 'business'], 'var_call_k5sGbiL4oFmiqIfZ4WcPHHpk': ['review', 'tip', 'user'], 'var_call_mWgCCFD4CvzIFr5XtKicdWSx': 'file_storage/call_mWgCCFD4CvzIFr5XtKicdWSx.json', 'var_call_jqDQXLnnWKUhEThCVKfHIfcx': 'file_storage/call_jqDQXLnnWKUhEThCVKfHIfcx.json'}

exec(code, env_args)
