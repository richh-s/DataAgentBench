code = """import json
import re

# Load funding data (from var_functions.query_db:2)
with open(var_functions.query_db:2, 'r') as f:
    funding = json.load(f)

# Load civic documents (from var_functions.query_db:30)
with open(var_functions.query_db:30, 'r') as f:
    civic = json.load(f)

# Build funding map for projects > $50,000
funding_map = {}
for rec in funding:
    amount = float(rec.get('Amount', 0))
    if amount > 50000:
        name = rec['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects from civic documents and count matches
count = 0

for doc in civic:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design_section = False
        
        if in_design_section and line and len(line) > 15:
            # Skip disaster projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'fire' in line:
                continue
            
            # Skip meta lines
            if any(word in line.upper() for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']):
                continue
            
            # Skip section markers
            if any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement Projects']):
                continue
            
            if line.startswith('('):
                continue
            
            # Check if this project has funding
            clean_line = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
            if line in funding_map or clean_line in funding_map:
                count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
