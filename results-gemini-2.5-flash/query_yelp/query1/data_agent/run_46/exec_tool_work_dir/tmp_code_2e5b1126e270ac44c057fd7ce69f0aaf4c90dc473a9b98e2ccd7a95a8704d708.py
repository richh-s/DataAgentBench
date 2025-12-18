code = """import json
result = locals()['var_function-call-14448117414862870801'][0]['avg(rating)']
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-2550558945733750297': [], 'var_function-call-11448420745239119650': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}], 'var_function-call-16555381942365469782': ['businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65'], 'var_function-call-14448117414862870801': [{'avg(rating)': '3.86046511627907'}]}

exec(code, env_args)
