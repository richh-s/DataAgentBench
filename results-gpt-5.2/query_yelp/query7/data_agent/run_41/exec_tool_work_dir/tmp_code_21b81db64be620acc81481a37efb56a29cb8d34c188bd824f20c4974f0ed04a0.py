code = """import json, pandas as pd

# reviews per business_ref
reviews = pd.DataFrame(var_call_gipmapO1KFOjT0eKMzcv6heZ)
reviews['review_count'] = reviews['review_count'].astype(int)

# load businesses attributes from json file
path = var_call_mVO13Y2jUnCrL9V2jF0OU4IQ
with open(path, 'r') as f:
    biz = json.load(f)
biz_df = pd.DataFrame(biz)

# map businessid_ -> businessref_
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# determine category field; dataset doesn't include explicit categories, so use attributes key 'categories' if present
# If not present, cannot compute true categories.

def extract_categories(attrs):
    if attrs is None or attrs == 'None':
        return []
    if isinstance(attrs, dict):
        for k in ['categories', 'Categories', 'category', 'Category']:
            if k in attrs and attrs[k] not in (None, 'None'):
                v = attrs[k]
                if isinstance(v, str):
                    return [c.strip() for c in v.split(',') if c.strip()]
                if isinstance(v, list):
                    return [str(c).strip() for c in v if str(c).strip()]
        return []
    return []

biz_df['categories'] = biz_df['attributes'].apply(extract_categories)

merged = reviews.merge(biz_df[['business_ref','categories']], on='business_ref', how='left')
merged = merged.explode('categories')
merged = merged[merged['categories'].notna() & (merged['categories']!='')]

if merged.empty:
    result = {"error":"No business category field found in business collection (attributes lacks categories). Cannot compute requested top categories with provided schema."}
else:
    top = (merged.groupby('categories', as_index=False)['review_count'].sum()
           .sort_values(['review_count','categories'], ascending=[False, True])
           .head(5))
    result = top.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_gipmapO1KFOjT0eKMzcv6heZ': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}], 'var_call_mVO13Y2jUnCrL9V2jF0OU4IQ': 'file_storage/call_mVO13Y2jUnCrL9V2jF0OU4IQ.json'}

exec(code, env_args)
