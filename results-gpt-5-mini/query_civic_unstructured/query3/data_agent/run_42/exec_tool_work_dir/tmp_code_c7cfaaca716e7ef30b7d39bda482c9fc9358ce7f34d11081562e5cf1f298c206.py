code = """import json
print("__RESULT__:")
print(json.dumps("test"))"""

env_args = {'var_call_T7kVCxI35Rb96wVLxFptILKp': 'file_storage/call_T7kVCxI35Rb96wVLxFptILKp.json', 'var_call_Kf6WvGDTE8OWsd75wFh8A3Zf': 'file_storage/call_Kf6WvGDTE8OWsd75wFh8A3Zf.json'}

exec(code, env_args)
