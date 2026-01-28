code = """import json
biz = var_call_wAIeEf89KFRN19GMVKvUgyV9
biz_refs = [b['business_id'].replace('businessid_','businessref_',1) for b in biz]
q = "SELECT AVG(rating) AS avg_rating FROM review WHERE business_ref IN (" + ",".join(["'"+x+"'" for x in biz_refs]) + ");"
print('__RESULT__:')
print(json.dumps({'biz_refs': biz_refs, 'sql': q}))"""

env_args = {'var_call_wAIeEf89KFRN19GMVKvUgyV9': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
