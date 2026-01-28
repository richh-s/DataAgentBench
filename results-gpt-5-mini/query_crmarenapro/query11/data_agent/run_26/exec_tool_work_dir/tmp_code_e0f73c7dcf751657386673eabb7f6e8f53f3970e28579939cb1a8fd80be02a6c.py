code = """import json
# var_call_i8amDck2hH60iWUj8HOKbUqV is available from previous query
records = var_call_i8amDck2hH60iWUj8HOKbUqV
account_raw = None
if records and len(records) > 0:
    account_raw = records[0].get('AccountId')
if account_raw is None:
    result = {"account_id": None}
else:
    # clean: trim whitespace and leading '#'
    acc = account_raw.strip()
    if acc.startswith('#'):
        acc = acc[1:]
    result = {"account_id": acc}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_i8amDck2hH60iWUj8HOKbUqV': [{'Id': '003Wt00000Jqy8SIAR', 'FirstName': 'Anita', 'LastName': 'Kabir', 'Email': 'anita.kabir@futuretechinnovations.com   ', 'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
