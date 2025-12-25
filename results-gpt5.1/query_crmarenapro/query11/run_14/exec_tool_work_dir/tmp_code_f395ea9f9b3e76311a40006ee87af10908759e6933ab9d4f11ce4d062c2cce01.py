code = """import json
products = [r['CleanProductId'] for r in var_call_AGU2s3wt7fLoUmQ1AchOdT5k]
result = json.dumps(products)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_WlILBG3Bb9bpD5BaWYpmkpRP': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '#01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hTUkIAM', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV9xIAE', 'CloseDate': '2021-06-15'}], 'var_call_W7SsozVfb5MQe4sy30VSb6f6': [], 'var_call_AGU2s3wt7fLoUmQ1AchOdT5k': [{'CleanProductId': '01tWt000006hV8LIAU'}, {'CleanProductId': '01tWt000006hV9xIAE'}, {'CleanProductId': '01tWt000006hTUkIAM'}]}

exec(code, env_args)
