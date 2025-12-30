code = """import json
import re

# Load the full JSON result from the file
with open(locals()['var_function-call-12540492671589378295'], 'r') as f:
    civic_docs = json.load(f)

project_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Regex to find project names and their descriptions, statuses, and types
    # Projects are often listed under 'Capital Improvement Projects (Design)', 'Disaster Recovery Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)'
    # and have 'Updates', 'Project Schedule', 'Project Description' sections.
    
    # Define patterns for different sections and project types/statuses
    project_section_pattern = re.compile(r'(Capital Improvement Projects \((?:Design|Construction|Not Started)\)|Disaster Recovery Projects|Projects Under Design|Emergency Warning Projects|Disaster Recovery Projects \(Design\)|Emergency Communications Projects|Homeland Security Projects|Emergency Operations Center Projects|Fire Department Projects|Sheriff's Department Projects|Public Safety Projects|Emergency Preparedness Projects)\n\n(.*?)(?=\n\n(?:Capital Improvement Projects|Disaster Recovery Projects|Projects Under Design|Emergency Warning Projects|Emergency Communications Projects|Homeland Security Projects|Emergency Operations Center Projects|Fire Department Projects|Sheriff's Department Projects|Public Safety Projects|Emergency Preparedness Projects|\Z))', re.DOTALL)
    
    project_sections = project_section_pattern.findall(text)
    
    for section_header, section_content in project_sections:
        # Further parse the content within each section to extract individual projects
        # Project names are usually followed by (cid:190) Updates:, (cid:190) Project Schedule:, or (cid:190) Project Description:
        project_detail_pattern = re.compile(r'\n\n(.*?)\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Project Description:)', re.DOTALL)
        
        projects_in_section = project_detail_pattern.findall(section_content)
        
        for proj_name_raw in projects_in_section:
            project_name = proj_name_raw.strip().split('\n')[0] # Take the first line as the project name
            project_name = project_name.replace('\ufffd', '') # Remove unicode replacement character
            project_name = project_name.replace('\u2019', '') # Remove smart quote
            project_name = project_name.replace('\u201c', '') # Remove smart quote
            project_name = project_name.replace('\u201d', '') # Remove smart quote
            project_name = project_name.replace('\u2013', '-') # Remove en dash

            # Extract topic
            topics = []
            if 'emergency' in text.lower():
                topics.append('emergency')
            if 'FEMA' in text.lower():
                topics.append('FEMA')
            if 'emergency warning' in text.lower():
                topics.append('emergency warning')
            if '(FEMA Project)' in project_name:
                topics.append('FEMA')
            if 'homeland security' in section_header.lower() or 'homeland security' in text.lower():
                topics.append('homeland security')
            if 'disaster' in section_header.lower() or 'disaster' in text.lower():
                topics.append('disaster')
            if not topics:
                topics.append('N/A')
            
            # Extract status
            status = 'N/A'
            if 'design' in section_header.lower() or 'preliminary design' in text.lower():
                status = 'design'
            elif 'construction' in section_header.lower() or 'under construction' in text.lower():
                status = 'construction'
            elif 'completed' in text.lower() or 'completion filed' in text.lower():
                status = 'completed'
            elif 'not started' in section_header.lower() or 'not started' in text.lower():
                status = 'not started'
            elif 'delayed' in text.lower():
                status = 'delayed'
            
            # Extract type
            project_type = 'N/A'
            if 'capital improvement projects' in section_header.lower():
                project_type = 'capital'
            elif 'disaster recovery projects' in section_header.lower():
                project_type = 'disaster'
            
            # Filter for projects related to 'emergency' or 'FEMA'
            if 'emergency' in '\n'.join([project_name, section_content]).lower() or 'fema' in '\n'.join([project_name, section_content]).lower():
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
