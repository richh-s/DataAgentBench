code = """import json

citing_assignees_info = locals()['var_function-call-3658823678110237683']

cpc_codes = set()
for item in citing_assignees_info:
    cpc_codes.add(item['cpc_code'])

print('__RESULT__:')
print(json.dumps(list(cpc_codes)))"""

env_args = {'var_function-call-13930125777228040085': ['publicationinfo'], 'var_function-call-1621381890062432431': [], 'var_function-call-10802364016398363406': [], 'var_function-call-13532911310427381018': 'file_storage/function-call-13532911310427381018.json', 'var_function-call-10059552934646644970': ['US-6767662-B2', 'US-9061071-B2', 'US-11376346-B2', 'US-6750960-B2', 'US-11546022-B2', 'US-11667770-B2'], 'var_function-call-15593298384675158215': 'file_storage/function-call-15593298384675158215.json', 'var_function-call-3658823678110237683': [{'assignee': 'UNKNOWN', 'cpc_code': 'H01M8/2425'}, {'assignee': 'UNKNOWN', 'cpc_code': 'H01M8/2425'}, {'assignee': 'UNKNOWN', 'cpc_code': 'H01M4/9066'}]}

exec(code, env_args)
