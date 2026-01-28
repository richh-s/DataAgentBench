code = """import json, pandas as pd, re

reviews = pd.DataFrame(var_call_W6mxKqy01W6Lb9hpl2insujk)
# coerce counts
reviews['review_cnt'] = reviews['review_cnt'].astype(int)

# load businesses from file
path = var_call_nmZg6KqsBiwtAZi0OxaZXIdQ
with open(path, 'r') as f:
    businesses = json.load(f)

biz_df = pd.DataFrame(businesses)

# derive business_ref from business_id
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# extract categories from description as comma-separated list after 'including'
# Many descriptions end with 'including ...' or 'in ...' and list categories separated by commas, sometimes with 'and'.
# We'll extract the last clause after 'including' if present else after 'in the categories of' else after 'in the category of' else after 'in the fields of' else after 'in' near end.

def extract_cat_list(desc):
    if desc is None:
        return []
    d = desc
    patterns = [
        r"including (.+?)\.?$",
        r"in the categories of (.+?)\.?$",
        r"in the category of (.+?)\.?$",
        r"in the fields of (.+?)\.?$",
        r"in (?:the )?categories? of (.+?)\.?$",
    ]
    m = None
    for p in patterns:
        m = re.search(p, d, flags=re.IGNORECASE)
        if m:
            s = m.group(1)
            break
    if not m:
        # try after 'offers' last 'in'
        m2 = re.search(r"offers (?:a|an|the)? ?(?:range|variety|diverse (?:menu|selection)|selection|mix|array) of (?:services|dishes|options|products)?(?: in)? (.+?)\.?$", d, flags=re.IGNORECASE)
        if m2:
            s = m2.group(1)
        else:
            return []
    s = s.strip()
    # remove leading filler
    s = re.sub(r"^(?:a )?range of services (?:in )?", "", s, flags=re.IGNORECASE)
    # replace ' and ' with ', '
    s = re.sub(r"\s+and\s+", ", ", s)
    # split by comma
    cats = [c.strip().strip("'\"") for c in s.split(',')]
    # filter empties
    cats = [c for c in cats if c]
    return cats

biz_df['categories_list'] = biz_df['description'].apply(extract_cat_list)

# join reviews to businesses
merged = reviews.merge(biz_df[['business_ref','categories_list']], on='business_ref', how='left')
merged = merged[merged['categories_list'].notna()]

# explode categories
expl = merged.explode('categories_list')
expl = expl[expl['categories_list'].notna() & (expl['categories_list']!='')]

cat_counts = expl.groupby('categories_list', as_index=False)['review_cnt'].sum()
cat_counts = cat_counts.sort_values(['review_cnt','categories_list'], ascending=[False, True]).head(5)

result = cat_counts.rename(columns={'categories_list':'category','review_cnt':'total_reviews'}).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_W6mxKqy01W6Lb9hpl2insujk': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}], 'var_call_nmZg6KqsBiwtAZi0OxaZXIdQ': 'file_storage/call_nmZg6KqsBiwtAZi0OxaZXIdQ.json'}

exec(code, env_args)
