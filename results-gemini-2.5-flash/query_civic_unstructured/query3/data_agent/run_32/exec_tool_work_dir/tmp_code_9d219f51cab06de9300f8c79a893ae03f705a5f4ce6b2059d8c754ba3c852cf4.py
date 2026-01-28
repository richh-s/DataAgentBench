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
    
    # Search for project names using a pattern that looks for a line followed by a (cid:190) marker
    # This pattern is more generic and tries to capture project titles before bullet points.
    project_line_pattern = re.compile(r'\n\n(.*?)\n\(cid:190\) (?:Updates:|Project Schedule:|Project Description:|Estimated Schedule:)', re.DOTALL)
    
    # Find all matches in the text
    matches = project_line_pattern.findall(text)
    
    for match_group in matches:
        # The project name is typically the first group captured
        project_name = match_group.strip()
        project_name = project_name.split('\n')[0] # Take only the first line as the name
        
        # Clean up the project name
        project_name = project_name.replace('\ufffd', '') # Remove unicode replacement character
        project_name = project_name.replace('\u2019', "'") # Replace smart quote with regular apostrophe
        project_name = project_name.replace('\u201c', '\"') # Replace smart left double quote
        project_name = project_name.replace('\u201d', '\"') # Replace smart right double quote
        project_name = project_name.replace('\u2013', '-') # Replace en dash

        # Ensure we only process projects relevant to 'emergency' or 'FEMA'
        if not ('emergency' in project_name.lower() or 'fema' in project_name.lower() or \
                'emergency' in text_lower or 'fema' in text_lower):
            continue

        # Initialize attributes
        topics = []
        status = 'N/A'
        project_type = 'N/A'
        
        # Extract topic based on project name and document text
        if 'emergency' in text_lower:
            topics.append('emergency')
        if 'fema' in text_lower:
            topics.append('FEMA')
        if 'emergency warning' in text_lower:
            topics.append('emergency warning')
        if '(fema project)' in project_name.lower():
            topics.append('FEMA')
        if 'homeland security' in text_lower:
            topics.append('homeland security')
        if 'disaster' in text_lower:
            topics.append('disaster')
        if not topics:
            topics.append('N/A')
            
        # Extract status based on document text
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
            
        # Extract type based on document text
        if 'capital improvement projects' in text_lower:
            project_type = 'capital'
        elif 'disaster recovery projects' in text_lower:
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
