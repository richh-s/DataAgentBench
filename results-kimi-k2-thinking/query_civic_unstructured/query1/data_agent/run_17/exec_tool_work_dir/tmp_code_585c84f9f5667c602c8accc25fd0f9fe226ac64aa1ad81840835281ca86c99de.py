code = """import json
import re

# Load funding data (Amount > 50000)
with open('/tmp/tmp4q6n_5e0.json', 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open('/tmp/tmp3d0s1x5g.json', 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic docs
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION)'
    design_section = re.search(design_pattern, text, re.DOTALL|re.IGNORECASE)
    
    if design_section:
        section_text = design_section.group(1)
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and known non-project lines
            if not line or line.startswith('(') or 'cid:' in line or \
               'Updates:' in line or 'Project Schedule:' in line or \
               'Complete Design:' in line or 'Advertise:' in line or \
               'Begin Construction:' in line or line.isupper() or \
               line in ['Spring 2023', 'Summer 2023', 'Fall 2023', 'Winter 2024']:
                continue
            
            # Check if line looks like a project name (has reasonable length, not just a date/keyword)
            if len(line) > 10 and not re.match(r'^\d{4}-', line):
                projects.append({
                    'Project_Name': line,
                    'type': 'capital',
                    'status': 'design'
                })

# Match with funding data
matches = []

for proj in projects:
    proj_name = proj['Project_Name']
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        amount = int(fund['Amount'])
        
        # Check for various match patterns
        if (proj_name == fund_name or 
            proj_name in fund_name or 
            fund_name in proj_name):
            matches.append({
                'Project_Name': fund_name,
                'type': proj['type'],
                'status': proj['status'],
                'Amount': amount
            })
            break

print('RESULT:')
print(json.dumps({
    'count': len(matches),
    'projects': matches
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
