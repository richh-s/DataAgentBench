code = """import json

business_ids_raw = locals()['var_function-call-5921860017581175208']
business_refs = [doc['business_id'].replace('businessid_', 'businessref_') for doc in business_ids_raw]
print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7283800389881393766': [], 'var_function-call-5921860017581175208': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
