code = """import json
ops = var_call_YQ3ajx2G8I93dx6GIjvzk6y2
# Select the most recent opportunity (already ordered desc by CloseDate) and first matching product line
product_id = ops[0]['Product2Id'] if ops else None
result = json.dumps(product_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_YQ3ajx2G8I93dx6GIjvzk6y2': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '#01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hTUkIAM', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV9xIAE', 'CloseDate': '2021-06-15'}], 'var_call_SXoXVJ74JRBoMmnm6sxJQGpD': []}

exec(code, env_args)
