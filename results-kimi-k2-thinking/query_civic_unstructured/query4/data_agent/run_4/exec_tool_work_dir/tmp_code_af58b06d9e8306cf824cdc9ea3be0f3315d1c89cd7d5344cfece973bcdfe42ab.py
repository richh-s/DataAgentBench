code = """import json
import re

# Load civic documents from file
civic_docs_file = var_functions.query_db:50
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from previous query
funding_file = var_functions.query_db:52
funding_data = []
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup by project name
funding_lookup = {}
for fund in funding_data:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    if proj_name:
        funding_lookup[proj_name] = amount

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")
print(f"Created funding lookup with {len(funding_lookup)} unique projects")

# Show first few funding entries
print("\nSample funding entries:")
for i, (name, amount) in enumerate(list(funding_lookup.items())[:5]):
    print(f"  {i+1}. {name}: ${amount:,}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '500', 'total_amount': '28094000'}]}

exec(code, env_args)
