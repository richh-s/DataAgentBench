code = """# Let's check what the variable actually contains
import json, os

var_content = var_functions.query_db:2  # This is a string - the file path

if os.path.exists(var_content):
    with open(var_content, 'r') as f:
        data = json.load(f)
    print('__RESULT__:')
    print(json.dumps({
        'success': True,
        'type': type(data).__name__,
        'length': len(data),
        'first_item': data[0] if data else None
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'success': False,
        'message': f'File not found: {var_content}',
        'var_value': var_content
    }))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'type': 'str', 'length': 38, 'first_item': 'f'}}

exec(code, env_args)
