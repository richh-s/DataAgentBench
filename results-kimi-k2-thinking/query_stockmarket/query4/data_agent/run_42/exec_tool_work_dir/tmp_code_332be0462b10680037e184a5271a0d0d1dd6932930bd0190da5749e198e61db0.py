code = """print('Checking variable names...')
print('Available locals:', list(locals().keys()))

# Let's check if we have any query_db results
for key in locals().keys():
    if 'query_db' in key or 'list_db' in key:
        print(f'Found: {key}')

print('Done checking')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.query_db:6': [{'name': 'AAAU'}, {'name': 'AADR'}, {'name': 'AAME'}, {'name': 'AAWW'}, {'name': 'AAXJ'}, {'name': 'ABEQ'}, {'name': 'ABMD'}, {'name': 'ACAD'}, {'name': 'ACES'}, {'name': 'ACIO'}]}

exec(code, env_args)
