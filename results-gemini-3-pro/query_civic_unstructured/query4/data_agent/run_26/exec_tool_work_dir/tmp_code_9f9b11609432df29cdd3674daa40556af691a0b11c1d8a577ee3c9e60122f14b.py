code = """import json
import re

path_docs = locals()['var_function-call-3486162399230155614']
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        is_project_header = False
        # Look ahead
        for j in range(i + 1, len(lines)):
            next_l = lines[j].strip()
            if not next_l:
                continue
            if next_l.startswith('(cid:190)') or next_l.startswith('\u00be'):
                is_project_header = True
            break
        
        if is_project_header:
            if current_project:
                extracted_projects.append(current_project)
            current_project = {'name': line, 'lines': []}
        elif current_project:
            current_project['lines'].append(line)

    if current_project:
        extracted_projects.append(current_project)

candidates = []
patterns = [r'spring\s*2022', r'march.*?2022', r'april.*?2022', r'may.*?2022']

for proj in extracted_projects:
    name = proj['name']
    relevant_lines = []
    for l in proj['lines']:
        l_lower = l.lower()
        for p in patterns:
            if re.search(p, l_lower):
                relevant_lines.append(l)
                break
    if relevant_lines:
        candidates.append({'name': name, 'relevant_lines': relevant_lines})

print('__RESULT__:')
print(json.dumps(candidates))"""

env_args = {'var_function-call-5404665793405674675': ['civic_docs'], 'var_function-call-5404665793405674210': ['Funding'], 'var_function-call-4895478785273924841': 'file_storage/function-call-4895478785273924841.json', 'var_function-call-4895478785273921810': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-3486162399230155614': 'file_storage/function-call-3486162399230155614.json', 'var_function-call-6421004180030422518': 'file_storage/function-call-6421004180030422518.json'}

exec(code, env_args)
