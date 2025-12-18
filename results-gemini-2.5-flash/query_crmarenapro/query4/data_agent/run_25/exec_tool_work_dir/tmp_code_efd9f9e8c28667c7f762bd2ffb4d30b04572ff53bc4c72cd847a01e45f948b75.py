code = """import json
order_item_ids_data = locals()['var_function-call-16823494873582588358']
order_item_ids = [item['Id'].replace('#', '') for item in order_item_ids_data]
print("__RESULT__:")
print(json.dumps(order_item_ids))"""

env_args = {'var_function-call-12698488873756692077': [], 'var_function-call-17723242976830367418': [], 'var_function-call-13408978245398052268': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-16823494873582588358': [{'Id': '802Wt00000797awIAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
