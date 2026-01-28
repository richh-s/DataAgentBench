code = """import json
import re

# Load the civic documents data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Convert funding records to a dictionary for easier lookup
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_dict[project_name] = amount

# Extract park-related projects that were completed in 2022
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project sections in the text
    # Projects are typically listed with bullet points or specific formatting
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for project names (usually bold or as headers)
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('o') and not line.startswith('□'):
            # Check if this line looks like a project name
            if len(line) > 10 and not any(keyword in line.lower() for keyword in ['updates:', 'schedule:', 'project description:', 'status:']):
                # This might be a project name
                current_project = line
                project_info = {'name': current_project}
        
        # Look for status information
        if 'completed' in line.lower() and current_project:
            project_info['status'] = 'completed'
        
        # Look for date information (check for 2022 in completion dates)
        if '2022' in line and 'completed' in line.lower() and current_project:
            project_info['completed_2022'] = True
        
        # Check if this is a park project by looking for 'park' in the project name
        if current_project and 'park' in current_project.lower():
            project_info['is_park'] = True
    
    # Add projects that match our criteria
    if project_info.get('is_park') and project_info.get('status') == 'completed':
        # Check if the text mentions completion in 2022
        if 'completed' in text.lower() and '2022' in text:
            # More specific check for this particular project
            project_name = project_info.get('name', '')
            if 'park' in project_name.lower():
                park_projects_completed_2022.append(project_name)

# Print out the projects found
print('__RESULT__:')
print(json.dumps({
    'park_projects': park_projects_completed_2022,
    'count': len(park_projects_completed_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
