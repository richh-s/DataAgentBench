code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_names_list = []

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Regex to find potential project names that are likely to be related to 'emergency' or 'FEMA'
    # This pattern looks for capitalized phrases that might be project titles.
    # It also explicitly looks for 'FEMA Project' in the name.
    # Using re.IGNORECASE to find 'emergency' and 'FEMA' case-insensitively within project names.
    potential_project_names = re.findall(r'([A-Z][^\n]{5,100}?(?: Project| Improvements| Plan| Study| Repairs| System| Road| Drainage| Wall| Master Plan| Park| Skate Park| Facility| Way| Lane| Signals| Power| Treatment| Signs| Emergency| FEMA| Recovery| Center| Slopes)?)', text, re.DOTALL)
    
    for name in potential_project_names:
        cleaned_name = name.strip()
        # Clean up unicode and smart quotes
        cleaned_name = cleaned_name.replace('\ufffd', '')
        cleaned_name = cleaned_name.replace('\u2019', "'")
        cleaned_name = cleaned_name.replace('\u201c', '\"')
        cleaned_name = cleaned_name.replace('\u201d', '\"')
        cleaned_name = cleaned_name.replace('\u2013', '-')
        
        # Filter for projects explicitly mentioning 'emergency' or 'FEMA' in their name
        if 'emergency' in cleaned_name.lower() or 'fema' in cleaned_name.lower():
            project_names_list.append({'Project_Name': cleaned_name})

# Remove duplicates based on Project_Name
unique_project_names = []
seen_project_names = set()
for project in project_names_list:
    if project['Project_Name'] not in seen_project_names:
        unique_project_names.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_project_names, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
