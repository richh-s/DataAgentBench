code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

park_projects = []

for doc in civic_docs:
    text = doc['text']
    project_pattern = re.compile(r'\n\n([A-Z][a-zA-Z0-9&\s\-]+(?:Park|Playground)(?:\sProject)?)\n(?:\(cid:190\)\sUpdates:.*?(?=\n\n[A-Z][a-zA-Z0-9&\s\-]+(?:Park|Playground)|$)|\n\(cid:190\)\sProject\sDescription:.*?(?=\n\n[A-Z][a-zA-Z0-9&\s\-]+(?:Park|Playground)|$)|\n\(cid:190\)\sEstimated\sSchedule:.*?(?=\n\n[A-Z][a-zA-Z0-9&\s\-]+(?:Park|Playground)|$)|\n\(cid:190\)\sProject\sSchedule:.*?(?=\n\n[A-Z][a-zA-Z0-9&\s\-]+(?:Park|Playground)|$))', re.DOTALL)
    
    for match in project_pattern.finditer(text):
        project_name = match.group(1).strip()
        project_details = match.group(0) # Get the entire matched block for details

        # Extract status
        status_match = re.search(r'Updates: (.*?(?:completed|under construction|is in the preliminary design phase|is currently out to bid))', project_details)
        status = status_match.group(1).strip() if status_match else 'N/A'

        # Extract end date
        et_match = re.search(r'Complete (?:Construction|Design): (\w+ \d{4}|\d{4})', project_details)
        et = et_match.group(1).strip() if et_match else 'N/A'
        
        # Check for 'park' or 'playground' in the project name itself as a primary topic indicator
        if 'Park' in project_name or 'Playground' in project_name:
            park_projects.append({'Project_Name': project_name, 'status': status, 'et': et})

filtered_projects = []
for project in park_projects:
    if project['status'] and 'completed' in project['status'].lower() and project['et'] and '2022' in project['et']:
        filtered_projects.append(project['Project_Name'])
        

print("__RESULT__:")
print(json.dumps(filtered_projects)))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json'}

exec(code, env_args)
