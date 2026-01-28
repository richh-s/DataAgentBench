code = """import json
import re

# Load the dataset files
civic_docs_file = var_functions.query_db:38
funding_file = var_functions.query_db:39

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Build funding lookup map
funding_map = {}
for rec in funding_records:
    project_name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    funding_map[project_name] = amount

print('Total funding records:', len(funding_map))
print('Total civic documents:', len(civic_docs))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:34': [], 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:39': 'file_storage/functions.query_db:39.json'}

exec(code, env_args)
