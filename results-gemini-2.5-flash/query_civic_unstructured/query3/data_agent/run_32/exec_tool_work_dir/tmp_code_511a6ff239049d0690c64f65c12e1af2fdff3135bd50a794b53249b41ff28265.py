code = """import json
import re

# Load the full JSON result from the file
with open(locals()['var_function-call-12540492671589378295'], 'r') as f:
    civic_docs = json.load(f)

project_data = []

# Regex to capture Project Name and its details block
# This pattern looks for a capitalized line followed by (cid:190) markers
# and captures the project name and its associated content until the next such pattern or end of text.
# Corrected regex for literal newlines and (cid:190) characters.
project_block_pattern = re.compile(
    r'\n\n([A-Z][^\n]{5,100}?(?: Project| Improvements| Plan| Study| Repairs)?)\n'
    r'((?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Project Description:).*?)(?=\n\n[A-Z]|$)',
    re.DOTALL
)

for doc in civic_docs:
    text = doc['text']
    
    # Find all project blocks in the document
    project_blocks = project_block_pattern.findall(text)
    
    for project_name_raw, project_content_raw in project_blocks:
        project_name = project_name_raw.strip()
        project_name = project_name.replace('\ufffd', '')
        project_name = project_name.replace('\u2019', '\'')
        project_name = project_name.replace('\u201c', '\"')
        project_name = project_name.replace('\u201d', '\"')
        project_name = project_name.replace('\u2013', '-')

        # Combine project name and content for keyword search
        full_project_text = project_name.lower() + ' ' + project_content_raw.lower()

        # Extract topic
        topics = []
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
        status = 'N/A'
        if 'design' in full_project_text or 'preliminary design' in full_project_text:
            status = 'design'
        elif 'construction' in full_project_text or 'under construction' in full_project_text:
            status = 'construction'
        elif 'completed' in full_project_text or 'completion filed' in full_project_text:
            status = 'completed'
        elif 'not started' in full_project_text:
            status = 'not started'
        elif 'delayed' in full_project_text:
            status = 'delayed'
            
        # Extract type
        project_type = 'N/A'
        if 'capital improvement projects' in full_project_text:
            project_type = 'capital'
        elif 'disaster recovery projects' in full_project_text:
            project_type = 'disaster'
        
        # Filter for projects related to 'emergency' or 'FEMA'
        if any(keyword in full_project_text for keyword in ['emergency', 'fema']):
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
