code = """import json
biz_ids = [d['business_id'] for d in var_call_YAgws4PmHKq8cZ4ZyN6r7NQM]
ref_ids = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]
result = json.dumps(ref_ids)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_bpmDtofwjroPd8AFC8BZdSe0': [], 'var_call_5tVwatIKZ3qMTBZRDCWyuxUY': ['review', 'tip', 'user'], 'var_call_YAgws4PmHKq8cZ4ZyN6r7NQM': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
