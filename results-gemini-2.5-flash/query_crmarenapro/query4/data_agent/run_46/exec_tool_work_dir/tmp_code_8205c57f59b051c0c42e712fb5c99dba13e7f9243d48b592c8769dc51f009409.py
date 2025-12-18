code = """import json
order_item_ids_raw = json.loads(locals()['var_function-call-2967129351824236084'])
order_item_ids = [item['Id'].lstrip('#') for item in order_item_ids_raw]
print('__RESULT__:')
print(json.dumps(order_item_ids))"""

env_args = {'var_function-call-3721613820015664191': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2967129351824236084': [{'Id': '802Wt00000797awIAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
