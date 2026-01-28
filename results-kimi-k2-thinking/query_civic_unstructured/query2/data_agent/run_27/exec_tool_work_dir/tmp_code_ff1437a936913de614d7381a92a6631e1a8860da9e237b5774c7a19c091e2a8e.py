code = """import json

# Let's first check if the files exist and can be read
import os
print('Files in current directory:', os.listdir('.'))

# Try to read the civic docs file
try:
    with open('var_functions.query_db:2.json', 'r') as f:
        civic_docs_content = f.read()
    print('Civic docs file size:', len(civic_docs_content))
    print('Civic docs first 200 chars:', civic_docs_content[:200])
except Exception as e:
    print('Error reading civic docs:', e)

# Try to read the funding data file
try:
    with open('var_functions.query_db:3.json', 'r') as f:
        funding_content = f.read()
    print('Funding file size:', len(funding_content))
    print('Funding first 200 chars:', funding_content[:200])
except Exception as e:
    print('Error reading funding data:', e)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
