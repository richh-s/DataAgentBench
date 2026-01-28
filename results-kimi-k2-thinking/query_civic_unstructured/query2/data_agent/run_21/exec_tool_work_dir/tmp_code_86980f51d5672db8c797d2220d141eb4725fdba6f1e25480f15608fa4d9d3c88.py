code = """import json
import re
import os

# Load the file paths from locals
funding_path = locals()['var_functions.query_db:10']
civic_path = locals()['var_functions.query_db:11']

# Read funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read civic docs data
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print(f'Funding records: {len(funding_data)}')
print(f'Civic docs: {len(civic_data)}')

# Filter park-related projects from funding data
park_funding = [f for f in funding_data if 'park' in f['Project_Name'].lower()]
print(f'Park-related funding records: {len(park_funding)}')
print(f'Sample park projects: {[p["Project_Name"] for p in park_funding[:10]]}')
print(f'Sample amounts: {[p["Amount"] for p in park_funding[:5]]}')

# Extract park projects completed in 2022 from civic docs
park_projects_2022 = []

for doc in civic_data:
    text = doc['text']
    
    # Look for park mentions
    # We'll extract project blocks that mention both park and completion dates in 2022
    # Split by project sections (look for common patterns)
    
    # Simple approach: find lines mentioning park and 2022 completion
    lines = text.split('\n')
    for line in lines:
        if 'park' in line.lower() and '2022' in line:
            # Look for completion indicators
            if any(word in line.lower() for word in ['completed', 'completion', 'complete']):
                park_projects_2022.append(line.strip())

print(f'\nPotential 2022 park completions found: {len(park_projects_2022)}')
for p in park_projects_2022[:5]:
    print(f'  - {p}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
