code = """import json
import re

# Access the stored results 
funding_data = locals()['var_functions.query_db:2']
civic_docs = locals()['var_functions.query_db:6']

# Parse the data (they're stored as JSON strings in the file paths)
with open(funding_data, 'r') as f:
    funding = json.load(f)

with open(civic_docs, 'r') as f:
    civic = json.load(f)

# Build funding map for projects > 50000
funding_map = {}
for rec in funding:
    amt = float(rec['Amount'])
    if amt > 50000:
        name = rec['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amt
        funding_map[clean_name] = amt

# Extract capital design projects from civic docs
capital_design = set()
for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design = False
        
        if in_design and line and len(line) > 15:
            # Skip disaster projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'fire' in line:
                continue
            
            # Skip meta lines
            if any(word in line.upper() for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']):
                continue
            
            # Skip section markers
            if any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement Projects']):
                continue
            
            if line.startswith('(') or line.startswith('\\u2022'):
                continue
            
            capital_design.add(line)

# Count matches
count = 0
for proj in capital_design:
    proj_clean = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in funding_map or proj_clean in funding_map:
        count += 1

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
