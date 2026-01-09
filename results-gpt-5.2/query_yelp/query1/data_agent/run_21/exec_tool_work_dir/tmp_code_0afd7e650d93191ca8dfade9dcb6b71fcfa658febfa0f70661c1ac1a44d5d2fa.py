code = """import json
biz = var_call_K8sMeSa1ORCK1SqSwgNGu3p0
bizrefs = [b['business_id'].replace('businessid_','businessref_') for b in biz]
print('__RESULT__:')
print(json.dumps({'bizrefs': bizrefs}))"""

env_args = {'var_call_K8sMeSa1ORCK1SqSwgNGu3p0': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
