code = """import json

# keys
key_docs = 'var_function-call-12716671968640832607'
key_fund = 'var_function-call-12716671968640831510'

# Load
with open(locals()[key_docs], 'r') as f:
    civic_docs = json.load(f)
text = civic_docs[0]['text']

with open(locals()[key_fund], 'r') as f:
    funding_data = json.load(f)
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Split lines
lines = text.split(chr(10))
projects = []
current_project = None
buffer_text = []

def is_marker(line):
    s = line.strip()
    if '(cid:190)' in s: return True
    if chr(190) in s: return True
    return False

for i, line in enumerate(lines):
    if is_marker(line):
        s = line.strip()
        prev_idx = i - 1
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
            
        if prev_idx >= 0:
            potential_name = lines[prev_idx].strip()
            
            ignore = False
            if is_marker(potential_name): ignore = True
            if "Agenda Item" in potential_name: ignore = True
            if "Page " in potential_name and " of " in potential_name: ignore = True
            if "Capital Improvement Projects" in potential_name: ignore = True
            
            if not ignore:
                if current_project:
                    projects.append({'name': current_project, 'text': chr(10).join(buffer_text)})
                current_project = potential_name
                buffer_text = []

    if current_project:
        buffer_text.append(line)

if current_project:
    projects.append({'name': current_project, 'text': chr(10).join(buffer_text)})

# Find all completed in 2022
completed_2022 = []
for p in projects:
    name = p['name']
    details = p['text']
    
    for l in details.split(chr(10)):
        l_lower = l.lower()
        if 'completed' in l_lower and '2022' in l_lower:
            # check context
            if "complete design" in l_lower: continue
            
            completed_2022.append({'name': name, 'line': l.strip()})
            break

print("__RESULT__:")
print(json.dumps(completed_2022))"""

env_args = {'var_function-call-12716671968640832607': 'file_storage/function-call-12716671968640832607.json', 'var_function-call-12716671968640831510': 'file_storage/function-call-12716671968640831510.json', 'var_function-call-6699042011993104825': {'target_projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}], 'total_funding': 21000}, 'var_function-call-2665130666355777402': {'target_projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}], 'total_funding': 21000}}

exec(code, env_args)
