code = """import json
import re

with open(locals()['var_function-call-16813778080259091819'], 'r') as f:
    civic_docs = json.load(f)

all_projects_info = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document by major project sections (Capital and Disaster)
    sections = re.split(r'\n(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects \(.*?\))\n', text)

    current_project_type = None
    for i, section in enumerate(sections):
        if section is None:
            continue
        
        if "Capital Improvement Projects" in section:
            current_project_type = "capital"
        elif "Disaster Recovery Projects" in section:
            current_project_type = "disaster"
        else:
            # If it's a content section after a project type header, extract individual projects
            # This regex looks for project names that are typically followed by a newline and then updates/schedule info
            project_blocks = re.findall(r'\n\n(.*?)\n\s*\(cid:190\) Updates:(.*?)(?:\n\s*\(cid:190\) Project Schedule:(.*?)|\n\s*\(cid:190\) Estimated Schedule:(.*?)|\n\s*\(cid:190\) Complete Construction:(.*?)|\n\s*\(cid:190\) Project Description:(.*?)(?:\n\s*\(cid:190\) Project Updates:(.*?)|\n\s*\(cid:190\) Updates:(.*?)))?(?=\n\n|Page \d+ of \d+|$)', section, re.DOTALL)
            
            for block in project_blocks:
                project_name = block[0].strip()
                schedule_info = block[2] or block[3] or block[4] or '' # Project Schedule, Estimated Schedule, Complete Construction
                
                start_date = None
                # Search for start date patterns within the extracted schedule information
                start_date_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', schedule_info)
                if start_date_match:
                    start_date = start_date_match.group(1)

                if project_name and current_project_type:
                    all_projects_info.append({
                        'Project_Name': project_name,
                        'type': current_project_type,
                        'st': start_date
                    })


# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
for project in all_projects_info:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps(disaster_projects_2022)))"""

env_args = {'var_function-call-13790590049181057957': ['civic_docs'], 'var_function-call-3607000441821407365': 'file_storage/function-call-3607000441821407365.json', 'var_function-call-3146719146564769422': ['Funding'], 'var_function-call-16813778080259091819': 'file_storage/function-call-16813778080259091819.json'}

exec(code, env_args)
