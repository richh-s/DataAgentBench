code = """import json
import os

# Read the civic documents file
civic_docs_path = '/tmp/tmpq0c3uww8.json'
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Read the funding data file
funding_path = '/tmp/tmphv6u7l7_.json'
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_data = json.load(f)

# Find park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if this document mentions both 2022 and completion
    if '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        # Split into lines and analyze
        lines = text.split('\n')
        for line in lines:
            stripped = line.strip()
            # Look for lines that look like project names (not too short, not bullet points)
            if len(stripped) > 10 and not stripped.startswith('(') and not stripped.startswith('•'):
                # Check if it's park-related
                line_lower = stripped.lower()
                if 'park' in line_lower:
                    # Check if it looks like a project name
                    if 'project' in line_lower or 'improvements' in line_lower or 'repairs' in line_lower or 'replacement' in line_lower:
                        park_projects.append(stripped)

# Remove duplicates
park_projects = list(set(park_projects))
print('Park projects:', len(park_projects))

# Create funding lookup
funding_total = 0
matched_projects = []

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    
    # Check if this funding matches any of our park projects
    for park_proj in park_projects:
        park_name = park_proj.lower()
        fund_name_lower = fund_name.lower()
        
        # Match if names are similar (one is contained in the other)
        if park_name in fund_name_lower or fund_name_lower in park_name:
            funding_total += amount
            if park_proj not in matched_projects:
                matched_projects.append(park_proj)
            break

print('Total funding:', funding_total)
print('Matched project count:', len(matched_projects))

result = str(funding_total)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
