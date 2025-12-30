code = """import json
import re

with open(locals()['var_function-call-5224027569778701662'], 'r') as f:
    civic_docs = json.load(f)

projects_spring_2022 = {}

for doc_info in civic_docs:
    text = doc_info['text']
    
    # Regex to find project names and their schedules, specifically looking for 'Begin Construction' or 'Project Schedule'
    # and then capturing a project name and a date that includes '2022-Spring' or '2022' and one of 'March', 'April', 'May'
    project_pattern = r"(?P<project_name>[A-Za-z0-9&,\- ]+?)(?:\n|\r|\t|\s)*\(cid:190\)(?:\n|\r|\t|\s)*Project Schedule:(?:\n|\r|\t|\s)*\(cid:131\)(?:\n|\r|\t|\s)*(?:Begin Construction|Advertise|Complete Design|Final Design|Estimated Schedule):\s*(?P<start_date>(?:Spring|March|April|May)\s*2022|2022\s*-\s*(?:Spring|03|04|05))"
    
    matches = re.finditer(project_pattern, text, re.IGNORECASE)
    
    for match in matches:
        project_name = match.group('project_name').strip()
        start_date = match.group('start_date').strip()
        
        # Further refine to ensure it's Spring 2022
        if "2022" in start_date and ("spring" in start_date.lower() or "march" in start_date.lower() or "april" in start_date.lower() or "may" in start_date.lower() or "03" in start_date or "04" in start_date or "05" in start_date):
            projects_spring_2022[project_name] = start_date

# Convert the dictionary keys to a list of project names
project_names = list(projects_spring_2022.keys())

print('__RESULT__:')
print(json.dumps(project_names))"""

env_args = {'var_function-call-5224027569778701662': 'file_storage/function-call-5224027569778701662.json'}

exec(code, env_args)
