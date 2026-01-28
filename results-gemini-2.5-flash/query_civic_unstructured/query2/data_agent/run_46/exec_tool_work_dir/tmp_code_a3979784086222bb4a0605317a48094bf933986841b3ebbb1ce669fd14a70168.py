code = """import json
import re

file_path = locals()['var_function-call-11564623496449314426']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc['text']
    # Split the document into sections based on project type/status
    sections = re.split(r'(Capital Improvement Projects \\(Design\\)|Capital Improvement Projects \\(Construction\\)|Capital Improvement Projects \\(Not Started\\)|Disaster Recovery Projects \\(Construction\\))', text)
    
    current_type_status = ""
    for i, section in enumerate(sections):
        if "Capital Improvement Projects (Design)" in section:
            current_type_status = "capital_design"
        elif "Capital Improvement Projects (Construction)" in section:
            current_type_status = "capital_construction"
        elif "Capital Improvement Projects (Not Started)" in section:
            current_type_status = "capital_not_started"
        elif "Disaster Recovery Projects (Construction)" in section:
            current_type_status = "disaster_construction"
        elif current_type_status:
            # Process project descriptions within each section
            project_blocks = re.split(r'\\n(?=[A-Z][a-zA-Z0-9 \\-\\&\\(\\) ]+?\\n\\(cid:190\\) Updates:)', section)
            for block in project_blocks:
                project_name_match = re.match(r'([A-Z][a-zA-Z0-9 \\-\\&\\(\\) ]+?)\\n\\(cid:190\\) Updates:', block)
                if project_name_match:
                    project_name = project_name_match.group(1).strip()
                    
                    status = ""
                    if "Design" in current_type_status:
                        status = "design"
                    elif "Construction" in current_type_status:
                        status = "construction" 
                    elif "Not Started" in current_type_status:
                        status = "not started"

                    et = ""
                    et_match = re.search(r'Complete (?:Construction|Design|Project):\\s*(.*?)\\n', block)
                    if et_match:
                        et = et_match.group(1).strip()
                    else:
                        et_match = re.search(r'Construction was completed,?\\s*(.*?)(?:\\n|$)', block)
                        if et_match:
                            et = et_match.group(1).strip()
                            status = "completed"

                    
                    # Extract topic based on keywords
                    topic = ""
                    if re.search(r'park|playground|bluffs park', block, re.IGNORECASE):
                        topic = "park"
                    elif re.search(r'road|highway|bridge|street|traffic', block, re.IGNORECASE):
                        topic = "road"
                    elif re.search(r'drain|storm', block, re.IGNORECASE):
                        topic = "drainage"
                    elif re.search(r'fema|fire|emergency', block, re.IGNORECASE):
                        topic = "disaster"
                    elif re.search(r'water treatment', block, re.IGNORECASE):
                        topic = "water treatment"
                    elif re.search(r'signal', block, re.IGNORECASE):
                        topic = "traffic signal"
                    
                    if not status and re.search(r'Project is currently under construction', block):
                        status = "construction"
                    elif not status and re.search(r'Construction was completed', block):
                        status = "completed"
                    
                    
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

env_args = {'var_function-call-6938316003150377742': ['civic_docs'], 'var_function-call-11564623496449314426': 'file_storage/function-call-11564623496449314426.json'}

exec(code, env_args)
