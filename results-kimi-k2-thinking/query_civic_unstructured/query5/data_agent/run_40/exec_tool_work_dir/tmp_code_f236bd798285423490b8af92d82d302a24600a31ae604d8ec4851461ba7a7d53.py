code = """import json

# Load civic documents
f = open('/tmp/tmp2d2u8k1a.json', 'r')
civic_docs = json.load(f)
f.close()

# Load funding data
f = open('/tmp/tmp0k5s9q8h.json', 'r')
funding_data = json.load(f)
f.close()

# Create funding map
funding_map = {}
for rec in funding_data:
    project_name = rec.get('Project_Name', '')
    if project_name:
        funding_map[project_name] = int(rec.get('Amount', 0))

# Find disaster projects starting in 2022
total_funding = 0
disaster_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check for disaster project indicators
        if '(FEMA Project)' in line or '(CalJPIA Project)' in line or '(CalOES Project)' in line or 'FEMA/CalOES Project' in line:
            # Check if there's a 2022 start date in nearby lines
            found_2022 = False
            for j in range(max(0, i-3), min(len(lines), i+8)):
                nearby_line = lines[j].strip()
                if '2022' in nearby_line and ('st:' in nearby_line.lower() or 'start:' in nearby_line.lower()):
                    found_2022 = True
                    break
            
            if found_2022:
                amount = funding_map.get(line, 0)
                if amount > 0:
                    total_funding += amount
                    disaster_projects.append({
                        'name': line,
                        'funding': amount
                    })

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': len(disaster_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
