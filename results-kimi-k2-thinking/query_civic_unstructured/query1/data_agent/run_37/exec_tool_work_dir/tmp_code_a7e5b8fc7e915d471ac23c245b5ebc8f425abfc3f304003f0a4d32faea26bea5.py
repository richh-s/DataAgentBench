code = """# Check what variables are actually available
all_globals = list(globals().keys())
print('All global variables starting with var_functions:')
var_func_vars = [g for g in all_globals if g.startswith('var_functions')]
print(var_func_vars)

# Try to access the variables
try:
    funding_var = 'var_functions.query_db\u002e2'  # Use unicode escape for colon
    if funding_var in globals():
        print('Found funding variable')
        print('Type:', type(globals()[funding_var]))
        print('Value:', str(globals()[funding_var])[:200])
except:
    print('Could not access funding variable')

try:
    civic_var = 'var_functions.query_db\u002e5'  # Use unicode escape for colon
    if civic_var in globals():
        print('Found civic variable')
        print('Type:', type(globals()[civic_var]))
        print('Value:', str(globals()[civic_var])[:200])
except:
    print('Could not access civic variable')"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
