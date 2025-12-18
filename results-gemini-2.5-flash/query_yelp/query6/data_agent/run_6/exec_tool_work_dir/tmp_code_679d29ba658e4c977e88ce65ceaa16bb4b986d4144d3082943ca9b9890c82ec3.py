code = """import json
parsed_result = json.loads(locals()['var_function-call-15883378990604638904']['results'][0])
business_ref = parsed_result[0]['business_ref']
business_id = 'businessid_' + business_ref.split('_')[1]
print('__RESULT__:')
print(json.dumps(business_id))"""

env_args = {'var_function-call-15883378990604638904': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}]}

exec(code, env_args)
