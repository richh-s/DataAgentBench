code = """import json
import re

# Read files
with open('/tmp/tmp2d2u8k1a.json') as f:
    civic_docs = json.load(f)

with open('/tmp/tmp0k5s9q8h.json') as f:
    funding_data = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_data:
    funding_map[rec.get('Project_Name', '')] = int(rec.get('Amount', 0))

# Find disaster projects starting in 2022
total = 0
disaster = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for disaster project indicators
        if '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line:
            
            # Find start date
            start_date = ''
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                if 'st:' in next_line.lower() or 'start:' in next_line.lower():
                    start_date = next_line
                    break
            
            # Check if started in 2022
            if '2022' in start_date:
                amount = funding_map.get(line, 0)
                if amount > 0:
                    total += amount
                    disaster.append({'name': line, 'funding': amount})

result = {'total_funding': total, 'project_count': len(disaster), 'projects': disaster}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
