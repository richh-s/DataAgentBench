code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_C2mbQ66HhoKKJY6jVA6s59TH, 'r') as f:
    business_data = json.load(f)
with open(var_call_nHJvBDBWgKRUxoHlXvERAyfZ, 'r') as f:
    review_data = json.load(f)

# Process businesses
rows = []
for b in business_data:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    desc = b.get('description') or ''
    # normalize attributes
    if isinstance(attrs, str):
        if attrs.lower() == 'none':
            attrs = None
    wifi = False
    if isinstance(attrs, dict):
        # keys might be 'WiFi' or 'wifi'
        w = None
        if 'WiFi' in attrs:
            w = attrs.get('WiFi')
        elif 'wifi' in attrs:
            w = attrs.get('wifi')
        if w is not None:
            lw = str(w).lower()
            # consider 'no' or 'none' as not offering wifi
            if ('no' in lw) or ('none' in lw):
                wifi = False
            else:
                wifi = True
    # extract state from description using regex
    state = None
    if isinstance(desc, str):
        m = re.search(r'in [^,]+,\s*([A-Z]{2}),', desc)
        if not m:
            m = re.search(r',\s*([A-Z]{2})(?:,|$)', desc)
        if m:
            state = m.group(1)
    rows.append({'business_id': bid, 'state': state, 'wifi': wifi})

bdf = pd.DataFrame(rows)
# Filter only businesses with a valid state
bdf = bdf[bdf['state'].notnull()]

# Count wifi-offering businesses per state
wifi_counts = bdf[bdf['wifi']].groupby('state').size().sort_values(ascending=False)

if wifi_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    top_state = wifi_counts.index[0]
    top_count = int(wifi_counts.iloc[0])
    # get set of business_ids in that state offering wifi
    top_biz_ids = set(bdf[(bdf['state'] == top_state) & (bdf['wifi'])]['business_id'].tolist())

    # Process reviews and compute average for reviews belonging to those businesses
    ratings = []
    for r in review_data:
        bref = r.get('business_ref')
        rating = r.get('rating')
        if bref and rating is not None:
            # convert businessref_# -> businessid_#
            bid = None
            if isinstance(bref, str) and bref.startswith('businessref_'):
                bid = 'businessid_' + bref.split('_', 1)[1]
            else:
                # fallback mapping
                bid = bref
            if bid in top_biz_ids:
                try:
                    ratings.append(float(rating))
                except:
                    pass
    if len(ratings) == 0:
        avg_rating = None
    else:
        avg_rating = sum(ratings) / len(ratings)
        # round to 2 decimals
        avg_rating = round(avg_rating, 2)
    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Xl71oVCKZDjgBfUGwocbe00I': ['checkin', 'business'], 'var_call_j0nQUdyfEokDYNM1shWtKX51': ['review', 'tip', 'user'], 'var_call_C2mbQ66HhoKKJY6jVA6s59TH': 'file_storage/call_C2mbQ66HhoKKJY6jVA6s59TH.json', 'var_call_nHJvBDBWgKRUxoHlXvERAyfZ': 'file_storage/call_nHJvBDBWgKRUxoHlXvERAyfZ.json'}

exec(code, env_args)
