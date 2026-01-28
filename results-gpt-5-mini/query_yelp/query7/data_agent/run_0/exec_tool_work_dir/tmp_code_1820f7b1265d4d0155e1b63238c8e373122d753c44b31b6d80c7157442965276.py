code = """import json, re

# Load inputs from storage-provided variables
business_file = var_call_Oci4PspAOshn9qT6uWFf2wWx  # path to JSON file
with open(business_file, 'r') as f:
    business_docs = json.load(f)

review_counts = var_call_ILOK88MRxsjVg38kz9EMv0Vt  # list of dicts with business_ref and cnt

# Build mapping from business_ref -> count (int)
ref_cnt = {r['business_ref']: int(r['cnt']) for r in review_counts}

# Map to business_id and gather descriptions
id_to_doc = {b.get('business_id'): b for b in business_docs}

# Helper to extract categories from description
def extract_categories(desc):
    if not desc or not isinstance(desc, str):
        return []
    desc = desc.strip()
    # Try to find text after keywords
    patterns = [r'including\s*(.*)',
                r'services,?\s*in\s*(.*)',
                r'services(?:,|\s)*including\s*(.*)',
                r'in the fields of\s*(.*)',
                r'in the category of\s*(.*)',
                r'offers (?:a|an|the)?\s*(?:wide range of )?(?:services,? )?(?:and products )?(?:in|including)?\s*(.*)']
    candidate = None
    for pat in patterns:
        m = re.search(pat, desc, flags=re.I)
        if m:
            candidate = m.group(1)
            break
    if not candidate:
        # fallback: take part after last comma (often categories are at end)
        parts = desc.split(',')
        if len(parts) > 1:
            candidate = ','.join(parts[-3:])  # last few parts
        else:
            candidate = desc
    # Remove trailing location phrases after a period
    candidate = candidate.split('.')[0]
    # Now split candidate into tokens by commas and ' and '
    tokens = re.split(r',|\band\b|;|\|', candidate)
    cats = []
    for t in tokens:
        tt = t.strip()
        # remove leading verbs/phrases
        tt = re.sub(r"^(providing|offering|offering a range of|offering a|offers a range of services in)\b.*?", '', tt, flags=re.I)
        # remove 'and' connectors
        tt = tt.strip(' .:;\n\t')
        # drop tokens that look like addresses or sentences
        if not tt:
            continue
        if re.search(r'\d', tt):
            continue
        # remove leading lowercase sentence fragments
        if tt[0].islower():
            # skip short fragments
            continue
        # common filler words to remove
        if tt.lower().startswith('located at'):
            continue
        # Normalize: remove trailing 'and' or conjunctions
        tt = re.sub(r'\s+and\s*$', '', tt)
        # Normalize whitespace
        tt = re.sub(r'\s+', ' ', tt).strip(' ,')
        if tt:
            cats.append(tt)
    # Further split items that contain '/', '&' into separate categories
    final = []
    for c in cats:
        parts = re.split(r'/|&|\\u2013|-', c)
        for p in parts:
            p = p.strip()
            if p:
                final.append(p)
    # Deduplicate while preserving order
    seen = set(); out=[]
    for c in final:
        if c not in seen:
            seen.add(c); out.append(c)
    return out

# Aggregate counts per category
from collections import defaultdict
cat_counts = defaultdict(int)
missing = 0
for ref, cnt in ref_cnt.items():
    bid = ref.replace('businessref_', 'businessid_')
    doc = id_to_doc.get(bid)
    if not doc:
        missing += 1
        continue
    desc = doc.get('description') or doc.get('attributes') or ''
    cats = extract_categories(desc)
    if not cats:
        # try to use name as category fallback
        name = doc.get('name','')
        if name:
            cats = [name]
    for c in cats:
        cat_counts[c] += cnt

# Prepare sorted top 5
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]
# Format as list of dicts
result = [{"category": c, "total_reviews": v} for c, v in top5]

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9jAHS88rMcFyHKXqRNMakGIe': ['checkin', 'business'], 'var_call_TM4HJMPVQToH4o8Yp6f5nPu3': ['review', 'tip', 'user'], 'var_call_Oci4PspAOshn9qT6uWFf2wWx': 'file_storage/call_Oci4PspAOshn9qT6uWFf2wWx.json', 'var_call_ILOK88MRxsjVg38kz9EMv0Vt': [{'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_33', 'cnt': '2'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '1'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}]}

exec(code, env_args)
