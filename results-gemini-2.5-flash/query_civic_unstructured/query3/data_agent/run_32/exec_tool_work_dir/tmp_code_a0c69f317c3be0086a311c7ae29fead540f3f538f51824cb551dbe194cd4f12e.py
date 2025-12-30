code = """import json
import re

# Load the full JSON result from the file
with open(locals()['var_function-call-12540492671589378295'], 'r') as f:
    civic_docs = json.load(f)

project_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Simpler regex to find potential project names followed by updates/schedule/description
    project_name_pattern = re.compile(r'\n\n(.*?)\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Project Description:)', re.DOTALL)
    
    potential_project_names = project_name_pattern.findall(text)
    
    for proj_name_raw in potential_project_names:
        project_name = proj_name_raw.strip().split('\n')[0] # Take the first line as the project name
        project_name = project_name.replace('\ufffd', '') # Remove unicode replacement character
        project_name = project_name.replace('\u2019', '') # Remove smart quote
        project_name = project_name.replace('\u201c', '') # Remove smart quote
        project_name = project_name.replace('\u201d', '') # Remove smart quote
        project_name = project_name.replace('\u2013', '-') # Remove en dash

        # Extract topic - check for keywords in the entire document text
        topics = []
        if 'emergency' in text.lower():
            topics.append('emergency')
        if 'FEMA' in text.lower():
            topics.append('FEMA')
        if 'emergency warning' in text.lower():
            topics.append('emergency warning')
        if '(FEMA Project)' in project_name:
            topics.append('FEMA')
        if 'homeland security' in text.lower():
            topics.append('homeland security')
        if 'disaster' in text.lower():
            topics.append('disaster')
        if not topics:
            topics.append('N/A')
        
        # Extract status - check for keywords in the entire document text
        status = 'N/A'
        if 'design' in text.lower() or 'preliminary design' in text.lower():
            status = 'design'
        if 'construction' in text.lower() or 'under construction' in text.lower():
            status = 'construction'
        if 'completed' in text.lower() or 'completion filed' in text.lower():
            status = 'completed'
        if 'not started' in text.lower():
            status = 'not started'
        if 'delayed' in text.lower():
            status = 'delayed'
        
        # Extract type - check for keywords in the entire document text
        project_type = 'N/A'
        if 'capital improvement projects' in text.lower():
            project_type = 'capital'
        if 'disaster recovery projects' in text.lower():
            project_type = 'disaster'
        
        # Filter for projects related to 'emergency' or 'FEMA' based on the original query
        if any(keyword in text.lower() for keyword in ['emergency', 'fema']):
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
