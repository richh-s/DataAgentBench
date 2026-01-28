code = """import json
import re

# Try to get the data from storage
try:
    mongo_data = locals()['var_functions.query_db:4']
    print(f"MongoDB data type: {type(mongo_data)}")
    print(f"MongoDB data: {str(mongo_data)[:200]}...")
except:
    print("Could not access MongoDB data with that key")

try:
    funding_data = locals()['var_functions.query_db:6']
    print(f"Funding data type: {type(funding_data)}")
    print(f"Funding data: {str(funding_data)[:200]}...")
except:
    print("Could not access Funding data with that key")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
