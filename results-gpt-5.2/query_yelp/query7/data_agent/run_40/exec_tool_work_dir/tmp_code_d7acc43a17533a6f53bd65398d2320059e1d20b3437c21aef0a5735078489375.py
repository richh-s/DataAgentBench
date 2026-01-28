code = """import json, pandas as pd, re

rev = pd.DataFrame(var_call_fQqTFz5ahRjS0U8MREcKYCwa)
rev['review_count'] = pd.to_numeric(rev['review_count'])

biz_data = var_call_4iP5Sy6dK0kJE5PWfrhEGIA6
if isinstance(biz_data, str):
    with open(biz_data, 'r') as f:
        biz_records = json.load(f)
else:
    biz_records = biz_data
biz = pd.DataFrame(biz_records)

pattern1 = re.compile(r"services? in (.+?)\.")
pattern2 = re.compile(r"categories? of (.+?)\.")

def extract_categories(desc):
    if desc is None:
        return []
    m = pattern1.search(desc)
    if not m:
        m = pattern2.search(desc)
    if not m:
        return []
    s = m.group(1)
    s = s.replace('including ', '')
    parts = [p.strip() for p in s.split(',')]
    out = []
    for p in parts:
        if p:
            out.append(p.strip("'\""))
    return out

biz['categories_list'] = biz['description'].apply(extract_categories)
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

merged = rev.merge(biz[['business_ref','categories_list']], on='business_ref', how='left')
merged = merged.explode('categories_list').dropna(subset=['categories_list'])
merged['category'] = merged['categories_list'].astype(str).str.strip()

cat_counts = merged.groupby('category', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)

top5 = cat_counts.head(5).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_fQqTFz5ahRjS0U8MREcKYCwa': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}], 'var_call_4iP5Sy6dK0kJE5PWfrhEGIA6': 'file_storage/call_4iP5Sy6dK0kJE5PWfrhEGIA6.json'}

exec(code, env_args)
