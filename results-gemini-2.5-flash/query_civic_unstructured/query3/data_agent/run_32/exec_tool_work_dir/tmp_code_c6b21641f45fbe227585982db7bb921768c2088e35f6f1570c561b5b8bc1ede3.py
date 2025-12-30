code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

# Regex to identify major project sections (Capital Improvement, Disaster Recovery etc.)
# Using a raw string with triple quotes to avoid issues with backslashes and single quotes.
section_pattern = re.compile(
    r"""(Capital Improvement Projects \((?:Design|Construction|Not Started)\)|"
    r"Disaster Recovery Projects|Projects Under Design|Emergency Warning Projects|"
    r"Emergency Communications Projects|Homeland Security Projects|"
    r"Emergency Operations Center Projects|Fire Department Projects|"
    r"Sheriff's Department Projects|Public Safety Projects|"
    r"Emergency Preparedness Projects)\n\n(.*?)(?=\n\n(?:Capital Improvement Projects|Disaster Recovery Projects|Projects Under Design|"
    r"Emergency Warning Projects|Emergency Communications Projects|Homeland Security Projects|"
    r"Emergency Operations Center Projects|Fire Department Projects|Sheriff's Department Projects|"
    r"Public Safety Projects|Emergency Preparedness Projects|\Z))""", re.DOTALL)

for doc in civic_docs:
    text = doc['text']
    text_lower = text.lower()
    
    # Find all major project sections
    project_sections = section_pattern.findall(text)
    
    for section_header, section_content in project_sections:
        section_header_lower = section_header.lower()
        section_content_lower = section_content.lower()
        
        # Regex to find individual project names within each section
        # Project names are usually preceded by \n\n and followed by (cid:190) marker.
        project_name_pattern = re.compile(r'\n\n(.*?)\n\(cid:190\) (?:Updates:|Project Schedule:|Project Description:|Estimated Schedule:)', re.DOTALL)
        projects_in_section = project_name_pattern.findall(section_content)
        
        for proj_name_raw in projects_in_section:
            project_name = proj_name_raw.strip().split('\n')[0] # Take the first line as the project name
            
            # Clean up the project name
            project_name = project_name.replace('\ufffd', '')
            project_name = project_name.replace('\u2019', "'")
            project_name = project_name.replace('\u201c', '\"')
            project_name = project_name.replace('\u201d', '\"')
            project_name = project_name.replace('\u2013', '-')

            # Normalize project name for keyword search
            project_name_lower = project_name.lower()

            # Filter for projects related to 'emergency' or 'FEMA'
            if not ('emergency' in project_name_lower or 'fema' in project_name_lower or 
                    'emergency' in section_header_lower or 'fema' in section_header_lower or 
                    'emergency' in section_content_lower or 'fema' in section_content_lower):
                continue

            # Initialize attributes
            topics = []
            status = 'N/A'
            project_type = 'N/A'
            
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
            if 'completed' in section_content_lower or 'completion filed' in section_content_lower:
                status = 'completed'
            elif 'construction' in section_content_lower or 'under construction' in section_content_lower:
                status = 'construction'
            elif 'design' in section_content_lower or 'preliminary design' in section_content_lower:
                status = 'design'
            elif 'not started' in section_content_lower:
                status = 'not started'
            elif 'delayed' in section_content_lower:
                status = 'delayed'
            elif 'design' in section_header_lower:
                status = 'design'
            elif 'construction' in section_header_lower:
                status = 'construction'
            elif 'not started' in section_header_lower:
                status = 'not started'

            # Extract type
            if 'capital improvement projects' in section_header_lower:
                project_type = 'capital'
            elif 'disaster recovery projects' in section_header_lower:
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
