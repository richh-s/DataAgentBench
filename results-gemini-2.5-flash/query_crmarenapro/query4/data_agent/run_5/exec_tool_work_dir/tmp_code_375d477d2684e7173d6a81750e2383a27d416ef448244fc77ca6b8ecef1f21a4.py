code = """import json
order_item_ids_str = locals()['var_function-call-12731424350234165751']["order_item_ids_str"]
query = "SELECT createddate FROM \"Case\" WHERE orderitemid__c IN (" + order_item_ids_str + ");"
print("__RESULT__:")
print(json.dumps({"query": query}))"""

env_args = {'var_function-call-17198506161418644478': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-12731424350234165751': {'order_item_ids_str': "'802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797z7IAA', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt0000079B0EIAU'"}}

exec(code, env_args)
