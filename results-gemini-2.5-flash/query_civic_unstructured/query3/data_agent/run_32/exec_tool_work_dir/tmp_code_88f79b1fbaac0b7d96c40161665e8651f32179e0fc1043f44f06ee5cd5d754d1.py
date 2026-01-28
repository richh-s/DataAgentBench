code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Regex to find potential project names that are typically capitalized and followed by a (cid:190) marker.
    # This pattern attempts to capture the project name and its immediate details section.
    # Using a triple-quoted raw string to handle multi-line and special characters.
    project_blocks = re.findall(
        r"""\n\n([A-Z][^\n]{5,100}?(?: Project| Improvements| Plan| Study| Repairs| System| Road| Drainage| Wall| Master Plan| Park| Skate Park| Facility| Way| Lane| Signals| Power)?)\n(\(cid:190\) (?:Updates:|Project Schedule:|Project Description:|Estimated Schedule:).*?)(?=\n\n[A-Z]|$|\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects)""", 
        text, 
        re.DOTALL
    )

    for project_name_raw, project_content_raw in project_blocks:
        project_name = project_name_raw.strip()
        project_name = project_name.replace('\ufffd', '')
        project_name = project_name.replace('\u2019', "'")
        project_name = project_name.replace('\u201c', '\"')
        project_name = project_name.replace('\u201d', '\"')
        project_name = project_name.replace('\u2013', '-')

        full_project_text = (project_name.lower() + ' ' + project_content_raw.lower()).replace("\n", " ")

        # Filter for projects related to 'emergency' or 'FEMA'
        if not ('emergency' in full_project_text or 'fema' in full_project_text):
            continue

        topics = []
        status = 'N/A'
        project_type = 'N/A'
        
        # Extract topic
        if 'emergency' in full_project_text:
            topics.append('emergency')
        if 'fema' in full_project_text:
            topics.append('FEMA')
        if 'emergency warning' in full_project_text:
            topics.append('emergency warning')
        if '(fema project)' in project_name.lower():
            topics.append('FEMA')
        if 'homeland security' in full_project_text:
            topics.append('homeland security')
        if 'disaster' in full_project_text:
            topics.append('disaster')
        if not topics:
            topics.append('N/A')
            
        # Extract status
        if 'completed' in full_project_text or 'completion filed' in full_project_text:
            status = 'completed'
        elif 'construction' in full_project_text or 'under construction' in full_project_text:
            status = 'construction'
        elif 'design' in full_project_text or 'preliminary design' in full_project_text:
            status = 'design'
        elif 'not started' in full_project_text:
            status = 'not started'
        elif 'delayed' in full_project_text:
            status = 'delayed'
            
        # Extract type
        if 'capital improvement projects' in full_project_text:
            project_type = 'capital'
        elif 'disaster recovery projects' in full_project_text:
            project_type = 'disaster'
        
        project_data.append({
            'Project_Name': project_name,
            'topic': topics,
            'type': project_type,
            'status': status,
        })

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for project in project_data:
    if project['Project_Name'] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
