code = """import json
orderitems = var_call_6XaIWaIrthZbt7Jz2IwwqkSJ
ids = [row['Id'].replace('#','') for row in orderitems]
values = "','".join(ids)
subquery = "SELECT Id FROM OrderItem WHERE REPLACE(Id, '#', '') IN ('" + values + "')"
result = json.dumps(subquery)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_6XaIWaIrthZbt7Jz2IwwqkSJ': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
