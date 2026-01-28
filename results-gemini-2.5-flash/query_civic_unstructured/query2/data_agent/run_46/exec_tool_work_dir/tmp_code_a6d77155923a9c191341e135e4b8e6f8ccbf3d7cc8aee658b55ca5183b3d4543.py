code = """import json
import re

file_path = locals()['var_function-call-11564623496449314426']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Regex to find project blocks. It looks for a project name (capitalized, potentially with numbers/symbols),
    # followed by '(cid:190) Updates:' and then captures everything until the next project or end of document.
    project_blocks = re.findall(r'([A-Z][a-zA-Z0-9 \\-\\&() ]+?)\\n\\(cid:190\\) Updates:(.*?)(?=\\n[A-Z][a-zA-Z0-9 \\-\\&() ]+?\\n\\(cid:190\\) Updates:|$)', text, re.DOTALL)

    for project_name_raw, details_block in project_blocks:
        project_name = project_name_raw.strip()
        
        status = ""
        et = ""
        
        # Check for completion status and date
        completion_match = re.search(r'Construction was completed,?\\s*(.*?)(?:\\n|$)', details_block)
        if completion_match:
            status = "completed"
            et = completion_match.group(1).strip()
        else:
            # If not explicitly 'completed', look for 'Complete Construction/Design/Project' for an end date
            et_match = re.search(r'Complete (?:Construction|Design|Project):\\s*(.*?)(?:\\n|$)', details_block)
            if et_match:
                et = et_match.group(1).strip()
                # We don't set status here, as 'Complete Design' doesn't mean the project is completed

        # Extract topic based on keywords from the details block AND project name
        topic = ""
        if re.search(r'park|playground|bluffs park', details_block + project_name, re.IGNORECASE):
            topic = "park"
        elif re.search(r'road|highway|bridge|street|traffic', details_block + project_name, re.IGNORECASE):
            topic = "road"
        elif re.search(r'drain|storm', details_block + project_name, re.IGNORECASE):
            topic = "drainage"
        elif re.search(r'fema|fire|emergency', details_block + project_name, re.IGNORECASE):
            topic = "disaster"
        elif re.search(r'water treatment', details_block + project_name, re.IGNORECASE):
            topic = "water treatment"
        elif re.search(r'signal', details_block + project_name, re.IGNORECASE):
            topic = "traffic signal"

        projects_data.append({
            "Project_Name": project_name,
            "topic": topic,
            "status": status,
            "et": et
        })

park_projects_2022_completed_names = []
for project in projects_data:
    if project['topic'] == 'park' and project['status'] == 'completed' and '2022' in project['et']:
        park_projects_2022_completed_names.append(project['Project_Name'])

# Filter out duplicates since the regex might pick up variations of the same project name or details
park_projects_2022_completed_names = list(set(park_projects_2022_completed_names))

print('__RESULT__:')
print(json.dumps(park_projects_2022_completed_names))"""

env_args = {'var_function-call-6938316003150377742': ['civic_docs'], 'var_function-call-11564623496449314426': 'file_storage/function-call-11564623496449314426.json', 'var_function-call-7034731746954393111': [], 'var_function-call-5088907466810494931': ['Funding'], 'var_function-call-16550090818495668891': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'Point Dume Walkway Repairs', 'Amount': '59000'}]}

exec(code, env_args)
