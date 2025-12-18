code = """import json
order_item_ids_data = locals()['var_function-call-9728789747611125872']
order_item_ids = [item['Id'].replace("#", "") for item in order_item_ids_data]
order_item_ids_str = json.dumps(order_item_ids)
print("__RESULT__:")
print(order_item_ids_str)"""

env_args = {'var_function-call-479248216998820960': [], 'var_function-call-2775121335105051301': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-9728789747611125872': [{'Id': '802Wt00000797awIAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
