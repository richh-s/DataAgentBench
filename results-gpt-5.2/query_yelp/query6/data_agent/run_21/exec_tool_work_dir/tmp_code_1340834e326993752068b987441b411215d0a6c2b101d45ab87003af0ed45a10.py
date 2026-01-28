code = """import json, pandas as pd

# top business from reviews query
rev = pd.DataFrame(var_call_NnWZdbWfGHD4FiGAXvK4x62P)
rev['avg_rating'] = rev['avg_rating'].astype(float)
rev['review_cnt'] = rev['review_cnt'].astype(int)
rev['business_num'] = rev['business_ref'].str.replace('businessref_','', regex=False)
rev['business_id'] = 'businessid_' + rev['business_num']

# load business collection full result from file
path = var_call_yQbzpnoaGFp0ZdJRegTFtr9B
with open(path, 'r', encoding='utf-8') as f:
    biz_records = json.load(f)
biz = pd.DataFrame(biz_records)

out = rev.merge(biz, on='business_id', how='left')

# derive category from description: take text after 'services in' or 'categories of'
import re

def extract_category(desc):
    if desc is None:
        return None
    m = re.search(r"services in (.*?)(?:\.|$)", desc)
    if m:
        return m.group(1).strip()
    m = re.search(r"categories of (.*?)(?:\.|$)", desc)
    if m:
        return m.group(1).strip().strip("\"")
    return None

out['category'] = out['description'].apply(extract_category)

best = out.sort_values(['avg_rating','review_cnt'], ascending=[False, False]).head(1)
ans = {
    'business_id': best.iloc[0]['business_id'],
    'business_ref': best.iloc[0]['business_ref'],
    'name': best.iloc[0].get('name'),
    'avg_rating': float(best.iloc[0]['avg_rating']),
    'review_count_in_period': int(best.iloc[0]['review_cnt']),
    'category': best.iloc[0].get('category')
}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_NnWZdbWfGHD4FiGAXvK4x62P': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_yQbzpnoaGFp0ZdJRegTFtr9B': 'file_storage/call_yQbzpnoaGFp0ZdJRegTFtr9B.json'}

exec(code, env_args)
