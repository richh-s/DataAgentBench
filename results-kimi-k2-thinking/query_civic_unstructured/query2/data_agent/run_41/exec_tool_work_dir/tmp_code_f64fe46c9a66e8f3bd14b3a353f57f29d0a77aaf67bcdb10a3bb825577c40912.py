code = """import json

# Load data from storage
civic_docs_raw = locals()['var_functions.query_db:2']
funding_raw = locals()['var_functions.query_db:5']

# Load civic documents
if isinstance(civic_docs_raw, str) and civic_docs_raw.endswith('.json'):
    with open(civic_docs_raw, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_raw

print('Documents:', len(civic_docs))

# Extract park projects completed in 2022
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        skip_terms = ['Public Works', 'Commission', 'Agenda', 'Page', 'Item']
        if any(term in line for term in skip_terms):
            continue
        
        # Check for project keywords
        if any(word in line.lower() for word in ['project', 'improvements', 'repairs']):
            # Look for 2022 completion
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if '2022' in next_line and 'complete' in next_line.lower():
                    # Check context for park
                    context = ' '.join(lines[max(0,i-3):min(len(lines),i+8)]).lower()
                    if 'park' in context or 'walkway' in context or 'shade' in context:
                        projects.append(line)
                        break

# Remove duplicates
unique = list(dict.fromkeys(projects))
print('Park projects:', len(unique))

# Load funding
if isinstance(funding_raw, str) and funding_raw.endswith('.json'):
    with open(funding_raw, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_raw

# Calculate total funding
total_funding = 0
matched = []

project_names = [p['Project_Name'] for p in funding]
for proj in unique:
    for i, fund_name in enumerate(project_names):
        if proj == fund_name or proj in fund_name or fund_name in proj:
            amount = int(funding[i]['Amount'])
            total_funding += amount
            matched.append({'project': proj, 'funding': fund_name, 'amount': amount})
            break

result = {}
result['total_funding'] = total_funding
result['matched_projects'] = matched
result['project_count'] = len(unique)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
