code = """import json
import re

# Load funding data with Amount > 50000
with open(r'/tmp/tmp4q6n_5e0.json', 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open(r'/tmp/tmp3d0s1x5g.json', 'r') as f:
    civic_docs = json.load(f)

# Extract projects with design status
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find Capital Improvement Projects (Design) section
    start_marker = 'Capital Improvement Projects (Design)'
    if start_marker in text:
        start = text.find(start_marker)
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = text.find('Capital Improvement Projects (Not Started)', start)
        if end == -1:
            end = text.find('Disaster Recovery Projects', start)
        if end == -1:
            end = len(text)
        
        section = text[start:end]
        for line in section.split('\n'):
            line = line.strip()
            # Skip non-project lines
            if not line or line.isupper() or len(line) < 10:
                continue
            if any(x in line for x in ['cid:', 'Updates:', 'Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:']):
                continue
            if line.startswith(('Spring', 'Summer', 'Fall', 'Winter')) or '2023' in line or '2024' in line:
                continue
                
            clean_line = line.strip(':-•')
            if clean_line:
                projects.append({'Project_Name': clean_line, 'type': 'capital', 'status': 'design'})

# Match with funding
matches = []
used_ids = set()

for proj in projects:
    proj_lower = proj['Project_Name'].lower()
    for fund in funding_data:
        if fund['Funding_ID'] in used_ids:
            continue
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower()
        amount = int(fund['Amount'])
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            matches.append({'Project_Name': fund_name, 'Amount': amount})
            used_ids.add(fund['Funding_ID'])
            break

print('__RESULT__:')
print(json.dumps({'count': len(matches), 'projects': matches}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
