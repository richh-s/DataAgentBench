code = """import json
import re

with open(locals()['var_function-call-11660002574223514196'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Check if the document itself contains 'emergency' or 'FEMA'
    if re.search(r'emergency|FEMA', text, re.IGNORECASE):
        
        # Split text into sections or lines to look for projects
        # A simple approach: assume project names are on lines ending with "Project" or "Projects"
        # and status is in a subsequent "Updates" or "Status" line
        
        lines = text.split('\n') # Split by actual newline character
        current_project_name = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Heuristic to identify project name: starts with a capital letter and contains "Project"
            # and is likely capitalized
            if re.match(r'^[A-Z][a-zA-Z0-9 &-,/.]+? Project(?:s)?$', line):
                current_project_name = re.sub(r'\\(cid:190\\)|\\(cid:131\\)', '', line).strip()
                
                # Further filter: ensure the project name or its context is related to 'emergency' or 'FEMA'
                # This check is important as the whole document was filtered, but not every project in it
                if not re.search(r'emergency|FEMA|disaster|fire|storm|drainage|repair', current_project_name, re.IGNORECASE):
                    current_project_name = None # Not a relevant project
                    continue
                    
                project_status = 'unknown'
                
                # Look for status in subsequent lines
                for j in range(i + 1, min(i + 5, len(lines))): # Look up to 4 lines ahead
                    sub_line = lines[j].strip()
                    if 'Updates:' in sub_line:
                        status_match = re.search(r'Updates:\s*(.+)', sub_line)
                        if status_match:
                            project_status = status_match.group(1).strip()
                            break # Found status, move to next project
                    elif 'Status:' in sub_line: # Also check for 'Status:'
                        status_match = re.search(r'Status:\s*(.+)', sub_line)
                        if status_match:
                            project_status = status_match.group(1).strip()
                            break

                # Extract topic and type based on keywords
                project_topic = []
                project_type = 'capital' # Default
                
                if re.search(r'FEMA', current_project_name + " " + text, re.IGNORECASE):
                    project_topic.append('FEMA')
                    project_type = 'disaster'
                if re.search(r'emergency', current_project_name + " " + text, re.IGNORECASE):
                    project_topic.append('emergency')
                    project_type = 'disaster' # More likely disaster
                if re.search(r'disaster', current_project_name + " " + text, re.IGNORECASE):
                    project_topic.append('disaster')
                    project_type = 'disaster'
                if re.search(r'fire', current_project_name + " " + text, re.IGNORECASE):
                    project_topic.append('fire')
                    
                project_topic = ', '.join(sorted(list(set(project_topic)))) if project_topic else 'unknown'
                
                extracted_projects.append({
                    'Project_Name': current_project_name,
                    'topic': project_topic,
                    'type': project_type,
                    'status': project_status
                })
                
final_projects_list = []
seen_project_names = set()
for project in extracted_projects:
    cleaned_name = re.sub(r'\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\)', '', project['Project_Name']).strip()
    cleaned_name = re.sub(r'\\(Design\\)|\\(Construction\\)|\\(Not Started\\)', '', cleaned_name).strip()
    cleaned_name = re.sub(r'\\s+', ' ', cleaned_name).strip()
    
    if cleaned_name and cleaned_name not in seen_project_names:
        project['Project_Name'] = cleaned_name
        final_projects_list.append(project)
        seen_project_names.add(cleaned_name)

__RESULT__:
print(json.dumps(list(seen_project_names)))"""

env_args = {'var_function-call-6905336155062781740': ['civic_docs'], 'var_function-call-11660002574223514196': 'file_storage/function-call-11660002574223514196.json'}

exec(code, env_args)
