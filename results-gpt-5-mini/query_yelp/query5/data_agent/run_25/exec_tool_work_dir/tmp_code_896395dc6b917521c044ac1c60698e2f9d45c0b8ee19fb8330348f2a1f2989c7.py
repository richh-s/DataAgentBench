code = """import json
import pandas as pd

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
    # handle dict attributes
    if isinstance(attr, dict):
        wifi_val = attr.get('WiFi')
    elif isinstance(attr, str):
        al = attr.lower()
        if 'wifi' in al:
            if 'free' in al:
                wifi_val = 'free'
            elif 'no' in al:
                wifi_val = 'no'
            elif 'paid' in al:
                wifi_val = 'paid'
            else:
                wifi_val = 'unknown'
    # normalize wifi_val string
    if isinstance(wifi_val, str):
        w = wifi_val.strip()
        # remove leading u' or surrounding quotes
        if w.startswith("u'") or w.startswith('u"'):
            w = w[2:]
        if (w.startswith("'") and w.endswith("'")) or (w.startswith('"') and w.endswith('"')):
            w = w[1:-1]
        wifi_val = w
    offers = False
    if wifi_val is not None:
        lw = str(wifi_val).lower()
        if lw == 'no':
            offers = False
        else:
            offers = True
    # extract state from description by splitting on commas and finding a two-letter token
    state = None
    parts = [p.strip() for p in desc.split(',') if p.strip()]
    for p in parts:
        if len(p) == 2 and p.isalpha() and p.isupper():
            state = p
            break
    # fallback: take last part and if it ends with 2 uppercase letters
    if state is None and parts:
        last = parts[-1]
        if len(last) >= 2 and last[-2:].isalpha() and last[-2:].isupper():
            state = last[-2:]

    rows.append({'business_id': bid, 'wifi_val': wifi_val, 'offers_wifi': offers, 'state': state})

bdf = pd.DataFrame(rows)
# keep with state
bdf = bdf[bdf['state'].notnull()]
# filter offers wifi
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
