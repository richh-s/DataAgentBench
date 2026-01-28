code = """import json

# Load data from files
civic_docs = json.load(open('/tmp/tmppk2n1y0f.json'))
funding_data = json.load(open('/tmp/tmpp8v2e1e3.json'))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Check if line contains Park and is not too long (likely a project name)
        if 'Park' in line and len(line) < 100:
            # Skip metadata lines
            bad_words = ['updates:', 'schedule:', 'description:', 'page', 'agenda', 'item']
            if not any(w in line.lower() for w in bad_words):
                # Check if completed in 2022 (look in nearby lines)
                nearby = '\n'.join(lines[max(0,i-3):min(len(lines),i+4)])
                if '2022' in nearby and 'completed' in nearby.lower():
                    if line not in park_projects:
                        park_projects.append(line)

# Check for Broad Beach Road Water Quality Repair (park infrastructure)
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Broad Beach Road Water Quality' in text and '2022' in text:
        if 'completed' in text.lower():
            if 'Broad Beach Road Water Quality Repair' not in park_projects:
                park_projects.append('Broad Beach Road Water Quality Repair')

# Match with funding records
total_funding = 0
matched_projects = []

for project in park_projects:
    proj_lower = project.lower()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        
        # Match exact or partial
        if proj_lower == fund_name or fund_name.startswith(proj_lower):
            total_funding += int(fund['Amount'])
            matched_projects.append(project)

result = {
    'total_funding': total_funding,
    'matched_projects': len(matched_projects),
    'project_list': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:70': {'files': [], 'civic_related': []}, 'var_functions.execute_python:72': {'civic_type': "<class 'NoneType'>", 'funding_type': "<class 'NoneType'>"}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
