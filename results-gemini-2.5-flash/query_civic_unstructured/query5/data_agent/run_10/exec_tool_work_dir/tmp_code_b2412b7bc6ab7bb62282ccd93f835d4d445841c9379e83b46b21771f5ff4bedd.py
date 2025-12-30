code = """import re
import json

docs = json.load(open(locals()['var_function-call-9774842745181215014'], 'r'))
disaster_projects_2022 = []

for doc in docs:
    text = doc['text']

    # Regex to find project blocks: Project Name followed by (cid:190) and details
    # This pattern captures the project name and all subsequent details until the next project or a major section break.
    project_pattern = r'(?P<project_name>[A-Za-z0-9][A-Za-z0-9\s&,-]+?)\n\(cid:190\)(?P<details>.+?)(?=\n[A-Za-z0-9][A-Za-z0-9\s&,-]+?\n\(cid:190\)|\n\nCapital Improvement Projects \(|\n\nDisaster Recovery Projects|\Z)'
    
    for match in re.finditer(project_pattern, text, re.DOTALL):
        project_name = match.group('project_name').strip()
        details = match.group('details')
        
        project_type = "capital" # Default type
        # Check for disaster keywords in project name or details
        if "Disaster" in project_name or "disaster" in details or "FEMA" in details or "CalOES" in details or "CalJPIA" in details:
            project_type = "disaster"
        
        start_date_in_2022 = False
        # Look for start date indicators mentioning '2022'
        # Keywords like 'Begin Construction', 'Advertise', 'Project Schedule', 'Estimated Schedule', 'Scheduled for', 'planning'
        # followed by a year '2022' or a season 'Spring 2022', etc.
        if re.search(r'(?:Begin Construction|Advertise|Project Schedule|Estimated Schedule|Scheduled for|planning|Complete Design|Final Design)[:-]?\s*(?:[A-Za-z]+\s+)?(?:2022|Fall\s*2022|Spring\s*2022|Summer\s*2022|Winter\s*2022|early\s*2022|mid\s*2022|late\s*2022)', details, re.IGNORECASE):
            start_date_in_2022 = True
        
        if project_type == "disaster" and start_date_in_2022:
            disaster_projects_2022.append(project_name)

print('__RESULT__:')
print(json.dumps(list(set(disaster_projects_2022)))) # Remove duplicates and print"""

env_args = {'var_function-call-3153928930254216863': ['civic_docs'], 'var_function-call-9774842745181215014': 'file_storage/function-call-9774842745181215014.json'}

exec(code, env_args)
