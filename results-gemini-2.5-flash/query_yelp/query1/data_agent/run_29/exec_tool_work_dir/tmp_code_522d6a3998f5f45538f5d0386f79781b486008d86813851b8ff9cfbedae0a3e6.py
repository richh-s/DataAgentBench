code = """import json
business_ids = [b['business_id'] for b in locals()['var_function-call-15598127334447935087']]
business_refs = [b.replace('businessid_', 'businessref_') for b in business_ids]
print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-5413465879172214691': [], 'var_function-call-15598127334447935087': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
