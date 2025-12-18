code = """import json

business_ids = [item['business_id'] for item in locals()['var_function-call-4531175142850792158']]
formatted_business_refs = [bid.replace("businessid_", "businessref_") for bid in business_ids]
print('__RESULT__:')
print(json.dumps(formatted_business_refs))"""

env_args = {'var_function-call-6893041925084802419': [], 'var_function-call-4531175142850792158': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
