code = """import json
import re

# Load funding data from the path returned by query_db
funding_data = json.load(open(var_functions.query_db:2))

# Load civic documents from the path returned by query_db
civic_docs = json.load(open(var_functions.query_db:6))

# Build funding map for projects > $50,000
funding_map = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects and count matches
count = 0
matched = []

for doc in civic_docs:
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
            
            if line.startswith('('):
                continue
            
            # Check for funding match
            clean_line = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
            if line in funding_map or clean_line in funding_map:
                count += 1
                amt = funding_map.get(line) or funding_map.get(clean_line, 0)
                matched.append({'project': line, 'funding': amt})

result = {'count': count, 'matches': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
