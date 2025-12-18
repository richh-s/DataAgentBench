code = """import json
product_ids_from_opportunities = [item['Product2Id'].replace('#', '') for item in locals()['var_function-call-2894929541924962912']]
product_ids_from_opportunities_str = ', '.join(f"'{id}'" for id in product_ids_from_opportunities)
print("__RESULT__:")
print(json.dumps(product_ids_from_opportunities_str))"""

env_args = {'var_function-call-11055127628110594963': [], 'var_function-call-8732559206158722235': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}], 'var_function-call-2894929541924962912': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
