code = """result = locals()['var_function-call-10986507755673810533']
product_ids = [item['Id'] for item in result]
print("__RESULT__:")
print(product_ids)"""

env_args = {'var_function-call-16373558783057992797': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}], 'var_function-call-8412187715708029270': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}], 'var_function-call-10986507755673810533': [{'Name': 'CloudLink Designer', 'Id': '01tWt000006hTUkIAM'}]}

exec(code, env_args)
