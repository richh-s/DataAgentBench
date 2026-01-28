code = """# Let's inspect what we actually have in the storage variable
# The result is likely a file path string
file_path = var_functions.query_db:0
print('__RESULT__:')
print(json.dumps({
    'file_path': file_path,
    'type': str(type(file_path))
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo']}

exec(code, env_args)
