code = """import json
# Access previous query result variable
contact = var_call_9Kb6vecatoooJahP1VXYJdIc[0]
# clean account id
acct = contact['AccountId'].lstrip('#').strip()
print('__RESULT__:')
print(json.dumps(acct))"""

env_args = {'var_call_9Kb6vecatoooJahP1VXYJdIc': [{'Id': '003Wt00000Jqy8SIAR', 'FirstName': 'Anita', 'LastName': 'Kabir', 'Email': 'anita.kabir@futuretechinnovations.com   ', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_7yEyMh87Y2eWxf1hDRxn7oaT': []}

exec(code, env_args)
