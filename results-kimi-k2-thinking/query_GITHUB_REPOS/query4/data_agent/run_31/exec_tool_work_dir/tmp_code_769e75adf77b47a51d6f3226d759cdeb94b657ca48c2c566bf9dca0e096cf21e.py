code = """# Load the languages table to see how language descriptions look
languages_result = var_functions.list_db:0
print('__RESULT__:') 
print('Already have table list. Need to query languages table.')"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses']}

exec(code, env_args)
