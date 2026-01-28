code = """import json

# Inspect the type of var_call_xBiYV60jNAjjtZUaBG5HfFo5
obj = var_call_xBiYV60jNAjjtZUaBG5HfFo5
info = {
    'type': str(type(obj)),
}
print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_call_xBiYV60jNAjjtZUaBG5HfFo5': 'file_storage/call_xBiYV60jNAjjtZUaBG5HfFo5.json', 'var_call_AIXjEpfUvdIcrQM9aiyt3Ncc': 'file_storage/call_AIXjEpfUvdIcrQM9aiyt3Ncc.json'}

exec(code, env_args)
