code = """import json

# Load files
f1 = open('/tmp/tmprp5f5z5k.json', 'r')
 civic_docs = json.load(f1)
 f1.close()

f2 = open('/tmp/tmp0k5s9q8h.json', 'r')
 funding_data = json.load(f2)
 f2.close()

# Create funding map
 funding_map = {}
 for rec in funding_data:
     name = rec.get('Project_Name', '')
     if name:
         funding_map[name] = int(rec.get('Amount', 0))

# Find disaster projects with 2022 start
total = 0
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check disaster indicators
        is_disaster = False
        if line.find('(FEMA Project)') != -1: is_disaster = True
        if line.find('(CalJPIA Project)') != -1: is_disaster = True
        if line.find('(CalOES Project)') != -1: is_disaster = True
        if line.find('FEMA/CalOES Project') != -1: is_disaster = True
        
        if is_disaster:
            # Look for 2022 in nearby lines
            found_2022 = False
            start = max(0, i-2)
            end = min(len(lines), i+6)
            for j in range(start, end):
                if lines[j].find('2022') != -1 and ('st:' in lines[j].lower() or 'start:' in lines[j].lower()):
                    found_2022 = True
                    break
            
            if found_2022:
                amount = funding_map.get(line, 0)
                if amount > 0:
                    total += amount
                    projects.append({'name': line, 'funding': amount})

result = {'total_funding': total, 'project_count': len(projects), 'projects': projects}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
