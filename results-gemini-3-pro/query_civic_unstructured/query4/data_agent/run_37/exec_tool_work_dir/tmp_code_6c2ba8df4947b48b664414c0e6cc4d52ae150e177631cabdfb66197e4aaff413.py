code = """import json

# Load data
with open(locals()['var_function-call-7227617260641500172'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-7188498576282706077'], 'r') as f:
    civic_docs = json.load(f)

project_names = [item['Project_Name'] for item in funding_data]
project_names.sort(key=len, reverse=True)

target_tokens = ['spring 2022', '2022-spring', 'march 2022', 'april 2022', 'may 2022', 'spring, 2022']

found_projects = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    current_project = None
    
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        # Identify project
        for pname in project_names:
            if pname in line_stripped and len(line_stripped) < len(pname) + 20:
                current_project = pname
                break
        
        if current_project:
            lower_line = line_stripped.lower()
            # Check for start indicators
            if 'begin construction' in lower_line or 'start' in lower_line:
                for token in target_tokens:
                    if token in lower_line:
                        found_projects[current_project] = line_stripped

matched_projects = list(found_projects.keys())
total_funding = 0
for pname in matched_projects:
    for record in funding_data:
        if record['Project_Name'] == pname:
            total_funding += int(record['Amount'])
            break

print('__RESULT__:')
print(json.dumps({'count': len(matched_projects), 'total_funding': total_funding, 'projects': matched_projects}))"""

env_args = {'var_function-call-17279470663678048780': 'file_storage/function-call-17279470663678048780.json', 'var_function-call-7227617260641500172': 'file_storage/function-call-7227617260641500172.json', 'var_function-call-7188498576282706077': 'file_storage/function-call-7188498576282706077.json'}

exec(code, env_args)
