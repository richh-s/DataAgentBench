code = """import json
import pandas as pd
import re

with open(var_call_ayIoNTe45A1cqrqRRXYS9Pef, 'r') as f:
    businesses = json.load(f)
with open(var_call_JQL7Y5PXp0wYe9As4GOYFNil, 'r') as f:
    reviews = json.load(f)

df_biz = pd.DataFrame(businesses)
if 'attributes' not in df_biz.columns:
    df_biz['attributes'] = None
if 'description' not in df_biz.columns:
    df_biz['description'] = None

# accepts cc
def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            return v.strip().lower() == 'true'
        return False
    if isinstance(attr, str):
        s = attr.lower()
        if 'businessacceptscreditcards' in s and 'true' in s:
            return True
    return False

df_biz['accepts_cc'] = df_biz['attributes'].apply(accepts_cc)

# parse categories from description
def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    s = desc
    # take substring after last ' in '
    if ' in ' in s:
        s = s.rsplit(' in ', 1)[-1]
    # remove trailing sentence fragments after a period
    s = s.split('.',1)[0]
    # remove leading phrases
    s = re.sub(r"^the category of\s*","",s, flags=re.I)
    s = re.sub(r"^the categories of\s*","",s, flags=re.I)
    s = re.sub(r"^the fields of\s*","",s, flags=re.I)
    s = re.sub(r"^the category\s*","",s, flags=re.I)
    s = re.sub(r"^offers a range of services including\s*","",s, flags=re.I)
    s = re.sub(r"^offers a range of services in the fields of\s*","",s, flags=re.I)
    s = re.sub(r"^offers a range of services in\s*","",s, flags=re.I)
    s = re.sub(r"^offers a diverse range of services including\s*","",s, flags=re.I)
    s = re.sub(r"^offering a diverse selection of services including\s*","",s, flags=re.I)
    s = re.sub(r"^offers a diverse selection of\s*","",s, flags=re.I)
    s = re.sub(r"^provides essential services in the categories of\s*","",s, flags=re.I)
    s = re.sub(r"^this .* offers a range of services including\s*","",s, flags=re.I)
    s = re.sub(r"^this .* offers a variety of services including\s*","",s, flags=re.I)

    # replace connecting phrases with comma
    s = re.sub(r"\s+including\s+"," , ", s, flags=re.I)
    s = re.sub(r"\s+ranging from\s+"," , ", s, flags=re.I)
    s = re.sub(r"\s+featuring\s+"," , ", s, flags=re.I)

    # split by commas
    parts = [p.strip() for p in re.split(r",|;", s) if p.strip()]
    tokens = []
    for p in parts:
        # further split by ' & ' and ' and '
        for sub in re.split(r"\s+&\s+|\s+and\s+", p):
            sub = sub.strip().strip('\"').strip("'")
            if sub:
                # remove trailing phrases like 'for all your ...' after comma
                sub = re.split(r"for |to meet |making it|perfect spot|offering|to meet|for any|for all", sub, flags=re.I)[0].strip()
                # ignore short tokens
                if len(sub) > 1:
                    tokens.append(sub)
    # dedupe and return
    seen = []
    out = []
    for t in tokens:
        if t.lower() not in seen:
            seen.append(t.lower())
            out.append(t)
    return out

# Apply extraction
df_biz['categories_parsed'] = df_biz['description'].apply(extract_categories)

# Filter businesses accepting cc
df_cc = df_biz[df_biz['accepts_cc']].copy()
# explode
if not df_cc.empty:
    df_cc = df_cc.explode('categories_parsed')
    df_cc = df_cc[df_cc['categories_parsed'].notna() & (df_cc['categories_parsed']!='')]

# Count unique businesses per category
if df_cc.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    cat_counts = df_cc.groupby('categories_parsed')['business_id'].nunique().reset_index()
    cat_counts = cat_counts.rename(columns={'categories_parsed':'category','business_id':'business_count'})
    cat_counts = cat_counts.sort_values(['business_count','category'], ascending=[False, True])
    top = cat_counts.iloc[0]
    top_cat = top['category']
    top_count = int(top['business_count'])

    # prepare reviews
    df_rev = pd.DataFrame(reviews)
    if 'rating' in df_rev.columns:
        df_rev = df_rev.dropna(subset=['business_ref'])
        df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
        df_rev = df_rev.dropna(subset=['rating'])
        df_rev['business_id'] = df_rev['business_ref'].str.replace('businessref_','businessid_')
        # businesses in top category
        biz_ids_in_cat = df_cc[df_cc['categories_parsed']==top_cat]['business_id'].unique().tolist()
        df_rev_cat = df_rev[df_rev['business_id'].isin(biz_ids_in_cat)].copy()
        if df_rev_cat.empty:
            avg_rating = None
        else:
            avg_rating = float(df_rev_cat['rating'].mean())
    else:
        avg_rating = None

    result = {'category': top_cat, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating,3)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6FU7kBcN06qZSAs1ZtN8NF87': ['business', 'checkin'], 'var_call_omKwTvAxZYsyy8pP1giAqkKq': ['review', 'tip', 'user'], 'var_call_BNfPlXFrji3oZk83tN7Nfhlh': 'file_storage/call_BNfPlXFrji3oZk83tN7Nfhlh.json', 'var_call_JQL7Y5PXp0wYe9As4GOYFNil': 'file_storage/call_JQL7Y5PXp0wYe9As4GOYFNil.json', 'var_call_fuDXv6s8oZ1TPVUnUAbTRzfK': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_jqSVV91gL42GfNSNnOn33Wfq': [], 'var_call_igbnbeaPIBL86oHEcLskL2HR': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_call_ayIoNTe45A1cqrqRRXYS9Pef': 'file_storage/call_ayIoNTe45A1cqrqRRXYS9Pef.json'}

exec(code, env_args)
