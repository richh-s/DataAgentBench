code = """import json
import pandas as pd
import re

# Load data from storage keys provided by previous tool calls
with open(var_call_v4PFAHXQgeJFQhadysNlv4rK, 'r') as f:
    businesses = json.load(f)
with open(var_call_tV5Ysp0Q7UR4tdGymlUigNb5, 'r') as f:
    reviews = json.load(f)

# Helper to extract numeric id
def extract_num_id(bid):
    if not isinstance(bid, str):
        return None
    parts = bid.split('_')
    return parts[-1]

# Determine if attributes indicate accepting credit cards
def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is True:
            return True
        if isinstance(val, str) and 'True' in val:
            return True
        return False
    if isinstance(attr, str):
        s = attr.strip().lower()
        if s in ('none', 'null'):
            return False
        if 'businessacceptscreditcards' in s and 'true' in s:
            return True
        return False
    return False

# Extract categories from 'categories' field or from description
def extract_categories(rec):
    cat = rec.get('categories', None)
    if cat and isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if cat and isinstance(cat, str):
        parts = [c.strip().strip("'\"") for c in cat.split(',') if c.strip()]
        return parts
    desc = rec.get('description', '')
    if not isinstance(desc, str) or not desc:
        return []
    # Look for 'in <categories>.' pattern
    m = re.search(r"in (.+?)\.", desc, flags=re.IGNORECASE)
    if m:
        seg = m.group(1)
        # remove location/address parts separated by commas at the start
        # split by commas or ' and ' or ' & '
        parts = re.split(r",| and | & ", seg)
        cleaned = []
        for p in parts:
            p = p.strip()
            # remove trailing words like 'services' or 'facility'
            p = re.sub(r"\bservices\b|\bfacility\b", '', p, flags=re.IGNORECASE).strip()
            p = p.strip("'\"")
            if p:
                cleaned.append(p)
        return cleaned
    # fallback: split by commas and return capitalized-looking tokens
    parts = [p.strip() for p in desc.split(',') if p.strip()]
    candidates = [p for p in parts if re.search(r"[A-Za-z]", p)]
    return candidates[:5]

# Build list of business records with relevant fields
rows = []
for b in businesses:
    biz_id = b.get('business_id')
    biz_num = extract_num_id(biz_id)
    attr = b.get('attributes', None)
    acc = accepts_cc(attr)
    cats = extract_categories(b)
    rows.append({'biz_num': biz_num, 'accepts_cc': acc, 'categories': cats})

bdf = pd.DataFrame(rows)

# Filter businesses that accept credit cards
cc_biz = bdf[bdf['accepts_cc'] == True].copy()
if cc_biz.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # explode categories
    cc_biz_expl = cc_biz.explode('categories')
    cc_biz_expl = cc_biz_expl[cc_biz_expl['categories'].notna() & (cc_biz_expl['categories'] != '')]
    if cc_biz_expl.empty:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        cat_counts = cc_biz_expl.groupby('categories')['biz_num'].nunique().reset_index()
        cat_counts = cat_counts.rename(columns={'categories':'category','biz_num':'business_count'})
        cat_counts = cat_counts.sort_values(['business_count','category'], ascending=[False, True])
        top = cat_counts.iloc[0]
        top_cat = top['category']
        top_count = int(top['business_count'])
        # get business nums in top category
        biz_nums_in_top = cc_biz_expl[cc_biz_expl['categories'] == top_cat]['biz_num'].unique().tolist()
        # process reviews
        rdf = pd.DataFrame(reviews)
        rdf['biz_num'] = rdf['business_ref'].apply(extract_num_id)
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
        revs_top = rdf[rdf['biz_num'].isin(biz_nums_in_top)]
        if revs_top.empty:
            avg_rating = None
        else:
            avg_rating = round(float(revs_top['rating'].mean()), 2)
        result = {'category': top_cat, 'business_count': top_count, 'average_rating': avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WxTjm8yJBKjgiFdZopzR8a8o': 'file_storage/call_WxTjm8yJBKjgiFdZopzR8a8o.json', 'var_call_tV5Ysp0Q7UR4tdGymlUigNb5': 'file_storage/call_tV5Ysp0Q7UR4tdGymlUigNb5.json', 'var_call_6SH0MDadi61uDz9mR8tLuNgV': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_v4PFAHXQgeJFQhadysNlv4rK': 'file_storage/call_v4PFAHXQgeJFQhadysNlv4rK.json'}

exec(code, env_args)
