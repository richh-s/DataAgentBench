code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_names_raw = set() # Use a set to store unique raw project names

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        if 'emergency' in stripped_line.lower() or 'fema' in stripped_line.lower():
            # Basic heuristic for a project name: starts with a capital letter and is not too short
            if re.match(r'^[A-Z][a-zA-Z0-9\s&,-_\']{5,}', stripped_line):
                project_names_raw.add(stripped_line)

# Clean up project names and convert to a list of dictionaries
unique_project_names = []
for name_raw in project_names_raw:
    project_name = name_raw.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
    unique_project_names.append({'Project_Name': project_name})

print("__RESULT__:")
print(json.dumps(unique_project_names, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
