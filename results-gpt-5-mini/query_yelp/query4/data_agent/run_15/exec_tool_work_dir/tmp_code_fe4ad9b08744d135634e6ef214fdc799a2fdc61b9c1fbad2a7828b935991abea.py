code = """import json
import pandas as pd

# Load data
with open(var_call_IHWLzyHEHKZ4SOhQUoYli9JT, 'r') as f:
    businesses = json.load(f)
with open(var_call_IfhiaA91o51YlbHgHKpGLQfP, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Determine if business accepts credit cards
def accepts_credit(attrs):
    if not isinstance(attrs, dict):
        return False
    val = attrs.get('BusinessAcceptsCreditCards')
    if val is None:
        return False
    return 'true' in str(val).lower()

bdf['accepts_cc'] = bdf['attributes'].apply(accepts_credit)

# Extract categories from description using simple phrase matching
phrases = [
    'in the categories of',
    'in the category of',
    'offers a range of services in',
    'offers a diverse range of services and products in',
    'offers a delightful array of options ranging from',
    'offers a delightful array of dishes in the category of',
    'offers a range of services including',
    'offers a range of services',
]

def extract_cats(desc, name):
    if not isinstance(desc, str):
        return [name] if isinstance(name, str) else []
    s = desc
    sl = s.lower()
    for p in phrases:
        i = sl.find(p)
        if i != -1:
            part = s[i+len(p):]
            part = part.split('.',1)[0]
            # truncate common trailing phrases
            for end_marker in ['making it', 'to meet', 'to serve', 'to meet all', 'to meet your']:
                em = part.lower().find(end_marker)
                if em != -1:
                    part = part[:em]
            # normalize
            part = part.replace(' & ', ', ')
            part = part.replace("'", '')
            part = part.replace('"', '')
            # split
            tokens = [t.strip() for t in part.replace(';', ',').replace('/', ',').split(',') if t.strip()]
            # further split on ' and '
            final = []
            for tok in tokens:
                for sub in tok.split(' and '):
                    ss = sub.strip()
                    if ss:
                        final.append(ss)
            return final if final else ([name] if isinstance(name, str) else [])
    # fallback: return name as category
    return [name] if isinstance(name, str) else []

bdf['categories_extracted'] = bdf.apply(lambda r: extract_cats(r.get('description'), r.get('name')), axis=1)

# Filter businesses that accept credit cards
cc_biz = bdf[bdf['accepts_cc'] == True].copy()
cc_exp = cc_biz.explode('categories_extracted')
cc_exp = cc_exp[cc_exp['categories_extracted'].notna()]

if cc_exp.empty:
    result = {'top_category': None, 'business_count': 0, 'average_rating': None}
else:
    cc_exp['cat_norm'] = cc_exp['categories_extracted'].apply(lambda x: x.strip())
    counts = cc_exp['cat_norm'].value_counts()
    top_category = counts.index[0]
    biz_count = int(counts.iloc[0])

    # map businessid to businessref
    def to_businessref(bid):
        if not isinstance(bid, str):
            return None
        parts = bid.split('_',1)
        if len(parts) == 2:
            return 'businessref_' + parts[1]
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
