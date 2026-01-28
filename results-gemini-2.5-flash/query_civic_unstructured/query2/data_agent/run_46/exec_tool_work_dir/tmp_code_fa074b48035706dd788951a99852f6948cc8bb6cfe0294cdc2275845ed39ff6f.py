code = """import json
import re

file_path = locals()['var_function-call-11564623496449314426']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc['text']
    
    # Use a more flexible regex to find project blocks
    # This looks for a capitalized line (potential project name) followed by updates/schedule
    project_blocks = re.findall(r'([A-Z][a-zA-Z0-9 \\-\\&\\(\\) ]+?)\\n\\(cid:190) Updates:(.*?)(?=\\n[A-Z][a-zA-Z0-9 \\-\\&\\(\\) ]+?\\n\\(cid:190) Updates: |$)', text, re.DOTALL)
    
    for name, details in project_blocks:
        project_name = name.strip()
        
        status = ""
        et = ""
        
        # Check for completion status and date
        if re.search(r'Construction was completed,?\\s*(.*?)(?:\\n|$)', details):
            status = "completed"
            et_match = re.search(r'Construction was completed,?\\s*(.*?)(?:\\n|$)', details)
            if et_match:
                et = et_match.group(1).strip()
        elif re.search(r'Complete (?:Construction|Design|Project):\\s*(.*?)(?:\\n|$)', details):
            et_match = re.search(r'Complete (?:Construction|Design|Project):\\s*(.*?)(?:\\n|$)', details)
            if et_match:
                et = et_match.group(1).strip()
        
        # Extract topic based on keywords
        topic = ""
        if re.search(r'park|playground|bluffs park', details, re.IGNORECASE):
            topic = "park"
        elif re.search(r'road|highway|bridge|street|traffic', details, re.IGNORECASE):
            topic = "road"
        elif re.search(r'drain|storm', details, re.IGNORECASE):
            topic = "drainage"
        elif re.search(r'fema|fire|emergency', details, re.IGNORECASE):
            topic = "disaster"
        elif re.search(r'water treatment', details, re.IGNORECASE):
            topic = "water treatment"
        elif re.search(r'signal', details, re.IGNORECASE):
            topic = "traffic signal"
        
        projects.append({
            "Project_Name": project_name,
            "topic": topic,
            "status": status,
            "et": et
        })

park_projects_2022_completed = []
for project in projects:
    if project['topic'] == 'park' and project['status'] == 'completed' and '2022' in project['et']:
        park_projects_2022_completed.append(project['Project_Name'])

print('__RESULT__:')
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-6938316003150377742': ['civic_docs'], 'var_function-call-11564623496449314426': 'file_storage/function-call-11564623496449314426.json', 'var_function-call-7034731746954393111': [], 'var_function-call-5088907466810494931': ['Funding'], 'var_function-call-16550090818495668891': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'Point Dume Walkway Repairs', 'Amount': '59000'}]}

exec(code, env_args)
