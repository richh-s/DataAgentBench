code = """import json
from collections import defaultdict

# Load query results from previous tool calls
sql_results = var_call_z1z1ZCsHlHchj4Moe5NcCkA3
# var_call_er... is a file path to the full JSON result
business_json_path = var_call_erTCfKX5IqV1Xnsj4NnnlfBU

# Load full business collection JSON from file
with open(business_json_path, 'r', encoding='utf-8') as f:
    business_docs = json.load(f)

# Build mapping from business_id to description (and name) for fast lookup
biz_map = {}
for doc in business_docs:
    bid = doc.get('business_id')
    name = doc.get('name')
    desc = doc.get('description') or ''
    biz_map[bid] = {'name': name, 'description': desc}

# Helper to extract category tokens from description
import re

keywords = ['including', 'ranging from', 'in the category of', 'in the categories of',
            'offers a range of services in', 'offers a range of services', 'offers a diverse range of services and products in the fields of',
            'offers a diverse range of services', 'offers a diverse selection of', 'offers a delightful array of options ranging from',
            'offers a delightful selection of', 'offers a range of services in the categories of', 'offers a range of services in the category of',
            'offers', 'provides', 'offering', 'offered']

stop_words = ['making', 'perfect', 'to meet', 'for all', 'providing', 'this', 'located at']

def extract_categories(desc):
    if not desc:
        return []
    desc_lower = desc.lower()
    start = None
    key_used = None
    for kw in keywords:
        idx = desc_lower.find(kw)
        if idx != -1:
            start = idx + len(kw)
            key_used = kw
            break
    if start is None:
        # fallback: try to find 'in ' occurrences after the first sentence
        m = re.search(r' in (the )?([A-Z].*)', desc)
        if m:
            substr = m.group(2)
        else:
            substr = desc
    else:
        substr = desc[start:]

    # Clean leading punctuation and words
    substr = substr.strip(' :,.')
    # Replace words like 'and' with comma to split
    substr = re.sub(r'\band\b', ',', substr, flags=re.IGNORECASE)
    # Remove parenthetical parts
    substr = re.sub(r"\(.*?\)", '', substr)

    parts = [p.strip() for p in substr.split(',') if p.strip()]
    cats = []
    for p in parts:
        # Stop if token begins with stop phrase
        low = p.lower()
        if any(sw in low for sw in stop_words):
            break
        # Remove trailing phrases that are not categories
        p = re.split(r'\b(making|perfect|to meet|for all|providing|who|which)\b', p, flags=re.IGNORECASE)[0]
        p = p.strip(' .;:')
        # Remove leading location fragments like 'Located at ...'
        if re.match(r'located at', p.lower()):
            continue
        # Remove stray words that are clearly not categories
        if len(p) == 0:
            continue
        # Ensure reasonable length
        if len(p) > 200:
            continue
        cats.append(p)
    # Further split tokens that contain ' & ' or '/'
    final = []
    for c in cats:
        for sub in re.split(r'\s&\s|/', c):
            s = sub.strip()
            if s:
                final.append(s)
    # Normalize: remove duplicate whitespace
    final = [re.sub(r'\s+', ' ', f).strip() for f in final]
    return final

# Aggregate review counts per category
cat_counts = defaultdict(int)
not_found = []
for rec in sql_results:
    bref = rec.get('business_ref')
    cnt = int(rec.get('review_count') or 0)
    # map to businessid prefix
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    biz = biz_map.get(bid)
    if not biz:
        not_found.append(bid)
        continue
    desc = biz.get('description') or ''
    cats = extract_categories(desc)
    if not cats:
        # As fallback, use the business name as a category proxy
        cats = [biz.get('name') or bid]
    for c in cats:
        cat_counts[c] += cnt

# Prepare top 5 categories
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]

# Format result as list of dicts
result = [{'category': c, 'review_count': v} for c, v in top5]

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_z1z1ZCsHlHchj4Moe5NcCkA3': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}], 'var_call_erTCfKX5IqV1Xnsj4NnnlfBU': 'file_storage/call_erTCfKX5IqV1Xnsj4NnnlfBU.json'}

exec(code, env_args)
