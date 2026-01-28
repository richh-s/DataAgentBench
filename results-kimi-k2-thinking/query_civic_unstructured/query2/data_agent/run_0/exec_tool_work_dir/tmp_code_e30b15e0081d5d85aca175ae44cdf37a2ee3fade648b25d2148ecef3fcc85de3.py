code = """import json
import re

# Load documents
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Look for park projects completed in 2022
park_completed_2022 = []

for doc in documents:
    text = doc.get('text', '')
    
    # Pattern to find projects and their completion status
    # Projects often have names followed by Updates sections
    pattern = r'([A-Z][^\n]{5,100})\n.*?\\\(cid:\d+\\) Updates:(.*?)(?=[A-Z][^\n]{5,100}\n.*?\\\(cid:\d+\\) Updates:|\Z)'
    
    matches = re.findall(pattern, text, re.DOTALL)
    
    for project_name, project_section in matches:
        project_name = project_name.strip()
        section_lower = project_section.lower()
        
        # Check if park related
        is_park = 'park' in project_name.lower() or 'playground' in section_lower
        
        # Check if completed in 2022
        completed_2022 = bool(re.search(r'2022.*completed|completed.*2022', section_lower))
        
        if is_park and completed_2022:
            park_completed_2022.append(project_name)

# Load funding data
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Match funding by project name
total_funding = 0
matched_funding = []

for project in park_completed_2022:
    for fund in funding_records:
        fund_name = fund['Project_Name'].lower()
        proj_lower = project.lower()
        
        if proj_lower == fund_name or proj_lower in fund_name or fund_name in proj_lower:
            amount = int(fund['Amount'])
            total_funding += amount
            matched_funding.append({
                'project': project,
                'funding_record': fund['Project_Name'],
                'amount': amount
            })

result = {
    'total_funding': total_funding,
    'matched_funding': matched_funding,
    'park_projects': park_completed_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
