code = """import json
import re

with open(locals()['var_function-call-3607000441821407365'], 'r') as f:
    civic_docs = json.load(f)

all_projects_info = []

for doc in civic_docs:
    text = doc['text']
    
    # Use re.split to get sections, then identify if it's a Capital or Disaster project section
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
            # If it's a content section, extract projects
            # Regex to capture Project Name and relevant schedule/update info
            project_patterns = re.findall(r'\n(.*?)\n\s*\(cid:190\) Updates:(.*?)(?:\n\s*\(cid:190\) Project Schedule:(.*?)|\n\s*\(cid:190\) Estimated Schedule:(.*?)|\n\s*\(cid:190\) Complete Construction:(.*?)|\n\s*\(cid:190\) Project Description:(.*?)(?:\n\s*\(cid:190\) Project Updates:(.*?)|\n\s*\(cid:190\) Updates:(.*?)))?(?=\n\n|Page \d+ of \d+|$)', section, re.DOTALL)
            
            for proj_match in project_patterns:
                project_name = proj_match[0].strip()
                schedule_info = proj_match[2] or proj_match[3] or proj_match[4] or '' # Project Schedule, Estimated Schedule, Complete Construction
                
                start_date = None
                # Look for 'Begin Construction: DATE' or similar patterns
                start_date_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', schedule_info)
                if start_date_match:
                    start_date = start_date_match.group(1)

                if project_name and current_project_type:
                    all_projects_info.append({
                        'Project_Name': project_name,
                        'type': current_project_type,
                        'st': start_date
                    })


disaster_projects_2022 = []
for project in all_projects_info:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps(disaster_projects_2022)))"""

env_args = {'var_function-call-13790590049181057957': ['civic_docs'], 'var_function-call-3607000441821407365': 'file_storage/function-call-3607000441821407365.json', 'var_function-call-3146719146564769422': ['Funding']}

exec(code, env_args)
