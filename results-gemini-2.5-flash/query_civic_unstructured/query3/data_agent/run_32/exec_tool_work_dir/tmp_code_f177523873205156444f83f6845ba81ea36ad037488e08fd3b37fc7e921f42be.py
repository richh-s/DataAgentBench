code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        line_lower = stripped_line.lower()

        if 'emergency' in line_lower or 'fema' in line_lower:
            # Basic cleanup for potential project names
            project_name = stripped_line.replace('\ufffd', '')
            project_name = project_name.replace('\u2019', "\'")
            project_name = project_name.replace('\u201c', "\"")
            project_name = project_name.replace('\u201d', "\"")
            project_name = project_name.replace('\u2013', '-')
            
            # Simple heuristic: if the line looks like a title (starts with uppercase and is not too short)
            if re.match(r'^[A-Z].{5,}', project_name):
                extracted_projects.append({'Project_Name': project_name})

# Deduplicate projects based on Project_Name
unique_projects = []
seen_project_names = set()
for project in extracted_projects:
    if project['Project_Name'] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
