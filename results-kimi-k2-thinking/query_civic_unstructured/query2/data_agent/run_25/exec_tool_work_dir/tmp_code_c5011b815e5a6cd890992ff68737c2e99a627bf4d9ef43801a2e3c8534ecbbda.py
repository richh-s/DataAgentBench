code = """import json
import re

# Load the civic documents data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create a dictionary of funding amounts by project name for easy lookup
funding_dict = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    funding_dict[proj_name] = amount

# Parse civic documents to find park projects completed in 2022
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if not line:
            continue
            
        # Look for project names containing Park
        if ('Park' in line or 'park' in line) and len(line) > 5:
            # Check if not a header
            if not any(header in line for header in ['Capital Improvement', 'Disaster Recovery', 'Project Status', 'RECOMMENDED ACTION']):
                current_project = line
                
                # Check next few lines for completion status
                for j in range(i, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    
                    if 'completed' in next_line.lower() and '2022' in next_line:
                        park_projects_completed_2022.append(current_project)
                        break

# Remove duplicates
park_projects_completed_2022 = list(set(park_projects_completed_2022))

# Find funding for these projects
funding_matches = []
total_funding = 0

for project in park_projects_completed_2022:
    # Direct match
    if project in funding_dict:
        funding_matches.append({
            'project': project,
            'amount': funding_dict[project]
        })
        total_funding += funding_dict[project]

# Also check for broader patterns in documents
projects_with_2022_completion = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'completed' in text.lower() and '2022' in text:
        # Extract lines mentioning both completed and 2022
        lines = text.split('\n')
        for line in lines:
            if 'completed' in line.lower() and '2022' in line and 'park' in line.lower():
                projects_with_2022_completion.append(line.strip())

print('__RESULT__:')
result = {
    'park_projects_completed_2022': park_projects_completed_2022,
    'projects_with_2022_completion': projects_with_2022_completion,
    'funding_matches': funding_matches,
    'total_funding': total_funding,
    'num_projects_found': len(park_projects_completed_2022),
    'num_funding_matches': len(funding_matches)
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'civic_docs_count': 5, 'funding_records_count': 500}}

exec(code, env_args)
