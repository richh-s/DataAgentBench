code = """import json

order_item_ids = [item["Id"].replace("#", "") for item in locals()["var_function-call-13759682269694555835"]]
query_ids = ", ".join([f"''{item}''" for item in order_item_ids])

print("__RESULT__:")
print(json.dumps(query_ids))"""

env_args = {'var_function-call-13759682269694555835': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-14808374270237099884': "'''802Wt0000078yuGIAQ''', '''802Wt00000790mOIAQ''', '''802Wt00000790zGIAQ''', '''802Wt00000794F2IAI''', '''802Wt000007968eIAA''', '''802Wt00000796bfIAA''', '''802Wt00000796qFIAQ''', '''802Wt0000079734IAA''', '''802Wt00000797W5IAI''', '''802Wt00000797z7IAA''', '''802Wt00000798YdIAI''', '''802Wt00000798okIAA''', '''802Wt0000079B0EIAU'''"}

exec(code, env_args)
