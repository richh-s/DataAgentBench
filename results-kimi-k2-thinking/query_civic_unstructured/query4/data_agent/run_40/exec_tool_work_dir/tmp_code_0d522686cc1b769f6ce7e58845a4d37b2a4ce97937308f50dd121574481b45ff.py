code = """import json, re, os

# Read data from files instead of using variable references directly
funding_path = '/root/shared_data/var_functions.query_db:5.json'
civic_path = '/root/shared_data/var_functions.query_db:2.json'

with open(funding_path, 'r') as file1:
    funding_data = json.load(file1)

with open(civic_path, 'r') as file2:
    civic_data = json.load(file2)

print('Loaded funding:', len(funding_data), 'records')
print('Loaded civic:', len(civic_data), 'documents')

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text or '2022-March' in text or '2022-April' in text or '2022-May' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if 'Spring 2022' in line or '2022-Spring' in line or ('2022-' in line and any(m in line for m in ['March', 'April', 'May', '03', '04', '05'])):
                # Look back for project name (up to 5 lines)
                for j in range(i-1, max(0, i-6), -1):
                    prev_line = lines[j].strip()
                    if prev_line and len(prev_line) > 15 and not prev_line.startswith('(') and 'Page' not in prev_line and 'Item' not in prev_line:
                        spring_2022_projects.append(prev_line)
                        break
                break

print('Candidate projects:', len(spring_2022_projects))

# Match with funding
total_funding = 0
matched = set()

for fund in funding_data:
    fund_name = fund['Project_Name']
    amount = int(fund['Amount'])
    
    for proj in spring_2022_projects:
        # Match if fund name is contained in project name or vice versa
        if fund_name in proj or proj in fund_name or any(fund_name.startswith(word) for word in proj.split()[:2]):
            if fund_name not in matched:
                matched.add(fund_name)
                total_funding += amount
                break

result = {'project_count': len(matched), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
