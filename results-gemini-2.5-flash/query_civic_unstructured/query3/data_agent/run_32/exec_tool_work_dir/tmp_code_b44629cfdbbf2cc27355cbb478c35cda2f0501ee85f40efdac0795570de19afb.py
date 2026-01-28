code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

# Regular expression to find project names followed by details markers
# This pattern looks for a capitalized line that serves as a project title,
# followed by a newline and a '(cid:190) ' prefix which signals project details.
# It captures the project name.
project_name_and_marker_pattern = re.compile(r'\n\n([A-Z][^\n]{5,100}?(?: Project| Improvements| Plan| Study| Repairs| System| Road| Drainage| Wall| Master Plan| Park| Skate Park| Facility| Way| Lane| Signals| Power| Treatment| Signs| Emergency| FEMA| Recovery| Center| Slopes)?)\n\(cid:190\) (?:Updates:|Project Schedule:|Project Description:|Estimated Schedule:)')

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Find all potential project names and their associated detail lines
    found_projects_with_markers = project_name_and_marker_pattern.findall(text)
    
    processed_project_names_in_doc = set() # To prevent duplicate projects within the same document

    for proj_name_raw in found_projects_with_markers:
        project_name = proj_name_raw.strip()
        # Clean up common unicode and smart quote characters
        project_name = project_name.replace('\ufffd', '')
        project_name = project_name.replace('\u2019', "'")
        project_name = project_name.replace('\u201c', '\"')
        project_name = project_name.replace('\u201d', '\"')
        project_name = project_name.replace('\u2013', '-')
        
        project_name_lower = project_name.lower()

        # Use the whole document text as context for keyword search
        full_context_lower = text_lower # Simplified context for now

        # Filter for projects related to 'emergency' or 'FEMA' as per the query
        if not ('emergency' in project_name_lower or 'fema' in project_name_lower or \
                'emergency' in full_context_lower or 'fema' in full_context_lower):
            continue

        # Skip if this exact project name has already been processed from this document
        if project_name in processed_project_names_in_doc:
            continue
        processed_project_names_in_doc.add(project_name)

        topics = []
        status = 'N/A'
        project_type = 'N/A'
        
        # Extract topic based on project name and document text
        if 'emergency' in full_context_lower: topics.append('emergency')
        if 'fema' in full_context_lower: topics.append('FEMA')
        if 'emergency warning' in full_context_lower: topics.append('emergency warning')
        if '(fema project)' in project_name_lower: topics.append('FEMA')
        if 'homeland security' in full_context_lower: topics.append('homeland security')
        if 'disaster' in full_context_lower: topics.append('disaster')
        if not topics: topics.append('N/A') # Ensure at least one topic is assigned

        # Extract status (searching throughout the document for general status indicators)
        if 'completed' in full_context_lower or 'completion filed' in full_context_lower: status = 'completed'
        elif 'construction' in full_context_lower or 'under construction' in full_context_lower: status = 'construction'
        elif 'design' in full_context_lower or 'preliminary design' in full_context_lower: status = 'design'
        elif 'not started' in full_context_lower: status = 'not started'
        elif 'delayed' in full_context_lower: status = 'delayed'

        # Extract type (searching throughout the document for general type indicators)
        if 'capital improvement projects' in full_context_lower: project_type = 'capital'
        elif 'disaster recovery projects' in full_context_lower: project_type = 'disaster'
        
        project_data.append({
            'Project_Name': project_name,
            'topic': topics,
            'type': project_type,
            'status': status,
        })

# Final deduplication across all documents based on Project_Name (though processed_project_names_in_doc helps, this is a final check)
unique_projects_final = []
seen_project_names_global = set()
for project in project_data:
    if project['Project_Name'] not in seen_project_names_global:
        unique_projects_final.append(project)
        seen_project_names_global.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects_final, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
