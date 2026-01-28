code = """import json
import re

# Load civic documents from the stored file
civic_docs_file = var_functions.query_db:5
civic_docs = json.load(open(civic_docs_file))

# Load funding data from the stored file
funding_file = var_functions.query_db:48
funding = json.load(open(funding_file))

# Function to extract projects from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for potential project names containing "Park"
        if 'Park' in line and len(line) > 5 and not line.startswith('('):
            # Skip headers/metadata
            skip_patterns = ['Subject:', 'Page', 'Item', 'To:', 'From:', 'Date:', 'Public Works', 'Commission', 'Agenda']
            if not any(pattern in line for pattern in skip_patterns):
                # Look ahead for status and completion date
                next_lines = lines[i+1:i+15]
                next_text = ' '.join(next_lines).lower()
                
                # Check if completed in 2022
                if ('completed' in next_text or 'completion' in next_text) and '2022' in ' '.join(next_lines):
                    # Verify it's actually completed in 2022 (not scheduled)
                    if re.search(r'completed[^\n]{0,100}2022|2022[^\n]{0,100}completed|november\s+2022|december\s+2022|construction was completed.*2022', 
                               ' '.join(next_lines), re.IGNORECASE):
                        park_projects_2022.append(line.strip())
        
        i += 1

# Remove duplicates
unique_projects = list(set(park_projects_2022))

# Find funding for these projects
funding_matches = []
total_funding = 0

for project in unique_projects:
    for fund in funding:
        fund_name = fund.get('Project_Name', '')
        # Check for partial match (project name contained in funding name)
        if project.lower() in fund_name.lower():
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            funding_matches.append({
                'project': project,
                'funding_project': fund_name,
                'amount': amount
            })

result = {
    'park_projects_completed_2022': unique_projects,
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'funding_breakdown': funding_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
