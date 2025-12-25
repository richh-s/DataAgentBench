code = """import json

order_item_ids_raw = locals()['var_function-call-13606805687795022908']
order_item_ids = [item['Id'].strip('# ') for item in order_item_ids_raw]

# Prepare the list of IDs for the SQL query
id_list_with_hash = ["#{item}" for item in order_item_ids]
id_list_without_hash = [f"{item}" for item in order_item_ids]

combined_id_list = id_list_with_hash + id_list_without_hash

id_query_string = ", ".join([f"'{item}'" for item in combined_id_list])


print("__RESULT__:")
print(json.dumps(id_query_string))"""

env_args = {'var_function-call-13606805687795022908': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
