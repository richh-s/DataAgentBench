code = """import json, pandas as pd, re

# load reviews per business
reviews = pd.DataFrame(var_call_0nSvkAlkOF9Y7xBnJHr1rVfT)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)

# load businesses from json file
path = var_call_tcDnqCMYumjIQGbBf764O60m
with open(path, 'r') as f:
    biz = pd.DataFrame(json.load(f))

# derive business_ref from business_id
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# extract categories list from description if categories field absent

def extract_cats(desc):
    if desc is None:
        return []
    m = re.search(r"providing a range of services in (.+?)\.|offers a (?:diverse|wide) (?:range|selection) of (?:services|products) in (?:the )?categories? of (.+?)\.|offers a delightful array of dishes in the category of '(.+?)'\.|offers a delightful selection of treats, making it a must-visit for anyone seeking (.+?)\.|specializes in a variety of offerings, including (.+?), making it|offers a diverse menu featuring (.+?) cuisine|offers a diverse menu featuring (.+?)\,|offers a delightful mix of (.+?)\, perfect|offers a tempting selection of treats in the categories of (.+?)\.|offers a range of services including (.+?)\.|specializes in (.+?)\, providing|specializes in a range of offerings within the (.+?) categories|specializes in (.+?)\.|offers enthusiasts a premier destination for (.+?)\.|This .* location offers a range of services including (.+?) to meet|This .* location offers a range of services including (.+?)\.|offers essential services in the categories of (.+?)\.|specializes in Optometrists, (.+?)\.|offers a range of services for animal lovers, including (.+?)\.|offers a delightful selection of fresh catches.*making it a go-to destination for (.+?)\,", desc)
    text = None
    if m:
        for g in m.groups():
            if g:
                text = g
                break
    if not text:
        return []
    # split by comma and strip
    cats = [c.strip().strip("'") for c in text.split(',')]
    cats = [c for c in cats if c]
    return cats

if 'categories' in biz.columns:
    biz['cat_list'] = biz['categories'].apply(lambda x: x if isinstance(x, list) else ([] if x is None else [x]))
else:
    biz['cat_list'] = biz['description'].apply(extract_cats)

# join and explode categories
merged = reviews.merge(biz[['business_ref','cat_list']], on='business_ref', how='left')
merged = merged.explode('cat_list')
merged = merged.dropna(subset=['cat_list'])
merged['category'] = merged['cat_list'].astype(str)

cat_totals = (merged.groupby('category', as_index=False)['review_cnt']
             .sum()
             .sort_values(['review_cnt','category'], ascending=[False, True])
             .head(5))

result = cat_totals.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0nSvkAlkOF9Y7xBnJHr1rVfT': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_call_tcDnqCMYumjIQGbBf764O60m': 'file_storage/call_tcDnqCMYumjIQGbBf764O60m.json'}

exec(code, env_args)
