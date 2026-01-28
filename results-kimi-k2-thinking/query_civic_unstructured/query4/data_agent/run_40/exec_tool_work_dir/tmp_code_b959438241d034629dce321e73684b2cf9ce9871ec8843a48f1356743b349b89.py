code = """import json
import re

print("Accessing data from storage variables...")
print("Number of available variables:", len(locals()))

print("\nAvailable keys:")
for key in locals().keys():
    if key.startswith('var_'):
        print(key)
        
print("\nVariable values:")
var_funding = locals().get('var_functions.query_db:5')
var_civic = locals().get('var_functions.query_db:2')

print("Funding variable type:", type(var_funding))
print("Civic variable type:", type(var_civic))

if isinstance(var_funding, str):
    print("Funding is a file path:", var_funding[:100])
else:
    print("Funding is data, length:", len(var_funding) if var_funding else "None")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
