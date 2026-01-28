code = """import json
import re

with open(locals()['var_function-call-16813778080259091819'], 'r') as f:
    civic_docs = json.load(f)

all_projects_info = []

for doc in civic_docs:
    text = doc['text']
    
    # Split text by the main headers to identify capital and disaster project sections
    # Using re.split with a capturing group to keep the delimiters
    sections = re.split(r'(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects \(.*?\))\n', text)
    
    current_project_type = None
    # Iterate through the split sections
    for i, section in enumerate(sections):
        if section is None:
            continue
        
        if "Capital Improvement Projects" in section:
            current_project_type = "capital"
        elif "Disaster Recovery Projects" in section:
            current_project_type = "disaster"
        else:
            # This section contains project details for the current_project_type
            if current_project_type:
                # Regex to extract individual project blocks: Project Name, then Updates/Schedule
                # The pattern looks for a project name followed by updates and optionally schedule information
                project_blocks = re.findall(
                    r'\n\n(.*?)\n\\s*\(cid:190\\) Updates:(.*?)(?:\\n\\s*\(cid:190\\) Project Schedule:(.*?)|\\n\\s*\(cid:190\\) Estimated Schedule:(.*?)|\\n\\s*\(cid:190\\) Complete Construction:(.*?)|\\n\\s*\(cid:190\\) Project Description:(.*?)(?:\\n\\s*\(cid:190\\) Project Updates:(.*?)|\\n\\s*\(cid:190\\) Updates:(.*?)))?(?=\\n\\n|Page \\d+ of \\d+|$)',
                    section, re.DOTALL
                )
                
                for block in project_blocks:
                    project_name = block[0].strip()
                    # Concatenate schedule-related groups for date extraction
                    schedule_info = block[2] or block[3] or block[4] or '' 
                    
                    start_date = None
                    # Look for 'Begin Construction: DATE' or similar patterns
                    start_date_match = re.search(r'Begin (?:Construction|Work|Project):\\s*(\w+\\s*\\d{4}|\\d{4}-\\w+)', schedule_info)
                    if start_date_match:
                        start_date = start_date_match.group(1)

                    if project_name:
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
