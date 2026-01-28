code = """import json
# print storage variable values (file paths or small results)
print("__RESULT__:")
print(json.dumps({"civic_var": var_call_O41YPgIMwwpDQ0mDeNFIYiWp, "funding_var": var_call_nwCBWIyTNPQah9PPbJJOWmRT}))"""

env_args = {'var_call_O41YPgIMwwpDQ0mDeNFIYiWp': 'file_storage/call_O41YPgIMwwpDQ0mDeNFIYiWp.json', 'var_call_nwCBWIyTNPQah9PPbJJOWmRT': 'file_storage/call_nwCBWIyTNPQah9PPbJJOWmRT.json'}

exec(code, env_args)
