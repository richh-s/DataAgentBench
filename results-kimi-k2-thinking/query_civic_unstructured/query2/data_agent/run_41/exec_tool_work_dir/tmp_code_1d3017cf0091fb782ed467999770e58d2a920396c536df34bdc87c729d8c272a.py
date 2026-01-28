code = """import json
import re

# Load civic documents data
civic_docs_file = var_functions.query_db:2
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

# Load funding data
funding_file = var_functions.query_db:5
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract project information from civic documents
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections - patterns that indicate project listings
    # Common patterns: project names followed by status updates
    
    # Find all potential project mentions with park-related keywords
    # Look for completed projects with 2022 dates
    
    # Pattern to find project names and their status
    lines = text.split('\n')
    
    current_project = None
    project_status = None
    project_dates = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically bolded or title case lines)
        # Skip agenda headers and common non-project lines
        if (line and 
            not line.startswith('Public Works') and
            not line.startswith('Commission') and
            not line.startswith('Agenda') and
            not line.startswith('Page') and
            not line.startswith('Item') and
            len(line) > 10 and
            len(line) < 200):
            
            # Check if this is likely a project name (has capital words, not just common text)
            capital_ratio = sum(1 for c in line if c.isupper()) / len(line) if line else 0
            if capital_ratio > 0.3 and 'Updates' not in line and 'Schedule' not in line:
                current_project = line
                # Look ahead for status and dates
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    if 'completed' in next_line.lower() or 'construction was completed' in next_line.lower():
                        project_status = 'completed'
                    if '2022' in next_line:
                        project_dates.append('2022')
                        
        # Check for park-related keywords in the project or surrounding text
        if current_project:
            context_window = ' '.join(lines[max(0, i-3):min(len(lines), i+3)]).lower()
            
            park_keywords = ['park', 'playground', 'shade structure', 'walkway', 'bluffs park']
            is_park_related = any(keyword in context_window for keyword in park_keywords)
            
            is_completed_2022 = project_status == 'completed' and '2022' in ' '.join(project_dates)
            
            # Also check for explicit completion mentions with 2022
            if not is_completed_2022 and project_status == 'completed':
                # Look for 2022 in recent lines
                for j in range(max(0, i-5), min(len(lines), i+10)):
                    if '2022' in lines[j] and ('complete' in lines[j].lower() or 'construction was completed' in lines[j].lower()):
                        project_dates.append('2022')
                        is_completed_2022 = True
                        break
            
            if is_park_related and is_completed_2022 and current_project not in [p['name'] for p in park_projects_completed_2022]:
                park_projects_completed_2022.append({
                    'name': current_project,
                    'status': project_status,
                    'dates': project_dates
                })
    
print(f"Found {len(park_projects_completed_2022)} park projects completed in 2022")
for proj in park_projects_completed_2022:
    print(f"  - {proj['name']}")

# Save the extracted projects
result = json.dumps(park_projects_completed_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
