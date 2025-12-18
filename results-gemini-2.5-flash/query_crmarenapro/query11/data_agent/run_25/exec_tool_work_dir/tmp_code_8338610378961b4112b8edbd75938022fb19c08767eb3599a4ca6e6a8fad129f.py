code = """product_ids = [item['Product2Id'] for item in locals()['var_function-call-13147432442458377202']]
import json
print("__RESULT__:")
print(json.dumps(product_ids))"""

env_args = {'var_function-call-7926429916752409643': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_function-call-9062097568578308463': [], 'var_function-call-1498617034454450845': [], 'var_function-call-17708119103426819696': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}], 'var_function-call-13147432442458377202': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
