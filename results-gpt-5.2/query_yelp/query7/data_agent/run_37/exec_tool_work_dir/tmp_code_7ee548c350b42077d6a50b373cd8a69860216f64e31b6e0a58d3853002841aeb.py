code = """import json, pandas as pd, re

reviews = pd.DataFrame(var_call_qY2onpghGOmlnFr2Hbjc8NvG)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)

# load businesses from file
path = var_call_Ernku44gSI14YnToml9ha2xa
with open(path, 'r') as f:
    biz = json.load(f)

dfb = pd.DataFrame(biz)

# derive categories from description (since no explicit categories field)
# take the part after 'categories of' or 'including'/'in the categories of'

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    # grab last clause after 'including' or 'categories of'
    m = re.search(r"(?:including|categories of|category of) (.+?)\.?$", desc, flags=re.IGNORECASE)
    if m:
        tail = m.group(1)
    else:
        # fallback: after 'in the fields of'
        m2 = re.search(r"fields of (.+?)\.?$", desc, flags=re.IGNORECASE)
        tail = m2.group(1) if m2 else desc
    # remove location preface if present
    tail = re.sub(r"Located at .*? in .*?, .*?, this (?:business|establishment|facility|store|spot|location) (?:offers|specializes in|provides).*?", "", tail, flags=re.IGNORECASE)
    # split by commas and 'and'
    parts = re.split(r",|\band\b", tail)
    cats = []
    for p in parts:
        c = p.strip().strip("'\"")
        if c:
            cats.append(c)
    return cats

# map business_id -> categories list
# also normalize ids: businessid_X <-> businessref_X

dfb['business_ref'] = dfb['business_id'].str.replace('businessid_', 'businessref_', regex=False)
dfb['categories_list'] = dfb['description'].apply(extract_cats)

# join reviews per business
merged = reviews.merge(dfb[['business_ref','categories_list']], on='business_ref', how='left')
merged = merged[merged['categories_list'].notna()]

# explode categories
expl = merged.explode('categories_list')
expl['category'] = expl['categories_list'].astype(str).str.strip()
expl = expl[expl['category']!='']

cat_totals = expl.groupby('category', as_index=False)['review_cnt'].sum().sort_values('review_cnt', ascending=False)
 топ5 = cat_totals.head(5)

result = топ5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_qY2onpghGOmlnFr2Hbjc8NvG': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_call_Ernku44gSI14YnToml9ha2xa': 'file_storage/call_Ernku44gSI14YnToml9ha2xa.json'}

exec(code, env_args)
