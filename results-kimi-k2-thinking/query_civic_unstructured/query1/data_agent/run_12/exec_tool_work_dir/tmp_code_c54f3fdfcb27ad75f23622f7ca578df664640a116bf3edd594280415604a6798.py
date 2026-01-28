code = """import json
import re

funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:1']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Build funding lookup for projects > $50K
funding_lookup = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

# Track capital projects in design phase
design_projects = set()

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    if 'Capital Improvement Projects (Design)' in text:
        start_pos = text.find('Capital Improvement Projects (Design)') + 38
        section = text[start_pos:]
        
        # Find section boundaries
        end_pos = float('inf')
        for marker in ['Capital Improvement Projects (Construction)', 
                      'Capital Improvement Projects (Not Started)',
                      'Disaster Recovery Projects']:
            marker_pos = section.find(marker)
            if marker_pos > 0 and marker_pos < end_pos:
                end_pos = marker_pos
        
        if end_pos != float('inf'):
            section = section[:end_pos]
        
        # Parse lines for project names
        for line in section.split('\n'):
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip non-project lines
            if any(p in line for p in ['(cid:', 'Updates:', 'Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction', 'Capital Improvement', 'Project Description:', '•', '-', '(']):
                if line.startswith('(') or line.startswith('-') or line.startswith('•'):
                    continue
                continue
            
            # Check funding match
            if line in funding_lookup:
                design_projects.add(line)

result = json.dumps({'count': len(design_projects), 'projects': sorted(list(design_projects))})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
