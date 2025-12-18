code = """import json
product_ids_raw = [item['Product2Id'] for item in locals()['var_function-call-10457068182315660162']]
product_ids = [pid.replace('#', '') for pid in product_ids_raw]
product_names = locals()['var_function-call-994363197601446170']
ai_products = [p for p in product_names if 'AI processing unit' in p['Name']]
ai_product_ids = [p['Id'] for p in ai_products]
print("__RESULT__:")
print(json.dumps(ai_product_ids))"""

env_args = {'var_function-call-3879124646833045278': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}], 'var_function-call-10457068182315660162': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}], 'var_function-call-994363197601446170': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}]}

exec(code, env_args)
