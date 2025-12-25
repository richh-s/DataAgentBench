code = """import json
products = [r['Product2Id'] for r in var_call_0508Y9FX4wpLDeepQ0pr8qYz]
result = json.dumps(products[0] if products else None)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_9zevBr3guEiKNyWn7t4WUukR': [], 'var_call_0508Y9FX4wpLDeepQ0pr8qYz': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
