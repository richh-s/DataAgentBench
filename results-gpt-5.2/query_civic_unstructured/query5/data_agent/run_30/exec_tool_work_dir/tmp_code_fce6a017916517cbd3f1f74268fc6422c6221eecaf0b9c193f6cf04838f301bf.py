code = """import json

result = {'note':'skip'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_POnMSnCxvKJodwURvENF1OP4': 'file_storage/call_POnMSnCxvKJodwURvENF1OP4.json', 'var_call_IegVeO7iEQ8LuDVQdQO2qcWC': 'file_storage/call_IegVeO7iEQ8LuDVQdQO2qcWC.json'}

exec(code, env_args)
