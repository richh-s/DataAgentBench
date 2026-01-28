code = """import json
import re

# Get the funding data - check if it's a file path or direct data
funding_result = locals().get('var_functions.query_db:0')
civic_result = locals().get('var_functions.query_db:4')

# Load data
funding_data = []
civic_docs = []

# Parse funding data
if isinstance(funding_result, str) and '.json' in funding_result:
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result if funding_result else []

# Parse civic docs
if isinstance(civic_result, str) and '.json' in civic_result:
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result if civic_result else []

# Extract project information from civic documents
projects_info = []

for doc in civic_docs:
    if isinstance(doc, dict):
        text = doc.get('text', '')
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for completion patterns with 2022
            if ('completed' in line.lower() or 'complete construction' in line.lower()) and '2022' in line:
                # Look backwards for project name
                for j in range(max(0, i-10), i):
                    prev_line = lines[j].strip()
                    if prev_line and not prev_line.startswith('(') and not prev_line.startswith('—'):
                        # Extract status and completion info
                        status = 'completed'
                        projects_info.append({
                            'project_name': prev_line,
                            'status': status,
                            'completion_year': '2022',
                            'source_line': line
                        })
                        break

# Match with funding data
park_funding = 0
park_projects = []

for funding in funding_data:
    if isinstance(funding, dict):
        project_name = funding.get('Project_Name', '')
        amount = int(funding.get('Amount', 0))
        
        # Check if it's a park project
        if any(keyword in project_name.lower() for keyword in ['park', 'bluffs', 'playground', 'arbors']):
            # Check if completed in 2022
            for project in projects_info:
                proj_name = project.get('project_name', '')
                if (project_name in proj_name or proj_name in project_name) and project.get('status') == 'completed':
                    park_funding += amount
                    park_projects.append({
                        'name': project_name,
                        'amount': amount
                    })
                    break

# Alternative approach: check for park projects that mention completion 2022
park_keywords = ['park', 'bluffs', 'playground', 'arbor', 'walkway', 'shade structure']

for funding in funding_data:
    if isinstance(funding, dict):
        project_name = funding.get('Project_Name', '')
        amount = int(funding.get('Amount', 0))
        
        if any(keyword in project_name.lower() for keyword in park_keywords):
            # Check if the project name appears in civic docs with 2022 completion
            for doc in civic_docs:
                if isinstance(doc, dict):
                    text = doc.get('text', '').lower()
                    name_lower = project_name.lower()
                    if name_lower in text and ('completed' in text or 'completion' in text) and '2022' in text:
                        # Double check this is about this specific project
                        park_funding += amount
                        park_projects.append({
                            'name': project_name,
                            'amount': amount
                        })
                        break

print('__RESULT__:')
print(json.dumps({
    'total_funding': park_funding,
    'projects': park_projects,
    'project_count': len(park_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
