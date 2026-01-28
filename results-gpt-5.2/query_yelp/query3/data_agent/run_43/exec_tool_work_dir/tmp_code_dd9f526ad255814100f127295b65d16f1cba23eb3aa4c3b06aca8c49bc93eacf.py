code = """import json, pandas as pd
rev_biz = pd.DataFrame(var_call_ZmPOlUd2TN4O4qh7vzbk39PS)
park_biz = pd.DataFrame(var_call_fSrnV1aHVcKj5L0dF9ZehNdw)
if rev_biz.empty or park_biz.empty:
    count = 0
else:
    count = int(pd.merge(rev_biz, park_biz, on='business_id', how='inner')['business_id'].nunique())
print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_fSrnV1aHVcKj5L0dF9ZehNdw': [{'business_id': 'businessid_83'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_17'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_37'}], 'var_call_ZmPOlUd2TN4O4qh7vzbk39PS': [{'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}]}

exec(code, env_args)
