code = """import json

# Read the result from the variable
companies_var = globals()['var_functions.query_db:0'] if 'var_functions.query_db:0' in globals() else locals()['var_functions.query_db:0']
print(f"Type of result: {type(companies_var)}")
print(f"Content (first 200 chars): {str(companies_var)[:200]}")

# The result might be stored as a JSON string or a list
if isinstance(companies_var, str):
    try:
        companies = json.loads(companies_var)
    except:
        # It might be a file path
        if companies_var.endswith('.json'):
            with open(companies_var, 'r') as f:
                companies = json.load(f)
        else:
            print(f"Unexpected string format: {companies_var}")
            companies = []
else:
    companies = companies_var

print(f"Number of companies: {len(companies) if isinstance(companies, list) else 'Not a list'}")
if companies and len(companies) > 0:
    print(f"First company: {companies[0]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
