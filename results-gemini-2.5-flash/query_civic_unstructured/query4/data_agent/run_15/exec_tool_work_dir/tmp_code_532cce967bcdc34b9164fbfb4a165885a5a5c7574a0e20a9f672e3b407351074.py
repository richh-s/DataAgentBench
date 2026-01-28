code = """import json
import re

with open(locals()['var_function-call-16078041005392265574'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc['text']
    # Split text into sections based on project type/status
    sections = re.split(r'(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects \(Design\))', text)
    
    current_type = None
    current_status = None
    
    for i, section in enumerate(sections):
        if "Capital Improvement Projects (Design)" in section:
            current_type = "capital"
            current_status = "design"
        elif "Capital Improvement Projects (Construction)" in section:
            current_type = "capital"
            current_status = "construction"
        elif "Capital Improvement Projects (Not Started)" in section:
            current_type = "capital"
            current_status = "not started"
        elif "Disaster Recovery Projects (Design)" in section:
            current_type = "disaster"
            current_status = "design"
        
        if current_type and current_status and i + 1 < len(sections):
            project_text_section = sections[i+1]
            
            # Regex to find project names and their schedules
            project_blocks = re.split(r'\n(?=[A-Z][a-zA-Z0-9\s,&-]+(?:\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\))?(?:\n|\(cid:190\)))', project_text_section)
            
            for block in project_blocks:
                project_name_match = re.match(r'([A-Z][a-zA-Z0-9\s,&-]+(?:\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\))?)', block)
                if project_name_match:
                    project_name = project_name_match.group(1).strip()
                    
                    st_match = re.search(r'Begin (Construction|Work|Project): (.*?)(?=\n|\(cid:131\))', block)
                    st = st_match.group(2).strip() if st_match else None
                    
                    if st:
                        projects.append({'Project_Name': project_name, 'st': st, 'type': current_type, 'status': current_status})

spring_2022_projects = []
for project in projects:
    if project['st'] and any(s in project['st'] for s in ["2022-Spring", "2022-03", "2022-04", "2022-05", "2022-March", "2022-April", "2022-May"]):
        spring_2022_projects.append(project)

result = [p['Project_Name'] for p in spring_2022_projects]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-11597689101478963928': ['civic_docs'], 'var_function-call-16078041005392265574': 'file_storage/function-call-16078041005392265574.json'}

exec(code, env_args)
