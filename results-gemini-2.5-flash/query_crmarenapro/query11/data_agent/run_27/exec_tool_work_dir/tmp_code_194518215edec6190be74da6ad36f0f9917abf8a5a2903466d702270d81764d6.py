code = """import json
product_details = locals()['var_function-call-9366555752063379231']
ai_products = [p for p in product_details if 'AI Cirku-Tech' in p['Name']]
if ai_products:
    result = ai_products[0]['Id']
else:
    result = 'No AI processing unit found.'
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-3879124646833045278': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}], 'var_function-call-10457068182315660162': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}], 'var_function-call-994363197601446170': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}], 'var_function-call-16483719783789625675': [], 'var_function-call-9366555752063379231': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}]}

exec(code, env_args)
