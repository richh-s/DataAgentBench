code = """import json, re

# Load inputs from storage-provided variables
business_file = var_call_Oci4PspAOshn9qT6uWFf2wWx
with open(business_file, 'r') as f:
    business_docs = json.load(f)

review_counts = var_call_ILOK88MRxsjVg38kz9EMv0Vt

# Build mapping from business_ref -> count (int)
ref_cnt = {r['business_ref']: int(r['cnt']) for r in review_counts}

# Map to business_id and gather descriptions
id_to_doc = {b.get('business_id'): b for b in business_docs}

# Simple category extractor
def extract_categories(desc):
    if not desc or not isinstance(desc, str):
        return []
    text = desc
    # Lowercase for keyword search
    low = text.lower()
    # Try to find 'including' or 'in the category of' or 'offers' or 'in ' patterns
    idx = None
    for kw in [' including ', ' in the category of ', ' in the fields of ', ' offers ', ' offering ', ' provides ', ' in ']:
        j = low.find(kw)
        if j != -1:
            idx = j + len(kw)
            break
    if idx is not None:
        fragment = text[idx:]
    else:
        # fallback: take last part after last comma
        parts = text.split(',')
        fragment = parts[-1] if parts else text
    # remove trailing sentences after period
    fragment = fragment.split('.')[0]
    # split by commas and ' and '
    parts = re.split(',| and |;|\|', fragment)
    cats = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # remove location fragments like 'located at'
        if p.lower().startswith('located at'):
            continue
        # drop if contains address-like numbers
        if re.search(r'\d', p):
            continue
        # trim
        p = p.strip(' .;\n\t')
        if p:
            cats.append(p)
    # further split on '/' and '&'
    final = []
    for c in cats:
        for part in re.split('/|&|-', c):
            part = part.strip()
            if part:
                final.append(part)
    # dedup
    seen=set(); out=[]
    for c in final:
        if c not in seen:
            seen.add(c); out.append(c)
    return out

from collections import defaultdict
cat_counts = defaultdict(int)
missing = 0
for ref, cnt in ref_cnt.items():
    bid = ref.replace('businessref_', 'businessid_')
    doc = id_to_doc.get(bid)
    if not doc:
        missing += 1
        continue
    desc = doc.get('description') or ''
    cats = extract_categories(desc)
    if not cats:
        name = doc.get('name','')
        if name:
            cats = [name]
    for c in cats:
        cat_counts[c] += cnt

sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]
result = [{"category": c, "total_reviews": v} for c, v in top5]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9jAHS88rMcFyHKXqRNMakGIe': ['checkin', 'business'], 'var_call_TM4HJMPVQToH4o8Yp6f5nPu3': ['review', 'tip', 'user'], 'var_call_Oci4PspAOshn9qT6uWFf2wWx': 'file_storage/call_Oci4PspAOshn9qT6uWFf2wWx.json', 'var_call_ILOK88MRxsjVg38kz9EMv0Vt': [{'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_33', 'cnt': '2'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '1'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}]}

exec(code, env_args)
