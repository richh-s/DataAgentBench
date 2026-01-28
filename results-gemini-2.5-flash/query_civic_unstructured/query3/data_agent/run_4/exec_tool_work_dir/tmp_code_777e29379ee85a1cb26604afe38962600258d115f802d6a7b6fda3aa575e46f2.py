code = """import json
import re

with open(locals()['var_function-call-11660002574223514196'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    # Split the text into sections based on project headings
    project_sections = re.split(r'\n\n[A-Z][a-zA-Z0-9 ]+ Project', text)
    
    # Process the first section before any explicit project heading (might contain general info)
    if project_sections and len(project_sections) > 0:
        # Get potential projects from the first section, looking for known project status or schedule keywords
        first_section_projects = re.findall(r'\n\n(.+?)(?:\n\n\(cid:190\) Updates:|\n\n\(cid:190\) Project Schedule:)', project_sections[0], re.DOTALL)
        for project_name in first_section_projects:
            project_name = project_name.strip()
            if project_name and (re.search(r'emergency', project_name, re.IGNORECASE) or re.search(r'FEMA', project_name, re.IGNORECASE) or re.search(r'disaster', project_name, re.IGNORECASE) or re.search(r'storm', project_name, re.IGNORECASE) or re.search(r'drainage', project_name, re.IGNORECASE) or re.search(r'repair', project_name, re.IGNORECASE)):
                status_match = re.search(r'Status:\s*(.+?)(?:\n|\.)', project_sections[0], re.IGNORECASE)
                status = status_match.group(1).strip() if status_match else 'unknown'
                
                type_match = re.search(r'Capital Improvement Projects and Disaster Recovery Projects Status Report', project_sections[0], re.IGNORECASE)
                project_type = 'disaster' if type_match else 'capital'

                topic_match = re.search(r'emergency|FEMA|disaster|storm|drainage|repair|fire|flood', project_sections[0], re.IGNORECASE)
                topic = topic_match.group(0) if topic_match else 'unknown'

                projects_data.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'type': project_type,
                    'status': status
                })

    # Process each identified project section
    for section in project_sections[1:]: # Skip the first section as it's handled above
        project_name_match = re.match(r'\n\n([A-Z][a-zA-Z0-9 ]+?)(?:\n\n\(cid:190\) Updates:|\n\n\(cid:190\) Project Schedule:)', section, re.DOTALL)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Check for keywords 'emergency' or 'FEMA' in the project section
            if re.search(r'emergency', section, re.IGNORECASE) or re.search(r'FEMA', section, re.IGNORECASE):
                status_match = re.search(r'Updates:\s*(.+?)(?:\n\(cid:190\) Project Schedule:|\n\n|$)', section, re.DOTALL)
                status = status_match.group(1).strip() if status_match else 'unknown'
                
                type_match = re.search(r'Disaster Recovery Projects', text, re.IGNORECASE)
                project_type = 'disaster' if type_match else 'capital'

                topic_match = re.search(r'emergency|FEMA|disaster|storm|drainage|repair|fire|flood', section, re.IGNORECASE)
                topic = topic_match.group(0) if topic_match else 'unknown'

                projects_data.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'type': project_type,
                    'status': status
                })

# Refine project names for better matching and remove duplicates
cleaned_projects = {}
for project in projects_data:
    cleaned_name = re.sub(r'\(cid:190\)', '', project['Project_Name']).strip()
    cleaned_name = re.sub(r'\(cid:131\)', '', cleaned_name).strip()
    cleaned_name = re.sub(r'Project Schedule:\s*', '', cleaned_name).strip()
    cleaned_name = re.sub(r'Updates:\s*', '', cleaned_name).strip()
    
    # Remove common suffixes that appear in project names
    cleaned_name = re.sub(r'\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\)', '', cleaned_name).strip()
    
    # If the project name contains "Capital Improvement Projects" or "Disaster Recovery Projects", extract only the specific project name
    if "Capital Improvement Projects" in cleaned_name:
        specific_project_match = re.search(r'Capital Improvement Projects \((?:Design|Construction|Not Started)\)\n\n(.+)', cleaned_name)
        if specific_project_match:
            cleaned_name = specific_project_match.group(1).split('\n')[0].strip()
            
    if "Disaster Recovery Projects" in cleaned_name:
        specific_project_match = re.search(r'Disaster Recovery Projects \((?:Design|Construction|Not Started)\)\n\n(.+)', cleaned_name)
        if specific_project_match:
            cleaned_name = specific_project_match.group(1).split('\n')[0].strip()

    cleaned_projects[cleaned_name] = {
        'Project_Name': cleaned_name,
        'topic': project['topic'],
        'type': project['type'],
        'status': project['status']
    }

final_projects_list = list(cleaned_projects.values())

__RESULT__:
print(json.dumps(final_projects_list))"""

env_args = {'var_function-call-6905336155062781740': ['civic_docs'], 'var_function-call-11660002574223514196': 'file_storage/function-call-11660002574223514196.json'}

exec(code, env_args)
