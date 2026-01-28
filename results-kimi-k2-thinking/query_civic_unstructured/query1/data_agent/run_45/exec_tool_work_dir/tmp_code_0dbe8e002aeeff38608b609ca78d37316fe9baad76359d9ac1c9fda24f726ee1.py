code = """import json
import re

# Load data
f_file = var_functions.query_db:2
with open(f_file) as f:
    funding = json.load(f)

c_file = var_functions.query_db:6
with open(c_file) as f:
    civic = json.load(f)

# Build funding map (amount > 50000)
fund_map = {}
for rec in funding:
    amt = float(rec.get('Amount', 0))
    if amt > 50000:
        name = rec['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund_map[name] = amt
        fund_map[clean] = amt

# Find capital design projects
cap_design = set()

for doc in civic:
    text = doc.get('text', '')
    
    # Find start of design section
    design_start = text.find('(Design)')
    if design_start == -1:
        continue
    
    # Get subsection until next major heading
    subtext = text[design_start:]
    next_section = subtext.find('(Construction)')
    if next_section > 0:
        subtext = subtext[:next_section]
    
    # Extract project names (lines that are likely project names)
    for line in subtext.split('\n'):
        line = line.strip()
        if len(line) > 10:
            # Skip meta content
            skip = False
            for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'Page']:
                if word in line.upper():
                    skip = True
            if skip:
                continue
            
            # Skip bullet points
            if line.startswith('('):
                continue
            
            # Skip disaster projects
            if any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            cap_design.add(line)

# Match with funding
total = 0
matches = []

for proj in cap_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    
    if proj in fund_map or proj_clean in fund_map:
        total += 1
        amt = fund_map.get(proj) or fund_map.get(proj_clean, 0)
        matches.append({'name': proj, 'amount': int(amt)})

print('__RESULT__:')
print(json.dumps({'count': total, 'projects': matches}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
