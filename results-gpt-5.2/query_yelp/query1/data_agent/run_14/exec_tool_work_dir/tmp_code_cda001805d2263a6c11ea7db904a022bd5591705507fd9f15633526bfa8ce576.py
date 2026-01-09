code = """import json
# business ids from mongo
biz = [r['business_id'] for r in var_call_bkgcqRJ7be2jxn81uOUg5iIa]
# map to businessref_
biz_refs = ['businessref_' + b.split('businessid_',1)[1] for b in biz]
print('__RESULT__:')
print(json.dumps({'biz_refs': biz_refs}))"""

env_args = {'var_call_bkgcqRJ7be2jxn81uOUg5iIa': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
