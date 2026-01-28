code = """# Check what variables are available
available_vars = sorted([key for key in globals().keys() if 'var_functions' in key or 'functions' in key])
print('Available variables with functions prefix:', available_vars)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['commits', 'contents', 'files']}

exec(code, env_args)
