code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:1
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:1

# Load civic documents
civic_file = var_functions.query_db:2
if isinstance(civic_file, str) and civic_file.endswith('.json'):
    with open(civic_file, 'r') as f:
        civic_docs = json.json.load(f)
else:
    civic_docs = var_functions.query_db:2

# Extract projects with design status
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern to find design section
    pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \((Construction|Not Started)\)|Disaster Recovery|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        section = match.group(1)
        lines = section.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:
                skip = False
                for skip_pattern in ['(', 'cid:', 'Updates:', 'Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Project Description:']:
                    if skip_pattern in line:
                        skip = True
                        break
                
                if not skip and any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Master Plan']):
                    cleaned = re.sub(r'^[^a-zA-Z]*', '', line)
                    if cleaned:
                        extracted_projects.append({
                            'Project_Name': cleaned,
                            'type': 'capital',
                            'status': 'design'
                        })

# Remove duplicates
unique = {}
for p in extracted_projects:
    unique[p['Project_Name']] = p
extracted_projects = list(unique.values())

# Match with funding
matched = []
for proj in extracted_projects:
    pname = proj['Project_Name'].lower()
    
    for fund in funding_data:
        fname = fund['Project_Name'].lower()
        
        if pname in fname or fname in pname:
            matched.append(proj)
            break
        
        # Word overlap
        pwords = set(re.findall(r'\b\w+\b', pname))
        fwords = set(re.findall(r'\b\w+\b', fname))
        if len(pwords.intersection(fwords)) >= 3:
            matched.append(proj)
            break

print('__RESULT__:')
print(json.dumps({
    'count': len(matched),
    'sample_matched': matched[:5],
    'total_extracted': len(extracted_projects)
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
