code = """import json

# Load civic documents
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in documents:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    if 'park' in lower_text and 'completed' in lower_text and '2022' in lower_text:
        lines = text.split('\n')
        
        for i in range(len(lines)):
            line = lines[i].strip()
            
            # Look for completion statements mentioning 2022
            line_lower = line.lower()
            if '2022' in line and ('completed' in line_lower or 'construction was completed' in line_lower):
                # Look backwards to find project name
                project_name = None
                for j in range(max(0, i-5), i):
                    prev_line = lines[j].strip()
                    prev_lower = prev_line.lower()
                    
                    if prev_line and len(prev_line) > 5:
                        skip_words = ['capital improvement', 'disaster recovery', 'public works', 'commission', 'agenda', 'updates:']
                        should_skip = any(word in prev_lower for word in skip_words)
                        
                        if not should_skip:
                            project_name = prev_line
                            break
                
                if project_name and 'park' in project_name.lower():
                    park_projects_2022.append(project_name)

# Load funding records
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Calculate total funding
total_funding = 0
matched_projects = []

for project in park_projects_2022:
    proj_lower = project.lower()
    for fund in funding_records:
        fund_name = fund['Project_Name'].lower()
        if proj_lower == fund_name or proj_lower in fund_name or fund_name in proj_lower:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': project,
                'funding_record': fund['Project_Name'],
                'amount': amount
            })

result = {
    'total_funding': total_funding,
    'matched_count': len(matched_projects),
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
