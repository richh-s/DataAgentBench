code = """import json

raw_string = locals()['var_function-call-16693986522350720468']['results'][0]
start_index = raw_string.find('[')
end_index = raw_string.rfind(']')
json_string = raw_string[start_index : end_index + 1]

order_item_ids_raw = json.loads(json_string)
order_item_ids = [item['Id'].replace('#', '') for item in order_item_ids_raw]

print("__RESULT__:")
print(json.dumps(order_item_ids))"""

env_args = {'var_function-call-13128304760937500599': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-16693986522350720468': [{'Id': '802Wt00000797awIAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
