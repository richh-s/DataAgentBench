code = """import json

# Read the full civic_docs result
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    documents = json.load(f)

# Extract park-related projects from documents
park_projects = []

for doc in documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project names that contain "park" (case insensitive)
    for line in lines:
        line = line.strip()
        # Look for project names based on context clues
        # Project names often appear as standalone lines or bullet points
        if ('park' in line.lower()) and len(line) < 150:  # Reasonable length for a project name
            # Skip if it's just a section header
            if any(header in line.lower() for header in ['capital improvement', 'disaster recovery', 'projects', 'status report', 'discussion', 'recommended action']):
                continue
            if line.startswith('('):  # Skip bullet/number markers
                continue
            if not line.strip():  # Skip empty lines
                continue
                
            # Look for completion info nearby
            project_info = {
                'project_name': line,
                'completed_2022': False,
                'topic': 'park'
            }
            
            # Look for completion info within the next few lines
            for i in range(max(0, lines.index(line)), min(len(lines), lines.index(line) + 10)):
                next_line = lines[i].strip().lower()
                if 'completed' in next_line and '2022' in next_line:
                    project_info['completed_2022'] = True
                    break
                    
            park_projects.append(project_info)

# Remove duplicates
unique_projects = {}
for proj in park_projects:
    if proj['project_name'] not in unique_projects:
        unique_projects[proj['project_name']] = proj
        
park_projects_unique = list(unique_projects.values())

# Count how many were completed in 2022
completed_2022 = [p for p in park_projects_unique if p['completed_2022']]

result = {
    'total_park_projects': len(park_projects_unique),
    'park_projects_2022': completed_2022,
    'count_2022': len(completed_2022),
    'all_park_projects': park_projects_unique
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
