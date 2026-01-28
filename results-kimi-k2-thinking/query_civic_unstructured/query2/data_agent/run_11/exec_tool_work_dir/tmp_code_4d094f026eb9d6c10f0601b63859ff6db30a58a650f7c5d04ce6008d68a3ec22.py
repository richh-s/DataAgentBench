code = """import json
import re

# Read the civic documents file from the stored path
civic_docs_path = var_functions.query_db:60
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Split lines - avoiding the backslash issue
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names containing Park
        if 'Park' in line and len(line) > 5:
            # Skip header/metadata lines
            skip_patterns = ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:']
            if any(pattern in line for pattern in skip_patterns):
                continue
            if line.startswith('('):
                continue
            
            # Look ahead for completion status and 2022 date
            next_section = ' '.join(lines[i:i+15])
            lower_next = next_section.lower()
            
            # Check if completed in 2022
            if ('completed' in lower_next or 'completion' in lower_next) and '2022' in next_section:
                # Avoid "scheduled to be completed" entries
                if 'will be completed' not in lower_next and 'to be completed' not in lower_next:
                    park_projects_2022.append(line)

# Remove duplicates
unique_park_projects = list(set(park_projects_2022))

# Load funding data and find matches
funding_path = var_functions.query_db:48
with open(funding_path, 'r') as f:
    funding = json.load(f)

funding_matches = []
total_funding = 0

for project in unique_park_projects:
    project_lower = project.lower()
    for fund_rec in funding:
        fund_name = fund_rec.get('Project_Name', '')
        fund_amount = int(fund_rec.get('Amount', 0))
        
        # Check if project name appears in funding project name
        if project_lower in fund_name.lower():
            funding_matches.append([project, fund_name, fund_amount])
            total_funding += fund_amount

# Output results
result = {
    'park_projects_completed_2022': unique_park_projects,
    'number_of_projects': len(unique_park_projects),
    'total_funding_amount': total_funding,
    'funding_matches': funding_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
