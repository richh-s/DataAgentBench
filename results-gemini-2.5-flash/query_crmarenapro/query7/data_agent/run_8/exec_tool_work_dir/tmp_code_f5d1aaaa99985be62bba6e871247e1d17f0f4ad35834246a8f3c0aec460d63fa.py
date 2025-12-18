code = """import json
case_id = "500Wt00000DDyznIAD".replace("#", "").strip()
print("__RESULT__:")
print(json.dumps(case_id))"""

env_args = {'var_function-call-4528939135170288868': []}

exec(code, env_args)
