code = """# Let's see what variables are available
import os
available_vars = [var for var in dir() if not var.startswith('_')]
print("Available variables:", available_vars)

# Check if file exists
import os
if os.path.exists('var_functions.query_db:0'):
    print("File exists!")
    with open('var_functions.query_db:0', 'r') as f:
        content_preview = f.read(1000)
        print("Preview:", content_preview[:500])
else:
    print("File does not exist at var_functions.query_db:0")
    # Try to list files in current directory
    print("Files in current directory:", os.listdir('.'))

# Check if the data was stored in a different way
# Let's look at all variables that start with 'var_'
var_vars = [var for var in dir() if var.startswith('var_')]
print("Variables starting with var_:", var_vars)

print('__RESULT__:')
print('{"status": "debugging"}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
