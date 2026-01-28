code = """import json

# Load the business collection result stored in var_call_FjUnubLN1jtXQpNIovHafnH2
file_path = var_call_FjUnubLN1jtXQpNIovHafnH2
with open(file_path, 'r') as f:
    docs = json.load(f)

refs = []
ref_to_category = {}

for d in docs:
    bid = d.get('business_id')
    attrs = d.get('attributes')
    accepts = False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is not None:
            if str(val).lower() == 'true':
                accepts = True
    # some entries might have attributes as a string 'None' or "None"
    if not accepts:
        # check if attributes is a string containing BusinessAcceptsCreditCards
        if isinstance(attrs, str):
            if 'BusinessAcceptsCreditCards' in attrs and 'True' in attrs:
                accepts = True
    if not accepts:
        continue
    # determine category
    category = None
    # check explicit categories field
    if 'categories' in d and d.get('categories'):
        c = d.get('categories')
        if isinstance(c, list) and len(c)>0:
            category = str(c[0])
        elif isinstance(c, str) and c.strip():
            category = c.split(',')[0].strip()
    if not category:
        desc = d.get('description') or ''
        cat = None
        # attempt to find " in " followed by categories
        if ' in ' in desc:
            # heuristic: take the last ' in ' occurrence
            parts = desc.rsplit(' in ', 1)
            tail = parts[-1]
            # take up to the first period
            tail = tail.split('.', 1)[0]
            # remove leading location like 'Goleta, CA, this facility offers ...' so find 'offers' or 'offers a' and skip
            if 'offers' in tail:
                tail_after_offers = tail.split('offers',1)[-1]
                # remove common prefixes
                for pref in [' a range of services', " a diverse range of services and products", ' a nurturing environment for young learners, providing a range of services in', ' a wide range of services, including']:
                    if tail_after_offers.strip().startswith(pref.strip()):
                        tail_after_offers = tail_after_offers.replace(pref, '')
                cand = tail_after_offers
            else:
                cand = tail
            # split by commas
            cand = cand.strip().strip("'")
            if cand:
                category = cand.split(',')[0].strip()
        # fallback
    if not category:
        category = 'Unknown'
    # form business_ref
    if bid and bid.startswith('businessid_'):
        bref = bid.replace('businessid_', 'businessref_')
    else:
        bref = bid
    refs.append(bref)
    ref_to_category[bref] = category

result = {
    'business_refs': refs,
    'ref_to_category': ref_to_category,
    'count_credit_card_businesses': len(refs)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ON7DXNzg44RXYnmlF5NVxm84': ['business', 'checkin'], 'var_call_Pgxm7eIExSxzxvdTgnJfg3u5': ['review', 'tip', 'user'], 'var_call_FjUnubLN1jtXQpNIovHafnH2': 'file_storage/call_FjUnubLN1jtXQpNIovHafnH2.json'}

exec(code, env_args)
