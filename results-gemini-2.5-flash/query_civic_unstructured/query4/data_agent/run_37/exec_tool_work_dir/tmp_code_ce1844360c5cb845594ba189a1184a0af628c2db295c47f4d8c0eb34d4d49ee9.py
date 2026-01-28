code = """import re
import json

def extract_projects(text):
    projects = []
    project_blocks = re.split(r'''\n\n(?=[A-Z][A-Za-z0-9_ -]+Project(?:\n|$))''', text)
    
    current_type = ''
    current_status = ''

    for block in project_blocks:
        if 'Capital Improvement Projects (Design)' in block:
            current_type = 'capital'
            current_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in block:
            current_type = 'capital'
            current_status = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in block:
            current_type = 'capital'
            current_status = 'not started'
        elif 'Disaster Recovery Projects' in block:
            current_type = 'disaster'
            current_status = '' # status varies within disaster projects

        project_name_match = re.search(r'''\n([A-Z][A-Za-z0-9_ -]+Project(?:\n|$|\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\)))''', block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            project_info = {
                'Project_Name': project_name,
                'type': current_type,
                'status': current_status
            }

            st_match = re.search(r'Begin Construction: ([A-Za-z0-9_ -]+)', block)
            if st_match:
                project_info['st'] = st_match.group(1).strip()
            else:
                st_match = re.search(r'Begin construction: ([A-Za-z0-9_ -]+)', block)
                if st_match:
                    project_info['st'] = st_match.group(1).strip()

            et_match = re.search(r'Complete Construction: ([A-Za-z0-9_ -]+)', block)
            if et_match:
                project_info['et'] = et_match.group(1).strip()
            
            topic_match = re.findall(r'(park|road|FEMA|fire|emergency warning|drainage|storm drain|highway|bridge|playground|water treatment|guardrail)', block, re.IGNORECASE)
            if topic_match:
                project_info['topic'] = ', '.join(list(set(topic_match)))

            projects.append(project_info)
    return projects

all_projects = []
file_path = locals()['var_function-call-9593347152521828074']
with open(file_path, 'r') as f:
    data = json.load(f)

for doc in data['query_db_response']['results']:
    all_projects.extend(extract_projects(doc['text']))


spring_2022_projects = []
for project in all_projects:
    if 'st' in project and ('Spring 2022' in project['st'] or 'March 2022' in project['st'] or 'April 2022' in project['st'] or 'May 2022' in project['st'] or ('2022' in project['st'] and ('March' in project['st'] or 'April' in project['st'] or 'May' in project['st']))):
        spring_2022_projects.append(project)


project_names = [proj['Project_Name'] for proj in spring_2022_projects]

print('__RESULT__:')
print(json.dumps(project_names))"""

env_args = {'var_function-call-9593347152521828074': 'file_storage/function-call-9593347152521828074.json'}

exec(code, env_args)
