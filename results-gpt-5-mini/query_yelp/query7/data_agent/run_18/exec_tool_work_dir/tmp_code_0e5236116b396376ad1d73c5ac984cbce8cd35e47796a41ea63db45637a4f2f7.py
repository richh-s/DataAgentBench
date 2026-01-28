code = """import json, re
# Load variables from previous tool calls
reviews = var_call_OyZAvKqaeA0cak02EIPNVXVZ
business_file = var_call_fXQpYhlrwqdOyB4ixgrWCUVX
# business_file is a file path to a JSON file with list of business docs
with open(business_file, 'r') as f:
    businesses = json.load(f)
# Build mapping from business_id to categories (as list)
biz_cat = {}
for b in businesses:
    bid = b.get('business_id')
    cats = None
    # try explicit categories field
    if 'categories' in b and b.get('categories'):
        if isinstance(b['categories'], list):
            cats = [c.strip() for c in b['categories'] if c]
        elif isinstance(b['categories'], str):
            cats = [c.strip() for c in b['categories'].split(',') if c.strip()]
    # fallback: parse description
    if not cats:
        desc = b.get('description') or ''
        # look for phrases indicating categories
        # common patterns: 'offers a range of services in X, Y, and Z.' or "offers a range of services in the categories of X, Y"
        m = re.search(r'(offers (?:a range of )?services (?:in|in the categories of|in the category of|including)|offers a diverse range of options (?:ranging )?from|offers a range of options (?:including )?)\s*(.+)', desc, flags=re.IGNORECASE)
        cats_list = None
        if m:
            tail = m.group(2)
            # cut off at first period
            tail = tail.split('.')[0]
            # remove leading location phrases like 'providing a range of services in '
            # split by commas and ' and '
            parts = re.split(r',| and |, and ', tail)
            parts = [p.strip() for p in parts if p.strip()]
            # remove trailing words like 'making it a perfect spot for any occasion' by filtering out parts with too many words that look like sentences
            cleaned = []
            for p in parts:
                # drop segments that contain 'in ' or addresses (digits with street abbreviations)
                if re.search(r'\d{2,}', p):
                    continue
                # often categories include words like 'Restaurants', 'Beauty & Spas'
                cleaned.append(p)
            if cleaned:
                cats_list = cleaned
        # if still none, try to extract last clause after last comma
        if not cats_list:
            desc_parts = [s.strip() for s in desc.split('.') if s.strip()]
            if desc_parts:
                last = desc_parts[-1]
                # split last by commas
                parts = [p.strip() for p in re.split(r',| and ', last) if p.strip()]
                if parts and len(parts) <= 10:
                    cats_list = parts
        if cats_list:
            # further clean tokens by removing leading phrases like 'ranging from', 'including'
            final = []
            for tok in cats_list:
                tok = re.sub(r'^(ranging from|including|such as|offering|offering a range of options|providing a range of services in)\s*', '', tok, flags=re.IGNORECASE)
                tok = tok.strip().strip('.').strip()
                if tok:
                    final.append(tok)
            cats = final if final else None
    if not cats:
        cats = []
    biz_cat[bid] = cats

# Now aggregate review counts per category
from collections import defaultdict
cat_counts = defaultdict(int)
missing_businesses = []
for r in reviews:
    bref = r.get('business_ref')
    try:
        cnt = int(r.get('review_count') or 0)
    except:
        cnt = 0
    if not bref:
        continue
    # translate to businessid_
    if bref.startswith('businessref_'):
        bid = 'businessid_' + bref.split('_',1)[1]
    else:
        bid = bref
    cats = biz_cat.get(bid)
    if cats is None:
        missing_businesses.append(bid)
        continue
    if not cats:
        # if no categories found, attribute to 'Unknown'
        cat_counts['Unknown'] += cnt
    else:
        for c in cats:
            cat_counts[c] += cnt

# Prepare top 5 categories
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': k, 'review_count': v} for k,v in sorted_cats[:5]]
# Output
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_tVS7x3aoQ7nYhfziTVSmNTJ2': ['business', 'checkin'], 'var_call_GKO7iyfChH297dktylUcjbwM': ['review', 'tip', 'user'], 'var_call_fXQpYhlrwqdOyB4ixgrWCUVX': 'file_storage/call_fXQpYhlrwqdOyB4ixgrWCUVX.json', 'var_call_OyZAvKqaeA0cak02EIPNVXVZ': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_call_uLotrxtCEKKAzeNU7Vr9lR4N': {'collection': 'business', 'filter': {'business_id': {'$in': ['businessid_45', 'businessid_74', 'businessid_66', 'businessid_33', 'businessid_36', 'businessid_60', 'businessid_57', 'businessid_92', 'businessid_96', 'businessid_13', 'businessid_15', 'businessid_12', 'businessid_31', 'businessid_53', 'businessid_86', 'businessid_62', 'businessid_37', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_79', 'businessid_98', 'businessid_14', 'businessid_6', 'businessid_20']}}, 'projection': {'business_id': 1, 'name': 1, 'description': 1, 'categories': 1}, 'limit': 1000}}

exec(code, env_args)
