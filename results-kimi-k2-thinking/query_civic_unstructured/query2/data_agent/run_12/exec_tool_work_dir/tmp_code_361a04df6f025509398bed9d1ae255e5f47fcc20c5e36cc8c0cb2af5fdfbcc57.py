code = """import json
import re

# Load the data from the files
civic_file_path = var_functions.query_db_106
funding_file_path = var_functions.query_db_107

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded data: civic=' + str(len(civic_docs)) + ', funding=' + str(len(funding_records)))

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for project lines mentioning park
        if 'park' in line.lower() and len(line) < 150 and not line.startswith('(') and not line.startswith('•'):
            # Check context for completion in 2022
            context_start = max(0, i-3)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'completed' in context and '2022' in context:
                project_name = line.strip()
                if project_name and project_name not in park_projects_2022:
                    park_projects_2022.append(project_name)

print('Park projects found: ' + str(len(park_projects_2022)))

# Clean project names for matching
def clean_name(name):
    if not name:
        return ''
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Match and calculate total funding
total_funding = 0
matched_funding = set()

for park_proj in park_projects_2022:
    park_clean = clean_name(park_proj)
    if not park_clean:
        continue
    
    for fund in funding_records:
        fund_name = fund.get('Project_Name', '')
        if not fund_name:
            continue
        fund_clean = clean_name(fund_name)
        if not fund_clean:
            continue
        
        # Check if names match
        if park_clean in fund_clean or fund_clean in park_clean:
            if fund_name not in matched_funding:
                total_funding = total_funding + int(fund.get('Amount', 0))
                matched_funding.add(fund_name)

print('Total funding: ' + str(total_funding))
result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.list_db:104': ['civic_docs'], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json'}

exec(code, env_args)
