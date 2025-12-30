code = """import json
import re

with open(locals()['var_function-call-3607000441821407365'], 'r') as f:
    civic_docs = json.load(f)

all_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Split text into sections based on project type headers
    # This regex looks for 'Capital Improvement Projects' or 'Disaster Recovery Projects' followed by text in parentheses and a newline
    sections = re.split(r'\n(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects \(.*?\))\n', text)

    current_type = None
    # Iterate through sections, identifying the project type and then extracting project details
    for i, section in enumerate(sections):
        if section is None:
            continue
        
        if "Capital Improvement Projects" in section:
            current_type = "capital"
        elif "Disaster Recovery Projects" in section:
            current_type = "disaster"
        elif current_type: # Only process if a project type has been identified
            # Regex to capture project name and schedule information
            # Project name is captured in group 1, and schedule/updates in group 2
            # It assumes project name is followed by '\n(cid:190) Updates:'
            project_details = re.findall(r'\n\n(.*?)\n\s*\(cid:190\) Updates:(.*?)(?:\n\s*\(cid:190\) Project Schedule:(.*?)|\n\s*\(cid:190\) Estimated Schedule:(.*?)|\n\s*\(cid:190\) Complete Construction:(.*?)|\n\s*\(cid:190\) Project Description:(.*?)(?:\n\s*\(cid:190\) Project Updates:(.*?)|\n\s*\(cid:190\) Updates:(.*?)))?(?=\n\n|Page \d+ of \d+|$)', section, re.DOTALL)
            
            for detail in project_details:
                project_name = detail[0].strip()
                schedule_info = detail[2] or detail[3] or detail[4] or '' # Project Schedule, Estimated Schedule, Complete Construction
                
                start_date = None
                # Look for 'Begin Construction: DATE' or similar patterns for start date
                start_date_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', schedule_info)
                if start_date_match:
                    start_date = start_date_match.group(1)

                if project_name:
                    all_projects.append({
                        'Project_Name': project_name,
                        'type': current_type,
                        'st': start_date
                    })


# Filter for disaster projects starting in 2022
disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps(disaster_projects_2022)))"""

env_args = {'var_function-call-13790590049181057957': ['civic_docs'], 'var_function-call-3607000441821407365': 'file_storage/function-call-3607000441821407365.json', 'var_function-call-3146719146564769422': ['Funding']}

exec(code, env_args)
