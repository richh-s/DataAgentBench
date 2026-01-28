code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Create a dictionary of funding by project name for easy lookup
funding_by_project = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if project_name in funding_by_project:
        funding_by_project[project_name] += amount
    else:
        funding_by_project[project_name] = amount

print(f"Unique funded projects: {len(funding_by_project)}")
print("__RESULT__:")
print(json.dumps({"funding_records": len(funding_data), "civic_docs": len(civic_docs), "unique_funded_projects": len(funding_by_project)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
