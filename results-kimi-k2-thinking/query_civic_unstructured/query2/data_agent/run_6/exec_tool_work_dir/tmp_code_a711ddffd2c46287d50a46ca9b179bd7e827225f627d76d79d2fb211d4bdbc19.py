code = """import json, re

# Read both datasets
with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

with open('file_storage/functions.query_db:20.json', 'r') as f:
    funding_data = json.load(f)

# Extract projects from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if line looks like a project name (not too long, contains project terms)
        project_terms = ['Park', 'Road', 'Project', 'Improvements', 'Repairs', 'Facility', 'Structure', 'Study', 'Drainage', 'Bridge', 'Culvert', 'Walkway', 'Playground']
        
        if len(line) < 100 and any(term in line for term in project_terms):
            # Verify next lines contain project details
            next_text = ' '.join(lines[i+1:min(i+5, len(lines))]).lower()
            if any(indicator in next_text for indicator in ['updates:', 'schedule:', 'description:', 'completion:']):
                current_project = line
        
        # Look for 2022 completion in current and surrounding lines
        if current_project and 'park' in current_project.lower():
            # Search in current line and next few lines
            search_window = ' '.join(lines[i:min(i+8, len(lines))])
            
            if '2022' in search_window and any(comp in search_window.lower() for comp in ['completed', 'completion', 'complete construction', 'construction was completed']):
                # Get specific completion text
                completion_lines = []
                for j in range(i, min(i+8, len(lines))):
                    if '2022' in lines[j] and any(comp in lines[j].lower() for comp in ['completed', 'completion', 'complete construction', 'construction was completed']):
                        completion_lines.append(lines[j].strip())
                
                park_projects_2022.append({
                    'Project_Name': current_project,
                    'completion_info': ' | '.join(completion_lines) if completion_lines else 'Completed in 2022'
                })
                current_project = None

print('__RESULT__:')
print(json.dumps({
    'park_projects_2022': park_projects_2022,
    'count': len(park_projects_2022)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:8': {'path': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'Loaded 5 documents', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
