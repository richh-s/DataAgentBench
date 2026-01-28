code = """import json
paths = {"civic": var_call_PiVO4fMjvPZ9Ri2Sq3DmNv40, "fund": var_call_VWfCe7d7cKITCZHoI1fqcWri}
print("__RESULT__:")
print(json.dumps(paths))"""

env_args = {'var_call_PiVO4fMjvPZ9Ri2Sq3DmNv40': 'file_storage/call_PiVO4fMjvPZ9Ri2Sq3DmNv40.json', 'var_call_VWfCe7d7cKITCZHoI1fqcWri': 'file_storage/call_VWfCe7d7cKITCZHoI1fqcWri.json'}

exec(code, env_args)
