code = """import json
business_ids = locals()['var_function-call-15685058272379338986']['results']
business_refs = [biz['business_id'].replace('businessid_', 'businessref_') for biz in business_ids]
print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-10087123869039632836': [], 'var_function-call-15685058272379338986': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
