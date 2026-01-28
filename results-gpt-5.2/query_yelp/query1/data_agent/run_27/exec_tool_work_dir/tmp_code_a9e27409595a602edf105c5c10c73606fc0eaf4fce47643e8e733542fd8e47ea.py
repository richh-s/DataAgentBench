code = """import json
biz_in = var_call_TlsZ30p7LiqAwav3j9M2RcTv
biz_ids = sorted({r['business_id'] for r in biz_in if r.get('business_id')})
refs = [bid.replace('businessid_','businessref_') for bid in biz_ids]
res = {'business_ids': biz_ids, 'business_refs': refs, 'n_businesses': len(biz_ids)}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Du7xK8N5X0nR5YAs9XtvsuoJ': [], 'var_call_TlsZ30p7LiqAwav3j9M2RcTv': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
