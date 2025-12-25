code = """import json
order_item_ids = [item["cleaned_order_item_id"] for item in locals()['var_function-call-6751001765798742146']]
print("__RESULT__:")
print(json.dumps(order_item_ids))"""

env_args = {'var_function-call-6751001765798742146': [{'cleaned_order_item_id': '802Wt0000078yuGIAQ'}, {'cleaned_order_item_id': '802Wt00000790mOIAQ'}, {'cleaned_order_item_id': '802Wt00000790zGIAQ'}, {'cleaned_order_item_id': '802Wt00000794F2IAI'}, {'cleaned_order_item_id': '802Wt000007968eIAA'}, {'cleaned_order_item_id': '802Wt00000796bfIAA'}, {'cleaned_order_item_id': '802Wt00000796qFIAQ'}, {'cleaned_order_item_id': '802Wt0000079734IAA'}, {'cleaned_order_item_id': '802Wt00000797W5IAI'}, {'cleaned_order_item_id': '802Wt00000797awIAA'}, {'cleaned_order_item_id': '802Wt00000797z7IAA'}, {'cleaned_order_item_id': '802Wt00000798VPIAY'}, {'cleaned_order_item_id': '802Wt00000798YdIAI'}, {'cleaned_order_item_id': '802Wt00000798okIAA'}, {'cleaned_order_item_id': '802Wt00000799o1IAA'}, {'cleaned_order_item_id': '802Wt0000079A2bIAE'}, {'cleaned_order_item_id': '802Wt0000079ACGIA2'}, {'cleaned_order_item_id': '802Wt0000079B0EIAU'}, {'cleaned_order_item_id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
