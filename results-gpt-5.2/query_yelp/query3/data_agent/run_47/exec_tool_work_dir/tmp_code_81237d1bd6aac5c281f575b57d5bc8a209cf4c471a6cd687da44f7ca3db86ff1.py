code = """import json, pandas as pd

# reviews in 2018
rev = pd.DataFrame(var_call_Q6W0zWw9hSFRSePzMUwZlD0z)
rev['business_id'] = rev['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
rev_set = set(rev['business_id'].tolist())

# parking/bikeparking businesses
biz_src = var_call_8LCEoqX020brGMO8AM8W2LaD
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz_records = json.load(f)
else:
    biz_records = biz_src
biz = pd.DataFrame(biz_records)
# some docs might miss business_id
biz_set = set(biz['business_id'].dropna().tolist())

count = len(rev_set.intersection(biz_set))

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_Q6W0zWw9hSFRSePzMUwZlD0z': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}], 'var_call_8LCEoqX020brGMO8AM8W2LaD': 'file_storage/call_8LCEoqX020brGMO8AM8W2LaD.json'}

exec(code, env_args)
