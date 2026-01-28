code = """import re
import json

docs = json.load(open(locals()['var_function-call-9774842745181215014'], 'r'))
disaster_projects_2022 = []

for doc in docs:
    text = doc['text']
    # Regex to find project names and their details. This is a simplified regex and might need refinement.
    # It looks for lines starting with '(cid:190) ' followed by a potential project name and then schedule information.
    # This pattern also tries to capture the project type and start date.
    projects_in_doc = re.findall(r'(?P<project_name>[A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\s+\(cid:190\)|\s*\(Updates:|\s*\(Project Description:))(.+?)(?=\n\n(?P<next_project>[A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\s+\(cid:190\)|\s*\(Updates:|\s*\(Project Description:))|\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|$)', text, re.DOTALL)
    
    
    # More specific parsing within the extracted project blocks
    for match in re.finditer(r'(?P<project_name>[A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\s+\(cid:190\)|\s*\(Updates:|\s*\(Project Description:))(?P<details>.+?)(?=\n\n[A-Za-z0-9][A-Za-z0-9\s&,-]+?(?:\s+\(cid:190\)|\s*\(Updates:|\s*\(Project Description:))|\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|$)', text, re.DOTALL):
        project_name = match.group('project_name').strip()
        details = match.group('details')
        
        project_type = "capital" # Default type
        if "Disaster Recovery Projects" in text or "Disaster" in project_name or "FEMA" in details or "CalOES" in details:
            project_type = "disaster"
        
        start_date = None
        st_match = re.search(r'(?:Begin Construction|Advertise|Complete Design|Final Design):\s*(.*?2022.*?)', details, re.IGNORECASE)
        if st_match:
            start_date = st_match.group(1).strip()
            
        if project_type == "disaster" and start_date and "2022" in start_date:
            disaster_projects_2022.append(project_name)

print('__RESULT__:')
print(json.dumps(list(set(disaster_projects_2022)))) # Remove duplicates and print"""

env_args = {'var_function-call-3153928930254216863': ['civic_docs'], 'var_function-call-9774842745181215014': 'file_storage/function-call-9774842745181215014.json'}

exec(code, env_args)
