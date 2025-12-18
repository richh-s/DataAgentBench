code = """import json
business_ids_raw = locals()['var_function-call-11448420745239119650']
business_refs = [doc['business_id'].replace('businessid_', 'businessref_') for doc in business_ids_raw]
print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-2550558945733750297': [], 'var_function-call-11448420745239119650': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
