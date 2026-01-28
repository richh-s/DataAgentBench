code = """import json
import re

def extract_project_info_final_v3(text):
    projects = []
    # Split by literal newline, ensuring escaping is correct for the Python string itself
    lines = text.split('\n')
    current_project = None
    
    global_disaster_context = "Disaster Recovery Projects" in text

    for i, line in enumerate(lines):
        line = line.strip()
        
        # Regex for project name. Pattern: '^(.*?Project(?:\\s*\\(.*?\\))?)$'
        # Each backslash within the regex is already part of the Python string, 
        # so they need to be escaped as '\\' for the Python interpreter to see them as '\'.
        # However, the string itself is within the tool call's '''...''', so the tool's parser
        # also needs to see '\\' as a single backslash for the Python string literal.
        # This means we need '^(.*?Project(?:\\\\s*\\\\(.*?\\\\))?)$' if not a raw string,
        # or r'^(.*?Project(?:\s*\(.*?\))?)$' with an r prefix.
        # Given the persistent 'unterminated string literal', let's simplify regex 
        # for project name recognition and try to avoid complex groups for now in regex literals.
        
        # Simplified project name recognition: ends with 'Project' and is on its own line or starts a line
        project_name_match = re.match(r'^(.*?Project(?:\s*\(FEMA Project\))?)$|'
                                      r'^(.*?Project(?:\s*\(CalJPIA Project\))?)$|'
                                      r'^(.*?Project(?:\s*\(CalOES Project\))?)$|'
                                      r'^(.*?Project)$', line)
        
        if project_name_match and len(line) > 10 and not line.isupper() and "(" not in line and ")" not in line[line.find("Project"):]:
            if current_project:
                projects.append(current_project)
            
            # Extract the actual project name, handling the multiple groups from the ORed regex
            project_name = next((g.strip() for g in project_name_match.groups() if g), None)
            if project_name: # Ensure a name was captured
                current_project = {
                    "Project_Name": project_name,
                    "type": "capital",
                    "st": None
                }
                # Check for disaster keywords in the project name itself
                if "FEMA Project" in project_name or "CalJPIA Project" in project_name or "CalOES Project" in project_name:
                    current_project["type"] = "disaster"
                continue

        if current_project:
            if current_project["type"] == "capital" and ("FEMA" in line or "CalOES" in line or "Disaster Recovery" in line):
                current_project["type"] = "disaster"

            if "(cid:190) Project Schedule:" in line:
                for j in range(i + 1, min(i + 5, len(lines))):
                    schedule_detail_line = lines[j].strip()
                    
                    begin_construction_match = re.search(r'Begin Construction:\s*([^\n]+)', schedule_detail_line)
                    if begin_construction_match:
                        current_project["st"] = begin_construction_match.group(1).strip()
                        break
                    
                    advertise_match = re.search(r'Advertise:\s*([^\n]+)', schedule_detail_line)
                    if advertise_match:
                        current_project["st"] = advertise_match.group(1).strip()
                        break
                    
                    date_match = re.search(r'\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b', schedule_detail_line)
                    if date_match:
                        current_project["st"] = date_match.group(0).strip()
                        break
    
    if current_project:
        projects.append(current_project)

    for project in projects:
        if project["type"] == "capital" and global_disaster_context:
            project["type"] = "disaster"

    return projects

file_path = locals()['var_function-call-6524522302801542169']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects = []
for doc in data:
    projects_in_doc = extract_project_info_final_v3(doc['text'])
    all_projects.extend(projects_in_doc)

disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in str(project['st']):
        disaster_projects_2022.append(project)

unique_project_names = list(set([project['Project_Name'] for project in disaster_projects_2022]))

unique_project_names = [name for name in unique_project_names if len(name) > 10 and not name.isupper()]

print("__RESULT__:")
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json', 'var_function-call-17434838567716078401': ['Funding'], 'var_function-call-7943208518371631309': 'file_storage/function-call-7943208518371631309.json'}

exec(code, env_args)
