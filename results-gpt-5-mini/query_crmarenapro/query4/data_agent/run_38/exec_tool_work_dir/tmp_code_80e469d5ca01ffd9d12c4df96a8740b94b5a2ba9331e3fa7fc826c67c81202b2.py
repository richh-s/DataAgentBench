code = """import json
# var_call_5H6oz5zfmhRrjuOijegm7AyX is available from previous query
records = var_call_5H6oz5zfmhRrjuOijegm7AyX
# Extract Ids, remove leading # and whitespace
cleaned = [rec.get('Id','') for rec in records]
cleaned = [s.lstrip('#').strip() for s in cleaned if s]
# Produce SQL IN list string
in_list = ','.join("'{}'".format(s.replace("'","''")) for s in cleaned)
output = json.dumps({'in_list': in_list, 'ids': cleaned})
print("__RESULT__:")
print(output)"""

env_args = {'var_call_5H6oz5zfmhRrjuOijegm7AyX': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
