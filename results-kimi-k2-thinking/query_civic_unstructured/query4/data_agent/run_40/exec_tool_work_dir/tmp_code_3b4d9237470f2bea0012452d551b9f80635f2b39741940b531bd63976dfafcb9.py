code = """import json, re, os

# Find and load the data files without quoting issues
files = []
for root, dirs, filenames in os.walk('/root/shared_data'):
    for filename in filenames:
        if filename.endswith('.json'):
            files.append(os.path.join(root, filename))

print('Found JSON files:', len(files))

funding_data = []
civic_docs = []

for f in files:
    with open(f, 'r') as data_file:
        data = json.load(data_file)
    if len(data) > 0 and isinstance(data[0], dict):
        if 'Project_Name' in data[0] and 'Amount' in data[0]:
            funding_data = data
            print('Found funding data', len(data), 'records')
        elif 'text' in data[0]:
            civic_docs = data
            print('Found civic docs data', len(data), 'records')

# Extract Spring 2022 projects from document text
spring_project_names = []
for doc in civic_docs:
    text_str = doc.get('text', '')
    if 'Spring 2022' in text_str or '2022-Spring' in text_str:
        lines = text_str.split('\n')
        for idx in range(len(lines)):
            line = lines[idx]
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Find project name before the schedule line
                start_search = max(0, idx-5)
                for back_idx in range(idx-1, start_search-1, -1):
                    candidate_line = lines[back_idx].strip()
                    if candidate_line and len(candidate_line) > 15 and not candidate_line.startswith('('):
                        spring_project_names.append(candidate_line)
                        break
                break

print('Spring 2022 projects found:', len(spring_project_names))

# Match with funding records
total_funding_amount = 0
matched_funding_projects = set()

for fund_item in funding_data:
    funding_name = fund_item['Project_Name']
    amount_value = int(fund_item['Amount'])
    
    for project_name in spring_project_names:
        # Check for containment relationship
        if funding_name in project_name or project_name in funding_name:
            if funding_name not in matched_funding_projects:
                matched_funding_projects.add(funding_name)
                total_funding_amount += amount_value
                break

final_result = json.dumps({'project_count': len(matched_funding_projects), 'total_funding': total_funding_amount})
print('__RESULT__:')
print(final_result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
