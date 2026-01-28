code = """import json
# Print the storage variable names and types
res = {'var1': var_call_JuYIc5TDnDtRd8TtislB5SI8, 'var2': var_call_iWKlRsPXFz8VehE93rIAy156}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_JuYIc5TDnDtRd8TtislB5SI8': 'file_storage/call_JuYIc5TDnDtRd8TtislB5SI8.json', 'var_call_iWKlRsPXFz8VehE93rIAy156': 'file_storage/call_iWKlRsPXFz8VehE93rIAy156.json'}

exec(code, env_args)
