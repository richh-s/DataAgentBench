code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

# A very simple regex to find lines that might be project names
# This version avoids complex escaping and focuses on basic structure.
project_name_simple_pattern = re.compile(r'^[A-Z][a-zA-Z0-9 ]*(?:Project|Plan|Improvements|Study)\s*$')

# Keywords for filtering
relevant_keywords = ['emergency', 'FEMA', 'disaster', 'CalOES']

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_details = []
    
    for line in lines:
        line = line.strip()
        if not line: # Skip empty lines
            continue

        if project_name_simple_pattern.search(line):
            if current_project_name:
                full_project_text = (current_project_name + ' ' + ' '.join(current_project_details))
                if any(keyword.lower() in full_project_text.lower() for keyword in relevant_keywords):
                    projects_data.append({
                        "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                        "Full_Text": full_project_text
                    })
            
            current_project_name = line
            current_project_details = []
        elif current_project_name:
            current_project_details.append(line)
            
    # Process the last project after the loop
    if current_project_name:
        full_project_text = (current_project_name + ' ' + ' '.join(current_project_details))
        if any(keyword.lower() in full_project_text.lower() for keyword in relevant_keywords):
            projects_data.append({
                "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                "Full_Text": full_project_text
            })

# Deduplicate projects based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects_data:
    normalized_name = re.sub(r'\s*(?:Project|Projects|Plan|Improvements|Study|Program|Report|Update|Master Plan)$', '', p['Project_Name'], flags=re.IGNORECASE).strip()
    if normalized_name not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(normalized_name)

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json', 'var_function-call-374798579160347094': ['Funding'], 'var_function-call-18081243149010549445': 'file_storage/function-call-18081243149010549445.json'}

exec(code, env_args)
