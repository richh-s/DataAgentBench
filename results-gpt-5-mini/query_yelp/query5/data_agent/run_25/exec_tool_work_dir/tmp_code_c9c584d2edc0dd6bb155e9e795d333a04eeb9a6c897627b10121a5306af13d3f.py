code = """import json
import pandas as pd
import re

businesss_path = var_call_IKWujBNHTebPwcihWYShzoM9
reviews_path = var_call_30w7Ze5vJ4gAizTxPlz23nvQ

with open(businesss_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(reviews_path, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

rows = []
for rec in businesses:
    bid = rec.get('business_id')
    attr = rec.get('attributes')
    desc = rec.get('description') or ''
    wifi_val = None
    if isinstance(attr, dict):
        wifi_val = attr.get('WiFi')
    elif isinstance(attr, str):
        if 'WiFi' in attr:
            # attempt simple extraction: find "WiFi" and then take up to next comma or brace
            idx = attr.find('WiFi')
            snippet = attr[idx: idx+50]
            # look for colon or colon-like
            m = re.search(r"WiFi\s*[:=]\s*([\"']?)([^,}\n\"]+)", snippet)
            if m:
                wifi_val = m.group(2)
            else:
                # fallback: mark as present but unknown
                wifi_val = 'unknown'
    if isinstance(wifi_val, str):
        wifi_val = wifi_val.strip()
        # remove leading u' or surrounding quotes
        wifi_val = re.sub(r"^[uU]?[\"']?(.*?)[\"']?$", r"\1", wifi_val)
    offers = False
    if wifi_val is not None:
        lw = str(wifi_val).lower()
        if 'no' in lw or 'none' in lw:
            offers = False
        elif 'free' in lw or 'paid' in lw or 'yes' in lw or lw == 'unknown':
            offers = True
        else:
            offers = True
    # extract state from description: look for pattern ", XX" where XX are uppercase letters
    state = None
    if desc:
        m = re.search(r",\s*([A-Z]{2})(?:\b|,)", desc)
        if m:
            state = m.group(1)
    rows.append({'business_id': bid, 'wifi_val': wifi_val, 'offers_wifi': offers, 'state': state})

bdf = pd.DataFrame(rows)
# keep rows with state
bdf = bdf[bdf['state'].notnull()]
# filter businesses that offer wifi
wifi_biz = bdf[bdf['offers_wifi'] == True].copy()
state_counts = wifi_biz.groupby('state').size().reset_index(name='count')
if state_counts.empty:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    state_counts = state_counts.sort_values(['count', 'state'], ascending=[False, True])
    top = state_counts.iloc[0]
    top_state = top['state']
    top_count = int(top['count'])
    biz_ids = wifi_biz[wifi_biz['state'] == top_state]['business_id'].dropna().unique().tolist()
    biz_refs = [str(b).replace('businessid_', 'businessref_') for b in biz_ids]
    rdf = pd.DataFrame(reviews)
    if rdf.empty:
        avg_rating = None
    else:
        if 'rating' in rdf.columns:
            rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
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
