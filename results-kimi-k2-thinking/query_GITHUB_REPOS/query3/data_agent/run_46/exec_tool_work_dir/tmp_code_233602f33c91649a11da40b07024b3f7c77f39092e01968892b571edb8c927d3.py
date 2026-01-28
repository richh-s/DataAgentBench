code = """print(locals().keys())"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['languages', 'repos', 'licenses']}

exec(code, env_args)
