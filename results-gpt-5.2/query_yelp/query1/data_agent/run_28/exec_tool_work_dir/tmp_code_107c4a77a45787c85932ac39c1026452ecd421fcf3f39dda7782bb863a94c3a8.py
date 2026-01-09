code = """import json
biz = var_call_Xmo9V95FPiDqBwxNKfrJuxWb
refs = ['businessref_' + b['business_id'].split('_',1)[1] for b in biz]
print('__RESULT__:')
print(json.dumps(refs))"""

env_args = {'var_call_TnCTCHlWAzSLzDt7oTZQg3wU': [], 'var_call_Xmo9V95FPiDqBwxNKfrJuxWb': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16'}]}

exec(code, env_args)
