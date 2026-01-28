code = """import json
import re

with open(locals()['var_function-call-13556780500414071833'], 'r') as f:
    civic_docs_data = json.load(f)

projects = []
for doc in civic_docs_data:
    text = doc['text']
    project_blocks = re.split(r'\n(?=[A-Z][A-Za-z ]+Project(?:s)?\n\n)', text)
    for block in project_blocks:
        project_name_match = re.search(r'([A-Z][A-Za-z ]+Project(?:s)?)(?:\n|\s*\(cid:190\))', block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            project_type = 'disaster' if 'Disaster Recovery Projects' in text or 'FEMA' in block or 'CalOES' in block else 'capital'
            start_time_match = re.search(r'Begin (?:Construction|Work|Project|Operation):\s*([A-Za-z0-9-]+(?:\s[A-Za-z0-9-]+)*)', block)
            start_time = start_time_match.group(1).strip() if start_time_match else None
            
            if project_type == 'disaster' and start_time and '2022' in start_time:
                projects.append({'Project_Name': project_name, 'st': start_time, 'type': project_type})

print('__RESULT__:')
print(json.dumps(projects))"""

env_args = {'var_function-call-13556780500414071833': 'file_storage/function-call-13556780500414071833.json'}

exec(code, env_args)
