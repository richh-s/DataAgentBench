code = """import json, re
print('__RESULT__:')
print(json.dumps({'test': bool(re.search(r'\\b(19\\d{2}|20\\d{2})\\b','Copyright 2019'))}))"""

env_args = {'var_call_gdpScBbhv5TooWljmDT7Dc6G': 'file_storage/call_gdpScBbhv5TooWljmDT7Dc6G.json', 'var_call_2F1arjDMEJ90CApnyrEodfYU': 'file_storage/call_2F1arjDMEJ90CApnyrEodfYU.json', 'var_call_3JcGcuFadE6mc0uD7bJMqbKe': {'ok': True}}

exec(code, env_args)
