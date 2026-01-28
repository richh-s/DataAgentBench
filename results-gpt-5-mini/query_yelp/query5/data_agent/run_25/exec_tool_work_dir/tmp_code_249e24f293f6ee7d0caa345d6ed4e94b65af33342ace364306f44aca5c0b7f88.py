code = """import json
import pandas as pd
import re

# Load data from storage file paths
businesss_path = var_call_IKWujBNHTebPwcihWYShzoM9
reviews_path = var_call_30w7Ze5vJ4gAizTxPlz23nvQ

with open(businesss_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Prepare business records
rows = []
for rec in businesses:
    bid = rec.get('business_id')
    attr = rec.get('attributes')
    desc = rec.get('description') or ''
    wifi_val = None
    if isinstance(attr, dict):
        wifi_val = attr.get('WiFi')
    elif isinstance(attr, str):
        # try to extract WiFi value from string representation
        m = re.search(r'WiFi\s*["\']\s*([^,}\n]+)', attr)
        if m:
            wifi_val = m.group(1)
    # normalize wifi_val
    if wifi_val is not None and isinstance(wifi_val, str):
        wifi_val = wifi_val.strip()
        # remove surrounding quotes like u'free' or 'free' or "free"
        wifi_val = re.sub(r'^[uU]?["\']?(.*?)["\']?$', r'\1', wifi_val)
    # determine offers wifi
    offers = False
    if wifi_val is not None:
        lw = str(wifi_val).lower()
        if 'no' in lw or 'none' in lw:
            offers = False
        elif any(x in lw for x in ['free', 'paid', 'yes']):
            offers = True
        else:
            # if value exists but not explicit, treat as offering if not 'no'
            offers = True
    # extract state from description
    state = None
    if desc:
        m2 = re.search(r'in\s+[^,]+,\s*([A-Z]{2})', desc)
        if m2:
            state = m2.group(1)
        else:
            # fallback: search for comma + space + two-letter before end
            m3 = re.search(r',\s*([A-Z]{2})(?:\b|,)', desc)
            if m3:
                state = m3.group(1)
    rows.append({'business_id': bid, 'wifi_val': wifi_val, 'offers_wifi': offers, 'state': state})

bdf = pd.DataFrame(rows)
# filter only entries with state
bdf = bdf[bdf['state'].notnull()]

# consider only businesses that offer wifi
wifi_biz = bdf[bdf['offers_wifi'] == True].copy()

# count per state
state_counts = wifi_biz.groupby('state').size().reset_index(name='count')
if state_counts.empty:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    state_counts = state_counts.sort_values(['count', 'state'], ascending=[False, True])
    top = state_counts.iloc[0]
    top_state = top['state']
    top_count = int(top['count'])
    # find business_refs for that state
    biz_ids = wifi_biz[wifi_biz['state'] == top_state]['business_id'].dropna().unique().tolist()
    biz_refs = [str(b).replace('businessid_', 'businessref_') for b in biz_ids]
    # load reviews into DataFrame
    rdf = pd.DataFrame(reviews)
    if rdf.empty:
        avg_rating = None
    else:
        # ensure rating numeric
        if 'rating' in rdf.columns:
            rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
        # filter reviews for these business refs
        rdf_f = rdf[rdf['business_ref'].isin(biz_refs)]
        if rdf_f.empty:
            avg_rating = None
        else:
            avg_rating = float(rdf_f['rating'].mean())
    result = {"state": top_state, "business_count": top_count, "average_rating": (None if avg_rating is None else round(avg_rating, 2))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oVNVsO9rDQsqu0hI9g6n4nTR': ['business', 'checkin'], 'var_call_7GKsqJQ6UpdqVf9ltYRposmo': ['review', 'tip', 'user'], 'var_call_IKWujBNHTebPwcihWYShzoM9': 'file_storage/call_IKWujBNHTebPwcihWYShzoM9.json', 'var_call_30w7Ze5vJ4gAizTxPlz23nvQ': 'file_storage/call_30w7Ze5vJ4gAizTxPlz23nvQ.json'}

exec(code, env_args)
