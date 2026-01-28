code = """import json
import re

def extract_project_info(text):
    projects = []
    # Regex to find project sections
    # Changed r'\\n\\n' to r'\n\n' to match actual newlines
    project_sections = re.split(r'\n\n(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)', text)

    current_status_type = None
    for i, section in enumerate(project_sections):
        if 'Capital Improvement Projects' in section or 'Disaster Recovery Projects' in section:
            current_status_type = section.strip()
            continue
        
        if current_status_type and section.strip():
            # Split by project to process each project individually within a section
            # Changed r'\\n\\n' to r'\n\n'
            project_blocks = re.split(r'\n\n([A-Za-z0-9][A-Za-z0-9 ]+ Project)', section)
            
            project_name_candidate = None
            for j, block in enumerate(project_blocks):
                # Adjusted the condition to check if the block itself starts with a project name pattern
                if j == 0 and not re.match(r'([A-Za-z0-9][A-Za-z0-9 ]+ Project)', block.strip()):
                    continue

                if re.match(r'([A-Za-z0-9][A-Za-z0-9 ]+ Project)', block.strip()):
                    project_name_candidate = block.strip()
                elif project_name_candidate:
                    project_info = {}
                    project_info['Project_Name'] = project_name_candidate
                    
                    # Extract status from the section header if available
                    if 'Design' in current_status_type:
                        project_info['status'] = 'design'
                    elif 'Construction' in current_status_type:
                        project_info['status'] = 'construction'
                    elif 'Not Started' in current_status_type:
                        project_info['status'] = 'not started'
                    
                    # Extract type
                    if 'Disaster Recovery Projects' in current_status_type:
                        project_info['type'] = 'disaster'
                    elif 'Capital Improvement Projects' in current_status_type:
                        project_info['type'] = 'capital'
                    
                    # Extract topic based on keywords in the text
                    topics = []
                    if re.search(r'FEMA', block, re.IGNORECASE):
                        topics.append('FEMA')
                    if re.search(r'emergency', block, re.IGNORECASE):
                        topics.append('emergency')
                    if re.search(r'fire', block, re.IGNORECASE):
                        topics.append('fire')
                    if re.search(r'CalOES', block, re.IGNORECASE):
                        topics.append('CalOES')
                    if re.search(r'storm drain', block, re.IGNORECASE):
                        topics.append('storm drain')
                    if re.search(r'drainage', block, re.IGNORECASE):
                        topics.append('drainage')
                    if re.search(r'warning', block, re.IGNORECASE):
                        topics.append('emergency warning')
                    

                    # If project name contains FEMA, CalJPIA, CalOES, add to topic
                    if re.search(r'\(FEMA Project\)', project_name_candidate, re.IGNORECASE):
                        if 'FEMA' not in topics:
                            topics.append('FEMA')
                    if re.search(r'\(CalJPIA Project\)', project_name_candidate, re.IGNORECASE):
                        if 'CalJPIA' not in topics:
                            topics.append('CalJPIA')
                    if re.search(r'\(CalOES Project\)', project_name_candidate, re.IGNORECASE):
                        if 'CalOES' not in topics:
                            topics.append('CalOES')
                    
                    # Updates for status from the text
                    if re.search(r'Updates: Project is currently under construction', block, re.IGNORECASE):
                        project_info['status'] = 'construction'
                    if re.search(r'Updates: Construction was completed', block, re.IGNORECASE):
                        project_info['status'] = 'completed'
                    if re.search(r'Updates: Project is in the preliminary design phase', block, re.IGNORECASE):
                        project_info['status'] = 'design'

                    if topics:
                        project_info['topic'] = ', '.join(sorted(list(set(topics)))) # remove duplicates and sort
                    else:
                        project_info['topic'] = 'N/A' # Default if no specific topic found

                    projects.append(project_info)
                    project_name_candidate = None # Reset for next project
    return projects

all_projects = []
with open(locals()['var_function-call-587439024112713590'], 'r') as f:
    data = json.load(f)

for doc in data:
    extracted = extract_project_info(doc['text'])
    all_projects.extend(extracted)

# Filter for 'emergency' or 'FEMA' in topic
filtered_projects = [
    p for p in all_projects 
    if any(keyword in p.get('topic', '').lower() for keyword in ['emergency', 'fema'])
]

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for project in filtered_projects:
    if project['Project_Name'] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

# Convert to JSON string
result = json.dumps(unique_projects)

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-6676072026141712734': ['civic_docs'], 'var_function-call-587439024112713590': 'file_storage/function-call-587439024112713590.json'}

exec(code, env_args)
