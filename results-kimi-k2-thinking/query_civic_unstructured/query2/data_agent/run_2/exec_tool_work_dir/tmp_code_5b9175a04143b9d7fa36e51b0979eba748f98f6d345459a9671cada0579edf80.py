code = """import json
import re

# Load the data from the stored file paths
civic_docs_fp = locals()['var_functions.query_db:0']
funding_fp = locals()['var_functions.query_db:2']

with open(civic_docs_fp, 'r') as f:
    civic_docs = json.load(f)

with open(funding_fp, 'r') as f:
    funding = json.load(f)

print('Loaded', len(civic_docs), 'documents and', len(funding), 'funding records')

# Look for specific patterns indicating park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Search for park-related projects with 2022 completion
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line looks like a project name with park in it
        line_lower = line.lower()
        if 'park' in line_lower and len(line) < 100 and line[0].isupper():
            # Look ahead for completion status and 2022 date
            context_start = max(0, i)
            context_end = min(len(lines), i + 8)
            context = ' '.join(lines[context_start:context_end])
            
            if 'completed' in context.lower() and '2022' in context:
                park_projects_2022.append(line)

# Remove duplicates
unique_projects = list(set(park_projects_2022))
print('Found park projects completed in 2022:', len(unique_projects))
for proj in unique_projects:
    print('-', proj)

# Find funding for park projects
total_funding = 0
seen_funding = set()

# Match identified projects with funding records
for project in unique_projects:
    proj_lower = project.lower()
    
    for fund in funding:
        fund_name = fund.get('Project_Name', '')
        if fund_name in seen_funding:
            continue
            
        fund_lower = fund_name.lower()
        fund_amount = int(fund.get('Amount', 0))
        
        # Check if this funding matches our project
        if 'park' in fund_lower:
            # Direct name match or partial match
            if proj_lower in fund_lower or fund_lower in proj_lower:
                total_funding += fund_amount
                seen_funding.add(fund_name)
            elif any(keyword in fund_lower for keyword in ['shade', 'structure', 'walkway']):
                # These likely related to park improvements completed in 2022
                total_funding += fund_amount
                seen_funding.add(fund_name)

print('Total funding calculated:', total_funding)
answer = 'Total funding for park-related projects completed in 2022 is ${:,}'.format(total_funding)
print('__RESULT__:', answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.list_db:17': ['Funding']}

exec(code, env_args)
