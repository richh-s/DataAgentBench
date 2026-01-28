code = """import json

with open('var_function-call-12694910972065598501.json') as f:
    funding_data = json.load(f)

high_funding_names = set()
for row in funding_data:
    try:
        amt = float(row['Amount'])
        if amt > 50000:
            high_funding_names.add(row['Project_Name'].strip())
    except:
        pass

with open('var_function-call-14720826093064389612.json') as f:
    docs = json.load(f)

found_projects = set()

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    start_idx = -1
    for i, line in enumerate(lines):
        if 'Capital Improvement Projects (Design)' in line:
            start_idx = i
            break
            
    if start_idx != -1:
        section_lines = []
        for i in range(start_idx + 1, len(lines)):
            line = lines[i].strip()
            if 'Capital Improvement Projects (' in line or 'Disaster Recovery Projects' in line:
                break
            section_lines.append(line)
            
        current_candidate = None
        for line in section_lines:
            if not line:
                continue
            
            is_metadata = False
            if '(cid:' in line: is_metadata = True
            if 'Updates:' in line: is_metadata = True
            if 'Project Schedule' in line: is_metadata = True
            if 'Estimated Schedule' in line: is_metadata = True
            if 'Project Description' in line: is_metadata = True
            if 'Recommended Action' in line: is_metadata = True
            
            if line.startswith('Page ') or line.startswith('Agenda Item'):
                continue
                
            if is_metadata:
                if current_candidate:
                    name = current_candidate.strip()
                    if len(name) > 3:
                        found_projects.add(name)
                    current_candidate = None
            else:
                current_candidate = line

matches = []
for proj in found_projects:
    if proj in high_funding_names:
        matches.append(proj)

print('__RESULT__:')
print(json.dumps({'count': len(matches), 'matches': matches, 'debug_found': list(found_projects)}))"""

env_args = {'var_function-call-12694910972065598501': 'file_storage/function-call-12694910972065598501.json', 'var_function-call-12694910972065599408': 'file_storage/function-call-12694910972065599408.json', 'var_function-call-14720826093064389612': 'file_storage/function-call-14720826093064389612.json'}

exec(code, env_args)
