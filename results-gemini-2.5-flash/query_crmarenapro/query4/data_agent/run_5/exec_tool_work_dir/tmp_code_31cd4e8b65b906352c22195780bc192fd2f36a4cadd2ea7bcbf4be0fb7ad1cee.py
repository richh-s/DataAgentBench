code = """import json
order_item_ids = [d["Id"] for d in locals()['var_function-call-17198506161418644478']]
cleaned_order_item_ids = [f"'{item.lstrip("#").strip()}'" for item in order_item_ids]
order_item_ids_str = ", ".join(cleaned_order_item_ids)
print("__RESULT__:")
print(json.dumps({"order_item_ids_str": order_item_ids_str}))"""

env_args = {'var_function-call-17198506161418644478': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
