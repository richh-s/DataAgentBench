code = """import json

# Access the data from previous query results
# The storage keys should be available in locals()

# Get funded projects data
funding_result = locals()['var_functions.query_db:120']
civic_result = locals()['var_functions.query_db:121']

print('Funding result type:', type(funding_result))
print('Civic result type:', type(civic_result))

# If they're file paths, load them
if isinstance(funding_result, str) and '.json' in funding_result:
    with open(funding_result) as f:
        funding_data = json.load(f)
    print('Loaded funding data from file, count:', len(funding_data))
else:
    funding_data = funding_result
    print('Funding data is direct, count:', len(funding_data))

if isinstance(civic_result, str) and '.json' in civic_result:
    with open(civic_result) as f:
        civic_docs = json.load(f)
    print('Loaded civic docs from file, count:', len(civic_docs))
else:
    civic_docs = civic_result
    print('Civic docs is direct, count:', len(civic_docs))

# Now process the data to answer the question
# Extract capital projects with design status
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    dpos = text.find('Capital Improvement Projects (Design)')
    if dpos < 0:
        continue
    
    # Get section boundaries
    after = text[dpos:]
    end = len(after)
    
    markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']
    for m in markers:
        pos = after.find(m)
        if pos > 0 and pos < end:
            end = pos
    
    section = after[:end]
    
    # Extract project names
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or ':' in line or 'cid:' in line:
            continue
        if 'Updates' in line or 'Schedule' in line or 'Design' in line:
            continue
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = ''.join(c for c in line if c.isalnum() or c.isspace()).strip()
            if clean and len(clean) > 5:
                design_projects.append(clean)

# Remove duplicates
design_projects = list(set(design_projects))

# Get funded project names
funded_names = [item['Project_Name'] for item in funding_data]

# Count matches
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    proj_words = set(proj_lower.split())
    if len(proj_words) < 2:
        continue
    
    for fund in funded_names:
        fund_lower = fund.lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            count += 1
            break
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            count += 1
            break

print('Final answer:', count)
result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:51': 'file_storage/functions.query_db:51.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.list_db:90': ['Funding'], 'var_functions.list_db:91': ['civic_docs'], 'var_functions.execute_python:96': {'funding_count': 276, 'civic_count': 5}, 'var_functions.query_db:102': [{'count': '276'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.query_db:107': 'file_storage/functions.query_db:107.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.query_db:111': 'file_storage/functions.query_db:111.json', 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json', 'var_functions.query_db:116': 'file_storage/functions.query_db:116.json', 'var_functions.query_db:117': 'file_storage/functions.query_db:117.json', 'var_functions.query_db:120': 'file_storage/functions.query_db:120.json', 'var_functions.query_db:121': 'file_storage/functions.query_db:121.json', 'var_functions.execute_python:130': {'status': 'checked'}}

exec(code, env_args)
