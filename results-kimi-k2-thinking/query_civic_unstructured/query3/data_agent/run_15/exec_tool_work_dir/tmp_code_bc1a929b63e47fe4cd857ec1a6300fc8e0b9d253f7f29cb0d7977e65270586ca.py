code = """# Check what variables are available
available_vars = list(locals().keys())
print('Available variables:', available_vars)

# Look for the specific variables we need
funding_var = None
civic_var = None

for var in available_vars:
    if 'query_db' in var:
        print(f'Found variable: {var}')
        if ':0' in var:
            funding_var = var
        elif ':2' in var:
            civic_var = var

print('Funding variable:', funding_var)
print('Civic variable:', civic_var)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
