code = """import json
print("__RESULT__:")
print(json.dumps("test"))"""

env_args = {'var_function-call-15044746787595229407': 'file_storage/function-call-15044746787595229407.json', 'var_function-call-2315172505104339094': 'file_storage/function-call-2315172505104339094.json', 'var_function-call-5384306223597069049': 'file_storage/function-call-5384306223597069049.json', 'var_function-call-331467625531987005': 1435}

exec(code, env_args)
