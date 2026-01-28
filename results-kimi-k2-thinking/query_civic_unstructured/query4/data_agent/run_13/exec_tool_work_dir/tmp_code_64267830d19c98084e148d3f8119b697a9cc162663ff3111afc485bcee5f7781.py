code = """import json

civic_docs_file = locals()['var_functions.query_db:4']
funding_file = locals()['var_functions.query_db:5']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if not line or line.startswith('Page') or line.startswith('Item'):
            continue
        
        if len(line) > 15 and line[0].isupper():
            next_text = ' '.join(lines[i+1:i+4]).lower()
            if 'updates' in next_text or 'schedule' in next_text:
                project = {'name': line, 'spring_2022': False}
                
                for j in range(i+1, min(i+8, len(lines))):
                    next_line = lines[j].lower()
                    if 'spring' in next_line and '2022' in next_line:
                        project['spring_2022'] = True
                    if '2022' in next_line:
                        if 'mar' in next_line or 'apr' in next_line or 'may' in next_line:
                            project['spring_2022'] = True
                        if '03' in next_line or '04' in next_line or '05' in next_line:
                            project['spring_2022'] = True
                
                projects.append(project)

spring_2022_projects = [p for p in projects if p['spring_2022']]
spring_names = [p['name'] for p in spring_2022_projects]

matches = []
for fund in funding:
    fund_name = fund['Project_Name'].lower()
    for name in spring_names:
        if name.lower() in fund_name or fund_name in name.lower():
            matches.append(fund)
            break

total_funding = sum(int(f['Amount']) for f in matches)

result = {
    'spring_2022_count': len(spring_2022_projects),
    'funding_matches': len(matches),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
