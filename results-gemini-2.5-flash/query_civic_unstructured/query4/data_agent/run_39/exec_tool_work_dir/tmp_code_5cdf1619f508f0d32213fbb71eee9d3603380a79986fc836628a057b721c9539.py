code = """import json
import re

file_path = locals()['var_function-call-8996949378808881180']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

projects_started_spring_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    for i, line in enumerate(lines):
        if 'Project Schedule:' in line or 'Estimated Schedule:' in line:
            for k in range(i - 1, -1, -1):
                potential_project_name = lines[k].strip()
                if potential_project_name and not potential_project_name.startswith('(cid:') and not potential_project_name.lower().startswith('updates:') and not potential_project_name.lower().startswith('to:') and not potential_project_name.lower().startswith('from:') and not potential_project_name.lower().startswith('date prepared:') and not potential_project_name.lower().startswith('subject:') and not potential_project_name.lower().startswith('recommended action:') and not potential_project_name.lower().startswith('discussion:') and not potential_project_name.lower().startswith('page ') and not potential_project_name.lower().startswith('agenda item') and not potential_project_name.lower().startswith('commission meeting') and not potential_project_name.lower().startswith('public works'):
                    current_project_name = potential_project_name
                    break

            for j in range(i + 1, len(lines)):
                if 'Begin Construction:' in lines[j] or 'Advertise:' in lines[j] or 'Begin Project:' in lines[j]:
                    start_date_match = re.search(r'(?:Begin Construction|Advertise|Begin Project):\s*(.*?)$' , lines[j])
                    if start_date_match:
                        start_date = start_date_match.group(1).strip()
                        is_spring_2022 = False
                        if '2022' in start_date:
                            if 'Spring' in start_date or 'March' in start_date or 'April' in start_date or 'May' in start_date:
                                is_spring_2022 = True

                        if is_spring_2022 and current_project_name:
                            projects_started_spring_2022.append({"Project_Name": current_project_name, "st": start_date})
                        break

result = json.dumps(projects_started_spring_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-8996949378808881180': 'file_storage/function-call-8996949378808881180.json'}

exec(code, env_args)
