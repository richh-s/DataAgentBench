code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

# Keywords to help identify project names more accurately
project_name_keywords = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall", "Park", "Facility", "Lane", "Signals", "Power", "Treatment", "Signs"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    text_lower = text.lower() # For document-wide keyword search

    current_project = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        line_lower = stripped_line.lower()

        # Attempt to identify a project name. Project names are usually capitalized and might contain specific keywords.
        # We also look for patterns like "Project Description:" or "Updates:" nearby to confirm it's a project.
        is_project_candidate = False
        if re.match(r'^[A-Z][a-zA-Z0-9\s&,-]+', stripped_line) and len(stripped_line) > 5:
            if any(keyword.lower() in line_lower for keyword in project_name_keywords):
                # Check next few lines for 'Updates:', 'Project Schedule:', 'Project Description:' indicators
                for j in range(1, min(5, len(lines) - i)):
                    next_line_lower = lines[i+j].lower()
                    if any(marker in next_line_lower for marker in ["updates:", "project schedule:", "project description:", "estimated schedule:"]): # Adding (cid:190) markers to identify project sections.
                        if "(cid:190)" in lines[i+j]:
                            is_project_candidate = True
                            break
        
        if is_project_candidate:
            project_name = stripped_line.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
            
            # Filter for projects related to 'emergency' or 'FEMA' at the project name level
            if not ('emergency' in project_name.lower() or 'fema' in project_name.lower() or \
                    'emergency' in text_lower or 'fema' in text_lower):
                continue

            # Initialize attributes
            topics = []
            status = 'N/A'
            project_type = 'N/A'

            # Extract topic (checking against the entire document text and project name)
            if 'emergency' in text_lower:
                topics.append('emergency')
            if 'fema' in text_lower:
                topics.append('FEMA')
            if 'emergency warning' in text_lower:
                topics.append('emergency warning')
            if '(fema project)' in project_name.lower():
                topics.append('FEMA')
            if 'homeland security' in text_lower:
                topics.append('homeland security')
            if 'disaster' in text_lower:
                topics.append('disaster')
            if not topics:
                topics.append('N/A')

            # Extract status (from the surrounding text or project name context)
            project_context = " ".join(lines[max(0, i-5):min(len(lines), i+10)]).lower() # Look in a window around the project name

            if 'completed' in project_context or 'completion filed' in project_context:
                status = 'completed'
            elif 'construction' in project_context or 'under construction' in project_context:
                status = 'construction'
            elif 'design' in project_context or 'preliminary design' in project_context:
                status = 'design'
            elif 'not started' in project_context:
                status = 'not started'
            elif 'delayed' in project_context:
                status = 'delayed'
            elif 'construction' in text_lower and 'capital improvement projects (construction)' in text_lower:
                 status = 'construction' # Default to section status if no specific status is found for the project
            elif 'design' in text_lower and 'capital improvement projects (design)' in text_lower:
                 status = 'design' # Default to section status
            elif 'not started' in text_lower and 'capital improvement projects (not started)' in text_lower:
                 status = 'not started' # Default to section status

            # Extract type (from the surrounding text or project name context)
            if 'capital improvement projects' in project_context:
                project_type = 'capital'
            elif 'disaster recovery projects' in project_context:
                project_type = 'disaster'
            elif 'capital' in text_lower and 'projects' in text_lower and 'capital improvement' in text_lower:
                project_type = 'capital'
            elif 'disaster' in text_lower and 'recovery' in text_lower and 'projects' in text_lower:
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
