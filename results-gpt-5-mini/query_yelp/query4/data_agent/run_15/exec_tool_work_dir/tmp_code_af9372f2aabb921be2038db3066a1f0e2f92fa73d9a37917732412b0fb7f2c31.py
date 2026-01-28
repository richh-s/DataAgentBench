code = """import json
import pandas as pd
import re

# Load data
with open(var_call_IHWLzyHEHKZ4SOhQUoYli9JT, 'r') as f:
    businesses = json.load(f)
with open(var_call_IfhiaA91o51YlbHgHKpGLQfP, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Function to extract categories from description
patterns = [
    r"in the categories of (.+)$",
    r"in the category of (.+)$",
    r"offers a range of services in (.+)$",
    r"offers a diverse range of services and products in (.+)$",
    r"offers a delightful array of options ranging from (.+)$",
    r"offers a delightful array of dishes in the category of (.+)$",
    r"this .* offers a range of services including (.+)$",
    r"this .* offers a range of services (.+)$",
    r"offers a range of services including (.+)$",
]

def extract_from_description(desc):
    if not isinstance(desc, str):
        return []
    s = desc
    # consider only the part after the keyword and before a sentence end or 'making' or 'to meet' or 'to' phrases
    for pat in patterns:
        m = re.search(pat, s, flags=re.IGNORECASE)
        if m:
            part = m.group(1)
            # truncate at first period
            part = part.split('.')[0]
            # truncate at 'making it' or 'to meet' or 'to' followed by words like 'all your' etc
            part = re.split(r"making it|to meet|to provide|to serve|to meet all|to meet your|,? making it|\bto\b", part, flags=re.IGNORECASE)[0]
            # replace connectors like 'and', '&' with comma
            part = part.replace(' & ', ', ')
            part = part.replace(' &', ',')
            # split by commas
            items = [x.strip().strip("'\"") for x in re.split(r",|;|/|\\band\\b|\\b&\\b", part) if x.strip()]
            # further split on ' and '
            final = []
            for it in items:
                sub = re.split(r"\band\b", it)
                for s2 in sub:
                    s3 = s2.strip()
                    if s3:
                        final.append(s3)
            return final
    return []

bdf['categories_extracted'] = bdf['description'].apply(extract_from_description)

# Also try to extract from name if nothing
bdf.loc[bdf['categories_extracted'].apply(lambda x: len(x)==0), 'categories_extracted'] = bdf.loc[bdf['categories_extracted'].apply(lambda x: len(x)==0), 'name'].apply(lambda x: [x] if isinstance(x,str) else [])

# Determine businesses that accept credit cards
def accepts_credit(attrs):
    if not isinstance(attrs, dict):
        return False
    val = attrs.get('BusinessAcceptsCreditCards')
    if val is None:
        return False
    s = str(val)
    return 'true' in s.lower()

bdf['accepts_cc'] = bdf['attributes'].apply(accepts_credit)
cc = bdf[bdf['accepts_cc'] == True].copy()

# explode categories
cc_exp = cc.explode('categories_extracted')
cc_exp = cc_exp[cc_exp['categories_extracted'].notna()]

# normalize category names
cc_exp['cat_norm'] = cc_exp['categories_extracted'].apply(lambda x: x.strip())

if cc_exp.empty:
    result = {'top_category': None, 'business_count': 0, 'average_rating': None}
else:
    counts = cc_exp['cat_norm'].value_counts()
    top_category = counts.index[0]
    biz_count = int(counts.iloc[0])

    # map businessid to businessref
    def to_businessref(bid):
        if not isinstance(bid, str):
            return None
        parts = bid.split('_',1)
        if len(parts)==2:
            return 'businessref_'+parts[1]
        return None

    top_biz_ids = cc_exp[cc_exp['cat_norm'] == top_category]['business_id'].unique()
    top_biz_refs = set([to_businessref(b) for b in top_biz_ids if to_businessref(b)])

    # compute average rating
    if rdf.empty:
        avg_rating = None
    else:
        rdf = rdf[rdf['business_ref'].notna() & rdf['rating'].notna()]
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
        sel = rdf[rdf['business_ref'].isin(top_biz_refs)]
        if sel.empty:
            avg_rating = None
        else:
            avg_rating = float(sel['rating'].mean())

    result = {'top_category': top_category, 'business_count': biz_count, 'average_rating': avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Cg65ZFW3PzhemgDYJz86wogR': ['checkin', 'business'], 'var_call_dlwQ63ehFVPelzf5TTRSOp3r': ['review', 'tip', 'user'], 'var_call_351upF9ajrDuDXdWaZJ20Gro': 'file_storage/call_351upF9ajrDuDXdWaZJ20Gro.json', 'var_call_IfhiaA91o51YlbHgHKpGLQfP': 'file_storage/call_IfhiaA91o51YlbHgHKpGLQfP.json', 'var_call_F8D84ASXCIhAgxhjEu5JbWJQ': {'top_category': None, 'business_count': 0, 'average_rating': None}, 'var_call_IHWLzyHEHKZ4SOhQUoYli9JT': 'file_storage/call_IHWLzyHEHKZ4SOhQUoYli9JT.json', 'var_call_JdiXL6BhYzZ2AS0nDCLDWk6m': []}

exec(code, env_args)
