code = """import json

# Load funding
f_file = var_functions.query_db:4
with open(f_file) as f:
    funding = json.load(f)

# Load civic docs
c_file = var_functions.query_db:28
with open(c_file) as f:
    docs = json.load(f)

# Get funding > 50000
high_fund = []
for item in funding:
    if item.get('Amount'):
        try:
            amt = int(item['Amount'])
            if amt > 50000:
                high_fund.append(item)
        except:
            pass

# Get design project names from docs
design_names = []
for doc in docs:
    text = doc.get('text', '')
    idx = text.lower().find('projects (design)')
    if idx > 0:
        section = text[idx:idx+3000]
        end_pos = len(section)
        for marker in ['projects (construction)', 'disaster recovery']:
            pos = section.lower().find(marker)
            if pos > 0:
                end_pos = min(end_pos, pos)
        
        design_section = section[:end_pos]
        lines = design_section.split('\n')
        
        for i in range(len(lines)):
            line = lines[i].strip()
            if len(line) < 6:
                continue
            lower = line.lower()
            if any(x in lower for x in ['capital improvement', 'design', 'updates:', 'project schedule']):
                continue
            if i + 1 < len(lines):
                next_line = lines[i+1].lower()
                if 'updates:' in next_line or 'project schedule' in next_line:
                    clean = line.lstrip('0123456789.-•')
                    if len(clean) > 8:
                        design_names.append(clean)

# Match
matches = set()
for design in design_names:
    d_lower = design.lower()
    for fund in high_fund:
        f_lower = fund['Project_Name'].lower()
        if d_lower in f_lower or f_lower in d_lower:
            matches.add(design)
            break

result = {'count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
