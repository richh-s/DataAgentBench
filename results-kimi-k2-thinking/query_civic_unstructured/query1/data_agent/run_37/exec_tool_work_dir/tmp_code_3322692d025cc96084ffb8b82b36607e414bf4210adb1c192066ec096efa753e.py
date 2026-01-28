code = """# Check what variables are available
import sys
print('Globals keys:', [k for k in globals().keys() if 'var_functions' in k])
print('Locals keys:', [k for k in locals().keys() if 'var_functions' in k])

# Check if we can access the stored results
try:
    funding_data = var_functions.query_db_2
    print('Found funding data via var_functions.query_db_2')
except:
    print('Could not access via var_functions.query_db_2')

try:
    civic_docs = var_functions.query_db_5  
    print('Found civic data via var_functions.query_db_5')
except:
    print('Could not access via var_functions.query_db_5')

# Let's see all available variables with 'functions' in the name
all_vars = [k for k in dir() if 'functions' in k]
print('All vars with functions:', all_vars[:10])"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
