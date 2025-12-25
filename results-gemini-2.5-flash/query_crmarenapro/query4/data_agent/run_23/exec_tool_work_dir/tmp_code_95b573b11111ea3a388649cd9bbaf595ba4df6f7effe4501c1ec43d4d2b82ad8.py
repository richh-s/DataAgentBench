code = """import json

raw_data_string = locals()['var_function-call-9320036195922497951']['results'][0]
list_of_ids_dicts = json.loads(raw_data_string)
cleaned_ids = [f"'{item['Id'].replace('#', '').strip()}'" for item in list_of_ids_dicts]
ids_string = ', '.join(cleaned_ids)

print("__RESULT__:")
print(json.dumps(ids_string))"""

env_args = {'var_function-call-9320036195922497951': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
