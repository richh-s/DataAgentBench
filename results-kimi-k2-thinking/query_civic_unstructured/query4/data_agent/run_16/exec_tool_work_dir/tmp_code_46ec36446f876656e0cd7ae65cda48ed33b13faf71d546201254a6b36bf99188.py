code = """import json
import re

# Load civic documents
civic_docs = []
with open("/tmp/tmp7q6r1zwh.json", "r") as f:
    civic_docs = json.load(f)

# Load funding data  
funding_data = []
with open("/tmp/tmptf8vwxq6.json", "r") as f:
    funding_data = json.load(f)

print("LOADED DATA COMPLETE")
print(f"Civic documents: {len(civic_docs)}")
print(f"Funding records: {len(funding_data)}")

# Show first project name from funding
if funding_data:
    print(f"First project: {funding_data[0]['Project_Name']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
