code = """import json
import re

# Helper function to safely load data
 civic_docs_path = var_functions.query_db:60
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = var_functions.query_db:48
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Find all park-related projects from civic documents
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Split into lines using alternative method to avoid escape issues
    lines = text.splitlines()
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for lines containing Park (case-sensitive for project names)
        if 'Park' in line and len(line) > 5:
            # Skip header/metadata lines
            skip_patterns = ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Agenda', 'Commission', 'Public Works']
            is_header = any(pattern in line for pattern in skip_patterns)
            
            if not is_header and not line.startswith('('):
                # Check if this project was completed in 2022
                context_start = max(0, i-2)
                context_end = min(len(lines), i+15)
                context = ' '.join(lines[context_start:context_end])
                
                # Check for completion status and 2022 date
                context_lower = context.lower()
                if ('completed' in context_lower or 'completion' in context_lower) and '2022' in context:
                    # Make sure it's not a future project
                    if 'will be completed' not in context_lower and 'to be completed' not in context_lower:
                        park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Find funding matches
total_funding = 0
matches = []

for project in unique_projects:
    project_lower = project.lower()
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Match if project name is part of the funding name
        if project_lower in fund_name.lower():
            total_funding += fund_amount
            matches.append([project, fund_name, fund_amount])

# Output results
result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
