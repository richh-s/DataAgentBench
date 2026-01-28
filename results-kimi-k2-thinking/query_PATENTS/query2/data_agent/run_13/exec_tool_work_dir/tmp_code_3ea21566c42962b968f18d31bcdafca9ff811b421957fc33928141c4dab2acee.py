code = """# Access the table list result
result = locals()['var_functions.list_db:0']
print('__RESULT__:')
import json
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo']}

exec(code, env_args)
