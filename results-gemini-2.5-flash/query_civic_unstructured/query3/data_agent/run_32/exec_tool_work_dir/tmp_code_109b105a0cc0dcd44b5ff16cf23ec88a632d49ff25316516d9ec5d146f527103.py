code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_details = []

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Regular expression to broadly capture project information, including multi-line project descriptions.
    # It looks for patterns that indicate a project title (capitalized, certain keywords) and then captures the following content.
    # Using re.DOTALL to allow ' . ' to match newlines within the project content.
    # The pattern tries to identify a project title (line starting with Cap, with keywords) followed by its description (until next similar title or end of doc)
    project_blocks = re.findall(
        r'\n\n([A-Z][^\n]{5,150}?(?: Project| Improvements| Plan| Study| Repairs| System| Road| Drainage| Wall| Master Plan| Park| Skate Park| Facility| Way| Lane| Signals| Power| Treatment| Signs| Emergency| FEMA| Recovery| Center| Slopes| Mitigation)?)\n'
        r'((?:\(cid:190\) (?:Updates:|Project Schedule:|Project Description:|Estimated Schedule:|\(cid:131\)).*?)(?=\n\n[A-Z]|$|\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\n\nEmergency Communications Projects|\n\nPublic Safety Projects))'
        , text, re.DOTALL)
    
    # Iterate through the extracted project blocks
    for project_name_raw, project_content_raw in project_blocks:
        project_name = project_name_raw.strip()
        # Clean up unicode and smart quotes
        project_name = project_name.replace('\ufffd', '')
        project_name = project_name.replace('\u2019', "'")
        project_name = project_name.replace('\u201c', '\"')
        project_name = project_name.replace('\u201d', '\"')
        project_name = project_name.replace('\u2013', '-')

        full_project_text_lower = (project_name.lower() + ' ' + project_content_raw.lower()).replace("\n", " ")

        # Filter for projects related to 'emergency' or 'FEMA'
        if not ('emergency' in full_project_text_lower or 'fema' in full_project_text_lower):
            continue

        topics = []
        status = 'N/A'
        project_type = 'N/A'
        
        # Extract topic
        if 'emergency' in full_project_text_lower: topics.append('emergency')
        if 'fema' in full_project_text_lower: topics.append('FEMA')
        if 'emergency warning' in full_project_text_lower: topics.append('emergency warning')
        if '(fema project)' in project_name.lower(): topics.append('FEMA')
        if 'homeland security' in full_project_text_lower: topics.append('homeland security')
        if 'disaster' in full_project_text_lower: topics.append('disaster')
        if not topics: topics.append('N/A')
            
        # Extract status
        if 'completed' in full_project_text_lower or 'completion filed' in full_project_text_lower: status = 'completed'
        elif 'construction' in full_project_text_lower or 'under construction' in full_project_text_lower: status = 'construction'
        elif 'design' in full_project_text_lower or 'preliminary design' in full_project_text_lower: status = 'design'
        elif 'not started' in full_project_text_lower: status = 'not started'
        elif 'delayed' in full_project_text_lower: status = 'delayed'
            
        # Extract type
        if 'capital improvement projects' in full_project_text_lower: project_type = 'capital'
        elif 'disaster recovery projects' in full_project_text_lower: project_type = 'disaster'
        
        project_details.append({
            'Project_Name': project_name,
            'topic': topics,
            'type': project_type,
            'status': status,
        })

# Remove duplicates based on Project_Name
unique_projects_dict = {project['Project_Name']: project for project in project_details}
final_projects = list(unique_projects_dict.values())

print("__RESULT__:")
print(json.dumps(final_projects, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
