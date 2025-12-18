code = """import json
business_refs = locals()['var_function-call-15969302131400067117']
business_ids = [item['business_ref'].replace('businessref_', 'businessid_') for item in business_refs]
print('__RESULT__:')
print(json.dumps(business_ids))"""

env_args = {'var_function-call-15969302131400067117': [{'business_ref': 'businessref_44'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_6'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_29'}, {'business_ref': 'businessref_81'}, {'business_ref': 'businessref_33'}, {'business_ref': 'businessref_60'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_56'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_10'}, {'business_ref': 'businessref_76'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_18'}, {'business_ref': 'businessref_25'}]}

exec(code, env_args)
