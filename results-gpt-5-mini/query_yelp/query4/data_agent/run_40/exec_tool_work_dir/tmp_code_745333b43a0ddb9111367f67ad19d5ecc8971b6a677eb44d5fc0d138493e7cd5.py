code = """import json
import pandas as pd
import re

# Load data
with open(var_call_v4PFAHXQgeJFQhadysNlv4rK, 'r') as f:
    businesses = json.load(f)
with open(var_call_tV5Ysp0Q7UR4tdGymlUigNb5, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# helper to extract biz numeric id
def extract_num_id(bid):
    if not isinstance(bid, str):
        return None
    parts = bid.split('_')
    return parts[-1]

bdf['biz_num'] = bdf.get('business_id', pd.Series([None]*len(bdf))).apply(extract_num_id)
rdf['biz_num'] = rdf['business_ref'].apply(extract_num_id)

# accepts credit card
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
        if s == 'none' or s == 'null':
            return False
        if 'businessacceptscreditcards' in s and 'true' in s:
            return True
        # sometimes attributes serialised include BusinessAcceptsCreditCards: 'True'
        if 'businessacceptscreditcards' in s and 'true' in s:
            return True
        return False
    return False

bdf['accepts_cc'] = bdf.get('attributes', pd.Series([None]*len(bdf))).apply(accepts_cc)

# categories extraction
def extract_categories(row):
    # prefer explicit 'categories' field
    cat = row.get('categories', None)
    if cat and not pd.isna(cat):
        if isinstance(cat, list):
            return [c.strip() for c in cat if c]
        if isinstance(cat, str):
            parts = [c.strip().strip("'\"") for c in cat.split(',') if c.strip()]
            return parts
    # else parse description
    desc = row.get('description', '')
    if not isinstance(desc, str) or not desc:
        return []
    # patterns to search
    patterns = [
        r"offers a range of services in (.*)$",
        r"offers a wide range of services, including (.*)$",
        r"offers a diverse range of services and products in the fields of (.*)$",
        r"offers a delightful array of dishes in the category of (.*)$",
        r"offers a range of services including (.*)$",
        r"offers a range of services, including (.*)$",
        r"offers a diverse range of services and products in the fields of (.*)$",
        r"this .* offers (.*) to",
        r"offers a range of services in the categories of (.*)$",
        r"offers a range of services in (.*)\.$",
    ]
    for pat in patterns:
        m = re.search(pat, desc, flags=re.IGNORECASE)
        if m:
            seg = m.group(1)
            # remove trailing location statements after a period
            seg = seg.split('.')[0]
            # remove enclosing quotes
            seg = seg.strip().strip('\"\' )
            # sometimes starts with 'the fields of'
            # split by commas and 'and'
            parts = re.split(r",| and | & ", seg)
            # clean parts
            cleaned = []
            for p in parts:
                p = p.strip()
                # remove leading 'the' or 'the category of'
                p = re.sub(r"^the ", '', p, flags=re.IGNORECASE)
                # remove trailing words like 'services'
                p = re.sub(r"services$", '', p, flags=re.IGNORECASE).strip()
                # remove surrounding quotes and extra spaces
                p = p.strip(" '\"")
                if p:
                    cleaned.append(p)
            if cleaned:
                return cleaned
    # as fallback, try to extract capitalized phrases after last comma
    # split entire description by commas and take last 6 tokens
    parts = [p.strip().strip("'\"") for p in re.split(r",", desc) if p.strip()]
    # try tokens that look like categories: contain uppercase or ampersand
    candidates = [p for p in parts if re.search(r"[A-Z]|&", p)]
    if candidates:
        # further split last candidate by spaces and limit
        last = candidates[-1]
        subparts = [s.strip() for s in re.split(r",| and | & ", last) if s.strip()]
        return subparts
    return []

bdf['category_list'] = bdf.apply(extract_categories, axis=1)

# Filter businesses accepting credit cards
cc_biz = bdf[bdf['accepts_cc'] == True].copy()

# explode categories
cc_biz_expl = cc_biz.explode('category_list')
cc_biz_expl = cc_biz_expl[cc_biz_expl['category_list'].notna() & (cc_biz_expl['category_list'] != '')]

# count distinct businesses per category
if cc_biz_expl.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    cat_counts = cc_biz_expl.groupby('category_list')['biz_num'].nunique().reset_index()
    cat_counts = cat_counts.rename(columns={'category_list': 'category', 'biz_num': 'business_count'})
    cat_counts = cat_counts.sort_values(['business_count', 'category'], ascending=[False, True])
    top = cat_counts.iloc[0]
    top_cat = top['category']
    top_count = int(top['business_count'])

    # businesses in top category
    biz_nums_in_top = cc_biz_expl[cc_biz_expl['category_list'] == top_cat]['biz_num'].unique().tolist()

    # convert review ratings
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
    revs_top = rdf[rdf['biz_num'].isin(biz_nums_in_top)].copy()
    if revs_top.empty:
        avg_rating = None
    else:
        avg_rating = float(revs_top['rating'].mean())

    result = {'category': top_cat, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WxTjm8yJBKjgiFdZopzR8a8o': 'file_storage/call_WxTjm8yJBKjgiFdZopzR8a8o.json', 'var_call_tV5Ysp0Q7UR4tdGymlUigNb5': 'file_storage/call_tV5Ysp0Q7UR4tdGymlUigNb5.json', 'var_call_6SH0MDadi61uDz9mR8tLuNgV': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_v4PFAHXQgeJFQhadysNlv4rK': 'file_storage/call_v4PFAHXQgeJFQhadysNlv4rK.json'}

exec(code, env_args)
