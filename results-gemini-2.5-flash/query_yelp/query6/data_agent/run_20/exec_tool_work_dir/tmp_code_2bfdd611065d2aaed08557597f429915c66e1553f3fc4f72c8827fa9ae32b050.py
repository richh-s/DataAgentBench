code = """import json

result = locals()['var_function-call-5427749435601098103'][0]
business_ref = result['business_ref']
business_id = business_ref.replace('businessref_', 'businessid_')

print('__RESULT__:')
print(json.dumps(business_id))"""

env_args = {'var_function-call-5427749435601098103': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}]}

exec(code, env_args)
