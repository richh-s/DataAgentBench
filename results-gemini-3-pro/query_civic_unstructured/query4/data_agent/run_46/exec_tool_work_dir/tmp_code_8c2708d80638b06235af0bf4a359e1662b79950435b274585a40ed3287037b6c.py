code = """import json

# Load data
with open(locals()['var_function-call-10071465858978758167'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-10071465858978756684'], 'r') as f:
    funding_data = json.load(f)

# Build Funding Lookup
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip()
    try:
        amount = int(item['Amount'])
    except:
        amount = 0
    funding_map[name] = amount
    funding_map[name.lower()] = amount

projects_found = {}

def check_spring_2022(text):
    t = text.lower()
    if '2022' not in t:
        return False
    # keywords
    if 'spring' in t: return True
    if 'march' in t: return True
    if 'april' in t: return True
    if 'may' in t: return True
    return False

# Scan documents
for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    current_project = None
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        # Identify Project Name
        if line.lower() in funding_map:
            current_project = line.strip()
        elif len(line) > 5 and not line.startswith('(') and 'Agenda' not in line and 'Page' not in line:
            # Heuristic lookahead
            if i+1 < len(lines):
                next_l = lines[i+1].strip()
                if 'Updates:' in next_l or 'Project Schedule' in next_l or 'Project Description' in next_l:
                    current_project = line.strip()
        
        if current_project:
            l_low = line.lower()
            # Look for Start Date
            # "Begin Construction" or "Start"
            if 'begin construction' in l_low or 'start' in l_low:
                if check_spring_2022(line):
                    projects_found[current_project] = line
            
            # Check next line
            if 'begin construction' in l_low and ':' in line and not any(c.isdigit() for c in line):
                 if i+1 < len(lines):
                     next_l = lines[i+1].strip()
                     if check_spring_2022(next_l):
                         projects_found[current_project] = next_l

# Match and Total
matched_projects = []
total_funding = 0
seen_projects = set()

for proj_name, context in projects_found.items():
    norm_name = ' '.join(proj_name.split())
    
    amt = funding_map.get(norm_name)
    if not amt:
        amt = funding_map.get(norm_name.lower())
    
    if amt is not None:
        if norm_name not in seen_projects:
            matched_projects.append({'name': norm_name, 'amount': amt})
            total_funding += amt
            seen_projects.add(norm_name)

print('__RESULT__:')
print(json.dumps({'count': len(matched_projects), 'total_funding': total_funding, 'projects': matched_projects}))"""

env_args = {'var_function-call-600716714873686583': ['Funding'], 'var_function-call-600716714873684502': 'file_storage/function-call-600716714873684502.json', 'var_function-call-10071465858978756684': 'file_storage/function-call-10071465858978756684.json', 'var_function-call-10071465858978758167': 'file_storage/function-call-10071465858978758167.json'}

exec(code, env_args)
