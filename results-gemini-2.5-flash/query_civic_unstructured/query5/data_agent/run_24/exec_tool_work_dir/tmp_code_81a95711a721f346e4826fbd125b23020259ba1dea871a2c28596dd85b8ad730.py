code = """import json
import re

with open(locals()['var_function-call-3607000441821407365'], 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Identify sections for Capital Improvement Projects and Disaster Recovery Projects
    capital_projects_section = re.search(r'Capital Improvement Projects\s*\(.*?\)(.*?)(?:Disaster Recovery Projects|Page \d+ of \d+|$)', text, re.DOTALL)
    disaster_projects_section = re.search(r'Disaster Recovery Projects\s*\(.*?\)(.*?)(?:Capital Improvement Projects|Page \d+ of \d+|$)', text, re.DOTALL)

    if capital_projects_section:
        capital_text = capital_projects_section.group(1)
        # Extract project names and schedules from capital projects section
        capital_project_details = re.findall(r'\n\n(.*?)\n\s*\(cid:190\) Updates:(.*?)(?:\n\s*\(cid:190\) Project Schedule:(.*?)|\n\s*\(cid:190\) Estimated Schedule:(.*?)|\n\s*\(cid:190\) Complete Construction:(.*?)|\n\s*\(cid:190\) Project Description:(.*?)(?:\n\s*\(cid:190\) Project Updates:(.*?)|\n\s*\(cid:190\) Updates:(.*?)))?(?=\n\n|Page \d+ of \d+|$)', capital_text, re.DOTALL)

        for detail in capital_project_details:
            project_name = detail[0].strip()
            schedule_info = detail[2] or detail[3] or detail[4] or ''
            
            st = None
            start_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', schedule_info)
            if start_match:
                st = start_match.group(1)

            if project_name:
                projects.append({
                    'Project_Name': project_name,
                    'type': 'capital',
                    'st': st
                })

    if disaster_projects_section:
        disaster_text = disaster_projects_section.group(1)
        # Extract project names and schedules from disaster projects section
        disaster_project_details = re.findall(r'\n\n(.*?)\n\s*\(cid:190\) Updates:(.*?)(?:\n\s*\(cid:190\) Project Schedule:(.*?)|\n\s*\(cid:190\) Estimated Schedule:(.*?)|\n\s*\(cid:190\) Complete Construction:(.*?)|\n\s*\(cid:190\) Project Description:(.*?)(?:\n\s*\(cid:190\) Project Updates:(.*?)|\n\s*\(cid:190\) Updates:(.*?)))?(?=\n\n|Page \d+ of \d+|$)', disaster_text, re.DOTALL)

        for detail in disaster_project_details:
            project_name = detail[0].strip()
            schedule_info = detail[2] or detail[3] or detail[4] or ''

            st = None
            start_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', schedule_info)
            if start_match:
                st = start_match.group(1)
            
            if project_name:
                projects.append({
                    'Project_Name': project_name,
                    'type': 'disaster',
                    'st': st
                })

disaster_projects_2022 = []
for project in projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps(disaster_projects_2022)))"""

env_args = {'var_function-call-13790590049181057957': ['civic_docs'], 'var_function-call-3607000441821407365': 'file_storage/function-call-3607000441821407365.json', 'var_function-call-3146719146564769422': ['Funding']}

exec(code, env_args)
