code = """import json
import re

# Load funding data
funding_result = var_functions.query_db:1
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic documents
civic_result = var_functions.query_db:2
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Extract design projects
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design = ''
    start = text.find('Capital Improvement Projects (Design)')
    if start >= 0:
        after = text[start:]
        end = after.find('Capital Improvement Projects (Construction)')
        if end < 0:
            end = after.find('Capital Improvement Projects (Not Started)')
        if end < 0:
            end = after.find('Disaster Recovery Projects')
        if end < 0:
            end = len(after)
        design = after[:end]
    
    # Extract names
    lines = design.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line == '-' or 'cid:' in line:
            continue
        skip_terms = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Begin Construction']
        if any(term in line for term in skip_terms):
            continue
        if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
            clean = re.sub('[^A-Za-z0-9\s]', '', line)
            clean = clean.strip()
            if clean:
                projects.append(clean)

# Remove duplicates
projects = list(set(projects))

# Match with funding
funding_names = [f['Project_Name'] for f in funding_data]
matches = []

for proj in projects:
    proj_lower = proj.lower()
    for fund in funding_names:
        fund_lower = fund.lower()
        if proj in fund or fund in proj:
            matches.append(proj)
            break
        proj_words = set(proj_lower.split())
        fund_words = set(fund_lower.split())
        if len(proj_words & fund_words) >= 3:
            matches.append(proj)
            break

count = len(matches)

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
