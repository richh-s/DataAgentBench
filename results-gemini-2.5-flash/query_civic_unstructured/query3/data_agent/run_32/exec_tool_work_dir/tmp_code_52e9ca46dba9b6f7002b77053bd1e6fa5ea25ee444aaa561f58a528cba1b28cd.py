code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Refined regex to capture a project name followed by any of the (cid:190) markers.
    # Using a single raw string to avoid multi-line string issues.
    # The pattern looks for a newline, then a capitalized phrase (project name),
    # followed by a newline and one of the (cid:190) detail markers.
    project_name_pattern = re.compile(r'\n\n([A-Z][^\n]{5,100}?(?: Project| Improvements| Plan| Study| Repairs| System)?)\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:)', re.DOTALL)
    
    potential_project_names = project_name_pattern.findall(text)
    
    for proj_name_raw in potential_project_names:
        project_name = proj_name_raw.strip()
        project_name = project_name.replace('\ufffd', '') # Remove unicode replacement character
        project_name = project_name.replace('\u2019', "'") # Replace smart quote with regular apostrophe
        project_name = project_name.replace('\u201c', '\"') # Replace smart left double quote
        project_name = project_name.replace('\u201d', '\"') # Replace smart right double quote
        project_name = project_name.replace('\u2013', '-') # Replace en dash

        # Initialize attributes
        topics = []
        status = 'N/A'
        project_type = 'N/A'
        
        # Normalize text for keyword searching
        text_lower = text.lower()
        project_name_lower = project_name.lower()

        # Extract topic
        if 'emergency' in text_lower:
            topics.append('emergency')
        if 'fema' in text_lower:
            topics.append('FEMA')
        if 'emergency warning' in text_lower:
            topics.append('emergency warning')
        if '(fema project)' in project_name_lower:
            topics.append('FEMA')
        if 'homeland security' in text_lower:
            topics.append('homeland security')
        if 'disaster' in text_lower:
            topics.append('disaster')
        if not topics:
            topics.append('N/A')
            
        # Extract status
        if 'completed' in text_lower or 'completion filed' in text_lower:
            status = 'completed'
        elif 'construction' in text_lower or 'under construction' in text_lower:
            status = 'construction'
        elif 'design' in text_lower or 'preliminary design' in text_lower:
            status = 'design'
        elif 'not started' in text_lower:
            status = 'not started'
        elif 'delayed' in text_lower:
            status = 'delayed'
            
        # Extract type
        if 'capital improvement projects' in text_lower:
            project_type = 'capital'
        elif 'disaster recovery projects' in text_lower:
            project_type = 'disaster'
        
        # Filter for projects related to 'emergency' or 'FEMA'
        if any(keyword in project_name_lower or keyword in text_lower for keyword in ['emergency', 'fema']):
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
