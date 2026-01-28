code = """import json

fund_file = var_functions.query_db:58
civic_file = var_functions.query_db:59

with open(fund_file) as f:
    funding = json.load(f)
with open(civic_file) as f:
    docs = json.load(f)

funded = [f['Project_Name'] for f in funding]

# Extract from text
design_section = ''
for doc in docs:
    t = doc.get('text', '')
    dpos = t.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
    section = t[dpos:]
    end = len(section)
    for m in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        p = section.find(m)
        if p > 0 and p < end:
            end = p
    design_section += section[:end]

# Extract projects using line parsing
projects = []
for line in design_section.splitlines():
    line = line.strip()
    if len(line) < 10:
        continue
    if line.startswith('('):
        continue
    if ':' in line or 'cid:' in line:
        continue
    if 'Updates' in line or 'Schedule' in line or 'Design' in line:
        continue
    if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
        clean = ''.join(c for c in line if c.isalnum() or c.isspace()).strip()
        if clean and len(clean) > 5:
            projects.append(clean)

projects = list(set(projects))

# Count matches
count = 0
for proj in projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    for fund in funded:
        fund_lower = fund.lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            break
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json'}

exec(code, env_args)
