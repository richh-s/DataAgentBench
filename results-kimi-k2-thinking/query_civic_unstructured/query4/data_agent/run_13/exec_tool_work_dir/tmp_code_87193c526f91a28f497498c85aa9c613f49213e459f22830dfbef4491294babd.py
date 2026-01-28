code = """import json
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

spring_projects = []

for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line or line.startswith('Page') or line.startswith('Item'):
            i += 1
            continue
        
        # Look for project name
        if len(line) > 10 and line[0].isupper() and line != 'PUBLIC WORKS COMMISSION':
            project_name = line
            spring_2022 = False
            
            # Look ahead for spring 2022 dates
            for j in range(i+1, min(i+8, len(lines))):
                next_line = lines[j]
                lower_line = next_line.lower()
                
                # Check for spring 2022
                if 'spring' in lower_line and '2022' in lower_line:
                    spring_2022 = True
                if '2022-spring' in lower_line:
                    spring_2022 = True
                if '2022' in lower_line:
                    if 'mar' in lower_line or 'apr' in lower_line or 'may' in lower_line:
                        spring_2022 = True
                    if '03' in lower_line or '04' in lower_line or '05' in lower_line:
                        spring_2022 = True
            
            if spring_2022:
                spring_projects.append(project_name)
        
        i += 1

# Deduplicate while preserving order
unique_spring = []
for p in spring_projects:
    if p not in unique_spring:
        unique_spring.append(p)

# Find funding matches
funding_matches = []
total_funding = 0
for fund in funding:
    fund_name = fund['Project_Name'].lower()
    for proj_name in unique_spring:
        proj_lower = proj_name.lower()
        # Check if project name is contained in funding name or vice versa
        if proj_lower in fund_name or fund_name in proj_lower:
            funding_matches.append({
                'project': proj_name,
                'funding_record': fund['Project_Name'],
                'amount': int(fund['Amount'])
            })
            total_funding += int(fund['Amount'])
            break

result = {
    'spring_2022_projects_count': len(unique_spring),
    'spring_2022_projects': unique_spring,
    'funding_matches': funding_matches,
    'total_funding': total_funding
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}}

exec(code, env_args)
