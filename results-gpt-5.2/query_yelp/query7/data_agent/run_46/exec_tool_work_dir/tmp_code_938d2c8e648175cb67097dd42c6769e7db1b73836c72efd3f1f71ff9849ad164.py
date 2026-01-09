code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_tMphjg23Egi6BS3HOupjyYd3)
reviews['review_cnt'] = reviews['review_cnt'].astype(int)
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

path = var_call_YsoLp0P6vWAUC7h6SA8EQlG2
with open(path, 'r') as f:
    biz = pd.DataFrame(json.load(f))

# derive a proxy 'category' from business attributes keys (dataset lacks explicit categories)
# each review is counted once for each attribute-key present on the reviewed business
biz['attr_keys'] = biz['attributes'].apply(lambda a: list(a.keys()) if isinstance(a, dict) else [])

merged = reviews.merge(biz[['business_id','attr_keys']], on='business_id', how='left')

data = []
for _, row in merged.iterrows():
    cnt = int(row['review_cnt'])
    for k in (row['attr_keys'] or []):
        data.append((k, cnt))

cat = pd.DataFrame(data, columns=['category','total_reviews'])
res = (cat.groupby('category', as_index=False)['total_reviews'].sum()
          .sort_values(['total_reviews','category'], ascending=[False, True])
          .head(5))

answer = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_9H2reTIMIn4cvaakBwjuCq63': ['review', 'tip', 'user'], 'var_call_nWrESKCOWfXN7ZXw59jlLFVc': ['business', 'checkin'], 'var_call_tMphjg23Egi6BS3HOupjyYd3': [{'business_ref': 'businessref_79', 'review_cnt': '3'}, {'business_ref': 'businessref_13', 'review_cnt': '2'}, {'business_ref': 'businessref_44', 'review_cnt': '2'}, {'business_ref': 'businessref_21', 'review_cnt': '1'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_82', 'review_cnt': '1'}, {'business_ref': 'businessref_9', 'review_cnt': '1'}, {'business_ref': 'businessref_25', 'review_cnt': '1'}, {'business_ref': 'businessref_29', 'review_cnt': '1'}, {'business_ref': 'businessref_39', 'review_cnt': '1'}, {'business_ref': 'businessref_15', 'review_cnt': '2'}, {'business_ref': 'businessref_67', 'review_cnt': '1'}, {'business_ref': 'businessref_96', 'review_cnt': '1'}, {'business_ref': 'businessref_3', 'review_cnt': '1'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_37', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '2'}, {'business_ref': 'businessref_16', 'review_cnt': '1'}, {'business_ref': 'businessref_40', 'review_cnt': '1'}], 'var_call_YsoLp0P6vWAUC7h6SA8EQlG2': 'file_storage/call_YsoLp0P6vWAUC7h6SA8EQlG2.json'}

exec(code, env_args)
