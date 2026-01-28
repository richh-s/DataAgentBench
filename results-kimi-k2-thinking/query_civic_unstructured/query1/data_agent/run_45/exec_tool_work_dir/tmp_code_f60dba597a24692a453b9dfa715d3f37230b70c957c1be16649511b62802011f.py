code = """import json, re, os

# Load funding data
with open(var_functions.query_db:2, 'r') as f:
    funding = json.load(f)

# Load civic documents
with open(var_functions.query_db:6, 'r') as f:
    civic = json.load(f)

# Build funding map for projects > 50000
fund = {}
for item in funding:
    amt = float(item['Amount'])
    if amt > 50000:
        name = item['Project_Name']
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        fund[name] = amt
        fund[clean] = amt

# Extract capital design projects
design = set()
for doc in civic:
    txt = doc.get('text', '')
    design_mode = False
    for line in txt.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            design_mode = True
        elif 'Capital Improvement Projects (Construction)' in line:
            design_mode = False
        if design_mode and line and len(line) > 15:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line and 'fire' not in line:
                meta = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA', 'UPDATES:', 'SCHEDULE:', 'Capital Improvement Projects']
                if not any(word in line.upper() for word in meta):
                    if not line.startswith('('):
                        design.add(line)

count = 0
for p in design:
    pc = re.sub(r'\s*\([^)]*\)\s*$', '', p).strip()
    if p in fund or pc in fund:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
