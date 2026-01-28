code = """import json
import re

# Load the full JSON result from the file
with open(locals()['var_function-call-12540492671589378295'], 'r') as f:
    civic_docs = json.load(f)

project_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Regex to capture project names that are often capitalized and followed by a specific pattern
    # The pattern looks for a line starting with an uppercase letter, at least 5 characters long,
    # and potentially ending with common project terms. This line should be followed by a (cid:190) marker.
    # Using r"""...""" for the regex to handle potential internal quotes more easily.
    project_name_pattern = re.compile(
        r"\n\n([A-Z][^\n]{5,100}?(?: Project| Improvements| Plan| Study| Repairs| System)?)\n"
        r"(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:)", 
        re.DOTALL
    )
    
    # Find all potential project names in the document
    potential_project_names = project_name_pattern.findall(text)
    
    for proj_name_raw in potential_project_names:
        project_name = proj_name_raw.strip()
        project_name = project_name.replace('\ufffd', '') # Remove unicode replacement character
        project_name = project_name.replace('\u2019', "'") # Replace smart quote with regular apostrophe
        project_name = project_name.replace('\u201c', '\"') # Replace smart left double quote
        project_name = project_name.replace('\u201d', '\"') # Replace smart right double quote
        project_name = project_name.replace('\u2013', '-') # Replace en dash

        # Extract topic (checking against the entire document text and project name)
        topics = []
        if 'emergency' in text.lower() or 'emergency' in project_name.lower():
            topics.append('emergency')
        if 'fema' in text.lower() or 'fema' in project_name.lower():
            topics.append('FEMA')
        if 'emergency warning' in text.lower():
            topics.append('emergency warning')
        if '(fema project)' in project_name.lower():
            topics.append('FEMA')
        if 'homeland security' in text.lower():
            topics.append('homeland security')
        if 'disaster' in text.lower() or 'disaster' in project_name.lower():
            topics.append('disaster')
        if not topics:
            topics.append('N/A')
            
        # Extract status (checking against the entire document text)
        status = 'N/A'
        if 'completed' in text.lower() or 'completion filed' in text.lower():
            status = 'completed'
        elif 'construction' in text.lower() or 'under construction' in text.lower():
            status = 'construction'
        elif 'design' in text.lower() or 'preliminary design' in text.lower():
            status = 'design'
        elif 'not started' in text.lower():
            status = 'not started'
        elif 'delayed' in text.lower():
            status = 'delayed'
            
        # Extract type (checking against the entire document text)
        project_type = 'N/A'
        if 'capital improvement projects' in text.lower():
            project_type = 'capital'
        elif 'disaster recovery projects' in text.lower():
            project_type = 'disaster'
        
        # Filter for projects related to 'emergency' or 'FEMA'
        if any(keyword in project_name.lower() or keyword in text.lower() for keyword in ['emergency', 'fema']):
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
