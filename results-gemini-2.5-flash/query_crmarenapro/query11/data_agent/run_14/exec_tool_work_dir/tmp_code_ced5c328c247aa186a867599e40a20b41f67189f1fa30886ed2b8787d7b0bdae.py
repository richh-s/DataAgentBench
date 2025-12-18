code = """import json

opp_line_items = locals()['var_function-call-10992779700646665931']
product_ids = [item['Product2Id'].lstrip('#') for item in opp_line_items]

print("__RESULT__:")
print(json.dumps(product_ids))"""

env_args = {'var_function-call-3928216419899774128': [{'Id': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_function-call-7868555401100644541': [], 'var_function-call-10992779700646665931': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}], 'var_function-call-15943954160636670431': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}]}

exec(code, env_args)
