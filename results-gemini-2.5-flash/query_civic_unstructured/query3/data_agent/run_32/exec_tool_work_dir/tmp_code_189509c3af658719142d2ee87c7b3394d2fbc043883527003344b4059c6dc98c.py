code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

# Keywords to help identify project names more accurately
project_name_keywords = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall", "Park", "Facility", "Lane", "Signals", "Power"]

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Split the document into sections based on typical project section headers or newlines followed by capitalized text
    # This pattern attempts to find logical blocks of text for individual projects
    project_blocks = re.split(r'\n\n(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects.*?|Public Safety Projects.*?|Emergency.*?Projects.*?)\n\n', text, flags=re.DOTALL)
    
    # The first element after split might be introductory text, or an empty string
    # Iterate through the split parts to find actual project sections and their content
    for i in range(1, len(project_blocks), 2): # Iterate over section headers and their content
        section_header = project_blocks[i].strip()
        section_content = project_blocks[i+1].strip()
        full_section_text_lower = (section_header + '\n' + section_content).lower()

        # Now, within each section, try to extract individual project names
        # Project names are often capitalized lines, potentially followed by (cid:190) markers
        project_lines = re.findall(r'\n\n([A-Z][^\n]{5,100}?(?: ' + '|'.join(project_name_keywords) + r')?)\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:)', section_content, re.DOTALL)

        for project_name_raw in project_lines:
            project_name = project_name_raw.strip()
            # Clean up unicode characters and smart quotes
            project_name = project_name.replace('\ufffd', '')
            project_name = project_name.replace('\u2019', "'")
            project_name = project_name.replace('\u201c', '\"')
            project_name = project_name.replace('\u201d', '\"')
            project_name = project_name.replace('\u2013', '-')

            project_name_lower = project_name.lower()

            # Filter for projects related to 'emergency' or 'FEMA' (redundant check, but safer)
            if not ('emergency' in project_name_lower or 'fema' in project_name_lower or \
                    'emergency' in full_section_text_lower or 'fema' in full_section_text_lower):
                continue

            topics = []
            status = 'N/A'
            project_type = 'N/A'

            # Extract topic
            if 'emergency' in full_section_text_lower:
                topics.append('emergency')
            if 'fema' in full_section_text_lower:
                topics.append('FEMA')
            if 'emergency warning' in full_section_text_lower:
                topics.append('emergency warning')
            if '(fema project)' in project_name_lower:
                topics.append('FEMA')
            if 'homeland security' in full_section_text_lower:
                topics.append('homeland security')
            if 'disaster' in full_section_text_lower:
                topics.append('disaster')
            if not topics:
                topics.append('N/A')
            
            # Extract status (from section content or header if available)
            if 'completed' in full_section_text_lower or 'completion filed' in full_section_text_lower:
                status = 'completed'
            elif 'construction' in full_section_text_lower or 'under construction' in full_section_text_lower:
                status = 'construction'
            elif 'design' in full_section_text_lower or 'preliminary design' in full_section_text_lower:
                status = 'design'
            elif 'not started' in full_section_text_lower:
                status = 'not started'
            elif 'delayed' in full_section_text_lower:
                status = 'delayed'
            
            # Extract type (from section header or content)
            if 'capital improvement projects' in section_header.lower() or 'capital improvement projects' in section_content.lower():
                project_type = 'capital'
            elif 'disaster recovery projects' in section_header.lower() or 'disaster recovery projects' in section_content.lower():
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
