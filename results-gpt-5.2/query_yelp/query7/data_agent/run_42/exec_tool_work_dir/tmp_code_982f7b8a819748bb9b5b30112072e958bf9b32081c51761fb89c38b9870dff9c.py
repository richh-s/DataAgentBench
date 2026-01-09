code = """import json, pandas as pd, re

# reviews counts per business_ref
rev = pd.DataFrame(var_call_6Q0U6ZueY8i5hhRoJZS0TRz2)
rev['review_cnt'] = rev['review_cnt'].astype(int)

# load businesses from file
path = var_call_mcEFeeTqnfCASSPWnnpu5aMR
with open(path, 'r') as f:
    biz = json.load(f)
biz_df = pd.DataFrame(biz)

# map businessid -> businessref
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# extract categories list from description after 'including'
cat_re = re.compile(r"including\s+(.*?)(?:\.|$)", re.IGNORECASE|re.DOTALL)

def extract(desc):
    if not isinstance(desc, str):
        return []
    m = cat_re.search(desc)
    if not m:
        return []
    s = m.group(1)
    s = s.replace(' and ', ', ')
    parts = [p.strip(" '\n\t\r\"") for p in s.split(',')]
    parts = [p for p in parts if p]
    return parts

biz_df['categories'] = biz_df['description'].apply(extract)

# join reviews to business categories
joined = rev.merge(biz_df[['business_ref','categories']], on='business_ref', how='left')
joined = joined.explode('categories')
joined = joined.dropna(subset=['categories'])

cat_totals = joined.groupby('categories', as_index=False)['review_cnt'].sum().sort_values('review_cnt', ascending=False)

top5 = cat_totals.head(5).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_fkVQfJocCYjNtW0iShfJNlPF': ['review', 'tip', 'user'], 'var_call_ftLe5gDAXcoJmeC3SJUa18Az': ['checkin', 'business'], 'var_call_6Q0U6ZueY8i5hhRoJZS0TRz2': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}], 'var_call_mcEFeeTqnfCASSPWnnpu5aMR': 'file_storage/call_mcEFeeTqnfCASSPWnnpu5aMR.json'}

exec(code, env_args)
