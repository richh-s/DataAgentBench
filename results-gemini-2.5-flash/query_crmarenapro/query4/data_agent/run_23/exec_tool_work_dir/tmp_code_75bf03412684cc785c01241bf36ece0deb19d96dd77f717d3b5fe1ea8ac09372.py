code = """import json

order_item_ids_raw_list = locals()['var_function-call-9320036195922497951']['results']
all_order_item_ids = []
for item_str in order_item_ids_raw_list:
    item_data = json.loads(item_str)
    for item_dict in item_data:
        all_order_item_ids.append(item_dict['Id'].replace('#', '').strip())

cleaned_ids_string = ', '.join([f"'{id_}'" for id_ in all_order_item_ids])

print("__RESULT__:")
print(json.dumps(cleaned_ids_string))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
