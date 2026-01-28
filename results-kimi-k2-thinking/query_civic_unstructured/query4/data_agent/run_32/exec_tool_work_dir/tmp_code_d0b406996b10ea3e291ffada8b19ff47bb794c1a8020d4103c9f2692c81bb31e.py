code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:52'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_functions.query_db:42'], 'r') as f:
    funding_data = json.load(f)

# Build funding dictionary
funding_dict = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(str(record.get('Amount', 0)))
    if proj_name and amount > 0:
        funding_dict[proj_name] = funding_dict.get(proj_name, 0) + amount

# Find Spring 2022 projects
spring_2022_projects = []

# Pattern to find Spring 2022 references
spring_patterns = [
    r'2022\s*-\s*Spring', r'2022\s*-\s*March', r'2022\s*-\s*April', r'2022\s*-\s*May',
    r'2022\s*Spring', r'2022\s*March', r'2022\s*April', r'2022\s*May'
]

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find all project sections
    # Projects are typically listed with name, then schedule info
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Skip headers
        if any(skip in line.lower() for skip in ['page', 'agenda', 'item', 'public works', 'commission', 'prepared by', 'approved by', 'date', 'subject', 'discussion']):
            i += 1
            continue
        
        # Check if this might be a project name
        if len(line) > 10 and len(line) < 150 and line[0].isupper():
            # Look at next few lines for schedule info
            look_ahead = '\n'.join(lines[i:i+10]).lower()
            
            # Check for Spring 2022 patterns
            has_spring_2022 = any(re.search(pattern, look_ahead, re.IGNORECASE) for pattern in spring_patterns)
            
            # Also check if project name itself contains 2022 (indicating start year)
            has_2022_in_name = '2022' in line and any(month in line.lower() for month in ['march', 'april', 'may', 'spring'])
            
            if has_spring_2022 or has_2022_in_name:
                spring_2022_projects.append(line)
        
        i += 1

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

# Match projects with funding
matched_projects = []
total_funding = 0

for proj_name in spring_2022_projects:
    # Direct match
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append({
            'project': proj_name,
            'funding': amount
        })
        total_funding += amount
    else:
        # Try base name match (for projects with parenthetical suffixes)
        base_name = proj_name.split(' (')[0]
        for funded_proj in funding_dict:
            if funded_proj.startswith(base_name + ' (') or funded_proj == base_name:
                amount = funding_dict[funded_proj]
                matched_projects.append({
                    'project': proj_name,
                    'matched_funding_name': funded_proj,
                    'funding': amount
                })
                total_funding += amount
                break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'sample_projects': matched_projects[:5]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'funding_records': 500, 'civic_documents': 5, 'status': 'data_loaded'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'civic_docs_loaded': 5, 'funding_records_loaded': 500, 'status': 'ready_to_process'}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'funding_records': 500, 'civic_documents': 3}, 'var_functions.list_db:50': ['civic_docs'], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
