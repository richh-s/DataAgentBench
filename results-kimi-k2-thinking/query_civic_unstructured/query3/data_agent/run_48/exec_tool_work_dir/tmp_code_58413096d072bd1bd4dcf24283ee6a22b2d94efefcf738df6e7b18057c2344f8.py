code = """import json

funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:0']

funding_list = []
civic_list = []

with open(funding_path, 'r') as f:
    funding_list = json.load(f)
with open(civic_path, 'r') as f:
    civic_list = json.load(f)

# Find FEMA/emergency projects
fema_proj = []
for rec in funding_list:
    name = rec['Project_Name']
    lower = name.lower()
    if 'fema' in lower or 'emergency' in lower:
        fema_proj.append({
            'Project_Name': name,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

# Extract status from documents
status_list = []
for doc in civic_list:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
        low = line.lower()
        if 'project' in low or 'repairs' in low or 'sirens' in low or 'warning' in low:
            st = None
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'design' in nxt and 'committee' not in nxt:
                    st = 'design'
                    break
                if 'completed' in nxt or 'completion' in nxt:
                    st = 'completed'
                    break
                if 'not started' in nxt:
                    st = 'not started'
                    break
            if st:
                status_list.append({'name': line, 'status': st})

# Compile results
output = []
for proj in fema_proj:
    s = 'Unknown'
    proj_lower = proj['Project_Name'].lower()
    for st in status_list:
        st_lower = st['name'].lower()
        if proj_lower in st_lower or st_lower in proj_lower:
            s = st['status']
            break
    output.append({'Project_Name': proj['Project_Name'], 'Funding_Source': proj['Funding_Source'], 'Amount': proj['Amount'], 'Status': s})

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
