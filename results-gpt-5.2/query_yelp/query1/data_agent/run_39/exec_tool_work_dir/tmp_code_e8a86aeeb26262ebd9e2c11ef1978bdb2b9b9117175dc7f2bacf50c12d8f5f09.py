code = """import json
biz = var_call_DeNuGAQcHBuRWCnWmLrkuGMv
bizrefs = [b['business_id'].replace('businessid_','businessref_') for b in biz]
print('__RESULT__:')
print(json.dumps({'bizrefs': bizrefs, 'n': len(bizrefs)}))"""

env_args = {'var_call_DeNuGAQcHBuRWCnWmLrkuGMv': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
