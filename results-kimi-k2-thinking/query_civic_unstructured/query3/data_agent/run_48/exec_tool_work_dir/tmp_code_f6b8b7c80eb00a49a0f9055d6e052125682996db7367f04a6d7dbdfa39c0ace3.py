code = """import json

# Load data
with open(locals()['var_functions.query_db:2'], 'r') as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:0'], 'r') as f:
    docs = json.load(f)

# Filter FEMA/emergency projects
fema = []
for r in funding:
    n = r['Project_Name']
    if 'FEMA' in n or 'fema' in n or 'emergency' in n.lower():
        fema.append({'Project_Name': n, 'Funding_Source': r['Funding_Source'], 'Amount': int(r['Amount'])})

# Extract status
status = []
for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
        low = line.lower()
        if 'project' in low or 'repairs' in low or 'sirens' in low:
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
                status.append({'name': line, 'status': st})

# Match
results = []
for p in fema:
    s = 'Unknown'
    for stat in status:
        pn = p['Project_Name'].lower()
        sn = stat['name'].lower()
        if pn in sn or sn in pn:
            s = stat['status']
            break
    results.append({'Project_Name': p['Project_Name'], 'Funding_Source': p['Funding_Source'], 'Amount': p['Amount'], 'Status': s})

# Output
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
