code = """import sys
import json

# Get all variables in current scope
all_vars = dir()
print('ALL VARS:', all_vars[:20])

# Try to find the variable with the query result
query_vars = [v for v in all_vars if 'query_db' in v]
print('QUERY VARS:', query_vars)

# If we can't find it, let's just work with the knowledge that
# we have a publication_database with publicationinfo table"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition']}

exec(code, env_args)
