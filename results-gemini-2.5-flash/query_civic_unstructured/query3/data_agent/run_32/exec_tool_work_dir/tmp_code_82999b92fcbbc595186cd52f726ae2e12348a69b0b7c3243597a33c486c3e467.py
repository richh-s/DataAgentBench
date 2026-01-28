code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_details = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    text_lower = text.lower()

    # Iterate through each line to find relevant project information
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        line_lower = stripped_line.lower()

        # Check if the line contains 'emergency' or 'FEMA' as a primary filter
        if 'emergency' in line_lower or 'fema' in line_lower:
            project_name = stripped_line.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
            project_name_lower = project_name.lower()

            topics = []
            status = 'N/A'
            project_type = 'N/A'

            # Extract topic based on the line and overall document text
            if 'emergency' in line_lower: topics.append('emergency')
            if 'fema' in line_lower: topics.append('FEMA')
            if 'emergency warning' in line_lower: topics.append('emergency warning')
            if '(fema project)' in project_name_lower: topics.append('FEMA')
            if 'homeland security' in line_lower: topics.append('homeland security')
            if 'disaster' in line_lower: topics.append('disaster')
            if not topics: # Fallback to document-wide topics if not found in the specific line
                if 'emergency' in text_lower: topics.append('emergency')
                if 'fema' in text_lower: topics.append('FEMA')
            if not topics: topics.append('N/A')
            
            # Extract status (searching broadly in the document for indicators)
            if 'completed' in text_lower or 'completion filed' in text_lower: status = 'completed'
            elif 'construction' in text_lower or 'under construction' in text_lower: status = 'construction'
            elif 'design' in text_lower or 'preliminary design' in text_lower: status = 'design'
            elif 'not started' in text_lower: status = 'not started'
            elif 'delayed' in text_lower: status = 'delayed'

            # Extract type (searching broadly in the document for indicators)
            if 'capital improvement projects' in text_lower: project_type = 'capital'
            elif 'disaster recovery projects' in text_lower: project_type = 'disaster'
            
            project_details.append({
                'Project_Name': project_name,
                'topic': topics,
                'type': project_type,
                'status': status,
            })

# Deduplicate projects based on Project_Name (keeping the first occurrence)
unique_projects_dict = {}
for project in project_details:
    if project['Project_Name'] not in unique_projects_dict:
        unique_projects_dict[project['Project_Name']] = project

final_projects = list(unique_projects_dict.values())

print("__RESULT__:")
print(json.dumps(final_projects, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
