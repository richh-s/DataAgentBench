code = """import json
import re

# Load the data files
mongo_file = globals()['var_functions.query_db:5']
funding_file = globals()['var_functions.query_db:20']

# Handle both file paths and direct data
if isinstance(mongo_file, str) and mongo_file.endswith('.json'):
    with open(mongo_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = mongo_file

if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_file

# Build funding map
funding_map = {}
for rec in funding_records:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

spring_2022_projs = []

# Process documents
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for Spring 2022 references
    pattern = r'Spring\s+2022|spring\s+2022|Mar\w*\s+2022|Apr\w*\s+2022|May\s+2022'
    if re.search(pattern, text, re.IGNORECASE):
        # Extract lines around the match
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                # Get project name from nearby lines
                proj_name = None
                # Look backwards for project name (usually a header)
                for j in range(i-1, max(-1, i-10), -1):
                    prev_line = lines[j].strip()
                    if len(prev_line) > 5 and not prev_line.startswith('(') and not prev_line.startswith('▪'):
                        if not any(x in prev_line.lower() for x in ['project schedule', 'updates:', 'complete', 'begin', 'advertise']):
                            proj_name = prev_line
                            break
                
                if proj_name and proj_name not in [p['name'] for p in spring_2022_projs]:
                    spring_2022_projs.append({'name': proj_name, 'line': line})

# Match with funding
matched = []
total_funding = 0

for proj in spring_2022_projs:
    proj_name = proj['name']
    
    # Direct match
    if proj_name in funding_map:
        matched.append({'name': proj_name, 'funding': funding_map[proj_name]})
        total_funding += funding_map[proj_name]
    else:
        # Try variations
        for fund_name, amount in funding_map.items():
            if (proj_name.lower() in fund_name.lower() or 
                fund_name.lower() in proj_name.lower() or
                (len(proj_name) > 10 and proj_name[:15].lower() in fund_name.lower())):
                matched.append({'name': fund_name, 'funding': amount})
                total_funding += amount
                break

result = {
    'count': len(matched),
    'total_funding': total_funding,
    'projects': [{'project': p['name'], 'funding': p['funding']} for p in matched]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'status': 'loaded', 'civic_docs': 5, 'funding_records': 500}, 'var_functions.query_db:36': [{'count': '500', 'total_funding': '28094000'}]}

exec(code, env_args)
