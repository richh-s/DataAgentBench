code = """# Process civic documents to extract project information
import json
import re
from collections import defaultdict

# Load civic docs from the file
civic_docs_file = '/var/results/var_functions.query_db:16.json'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from the file  
funding_file = '/var/results/var_functions.query_db:8.json'
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_records)} funding records")

# Create a funding lookup by project name
funding_lookup = {}
for record in funding_records:
    funding_lookup[record['Project_Name']] = {
        'Funding_ID': record['Funding_ID'],
        'Funding_Source': record['Funding_Source'],
        'Amount': int(record['Amount'])
    }

print(f"Funding lookup created for {len(funding_lookup)} projects")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
