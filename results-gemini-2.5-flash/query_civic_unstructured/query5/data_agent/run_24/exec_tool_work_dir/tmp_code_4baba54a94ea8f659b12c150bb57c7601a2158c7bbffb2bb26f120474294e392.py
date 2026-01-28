code = """import json
import re

with open(locals()['var_function-call-16813778080259091819'], 'r') as f:
    civic_docs = json.load(f)

all_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Use a single regex to find all project blocks (Capital and Disaster) and their details
    # This regex tries to capture: 
    # Group 1: Project Type (Capital Improvement Projects or Disaster Recovery Projects)
    # Group 2: Project Name
    # Group 3: Updates/Schedule information (including 'Begin Construction' dates)
    project_blocks_regex = re.compile(
        r'(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects \(.*?\))\n\n(.*?)(?=\n\n(Capital Improvement Projects|Disaster Recovery Projects)|Page \d+ of \d+|$)',
        re.DOTALL
    )
    
    for match in project_blocks_regex.finditer(text):
        project_type_header = match.group(1)
        project_section_content = match.group(2)
        
        current_type = None
        if "Capital Improvement Projects" in project_type_header:
            current_type = "capital"
        elif "Disaster Recovery Projects" in project_type_header:
            current_type = "disaster"
        
        if current_type:
            # Now parse the project_section_content for individual projects
            # This regex looks for project name followed by \n(cid:190) Updates: and then schedule info
            individual_project_regex = re.compile(
                r'\n\n(.*?)\n\s*\(cid:190\) Updates:(.*?)(?:\n\s*\(cid:190\) Project Schedule:(.*?)|\n\s*\(cid:190\) Estimated Schedule:(.*?)|\n\s*\(cid:190\) Complete Construction:(.*?)|\n\s*\(cid:190\) Project Description:(.*?)(?:\n\s*\(cid:190\) Project Updates:(.*?)|\n\s*\(cid:190\) Updates:(.*?)))?(?=\n\n|Page \d+ of \d+|$)',
                re.DOTALL
            )
            
            for proj_match in individual_project_regex.finditer(project_section_content):
                project_name = proj_match.group(1).strip()
                schedule_info = proj_match.group(3) or proj_match.group(4) or proj_match.group(5) or ''
                
                start_date = None
                start_date_match = re.search(r'Begin (?:Construction|Work|Project):\s*(\w+\s*\d{4}|\d{4}-\w+)', schedule_info)
                if start_date_match:
                    start_date = start_date_match.group(1)

                if project_name:
                    all_projects.append({
                        'Project_Name': project_name,
                        'type': current_type,
                        'st': start_date
                    })


# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and project['st'] and '2022' in project['st']:
        disaster_projects_2022.append(project)

print('__RESULT__:')
print(json.dumps(disaster_projects_2022)))"""

env_args = {'var_function-call-13790590049181057957': ['civic_docs'], 'var_function-call-3607000441821407365': 'file_storage/function-call-3607000441821407365.json', 'var_function-call-3146719146564769422': ['Funding'], 'var_function-call-16813778080259091819': 'file_storage/function-call-16813778080259091819.json'}

exec(code, env_args)
