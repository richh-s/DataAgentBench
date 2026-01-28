code = """import json

# Access stored data
civic_docs_key = 'var_functions.query_db:2'
funding_key = 'var_functions.query_db:5'

civic_docs_data = locals()[civic_docs_key]
funding_data = locals()[funding_key]

# Load civic documents
if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    with open(civic_docs_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_data

print('Loaded ' + str(len(civic_docs)) + ' documents')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for 2022 completion mentions with park context
    if '2022' in text and 'complete' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
            
            # Skip headers
            if line.startswith('Public Works') or line.startswith('Commission') or line.startswith('Agenda'):
                continue
            
            # Find project names
            if any(word in line.lower() for word in ['project', 'improvements', 'repairs', 'replacement']):
                # Look for completion in 2022 nearby
                for j in range(i+1, min(i+8, len(lines))):
                    next_line = lines[j].strip()
                    if '2022' in next_line and 'complete' in next_line.lower():
                        # Check if park-related
                        context = ' '.join(lines[max(0,i-3):min(len(lines),i+6)]).lower()
                        if 'park' in context or 'walkway' in context or 'shade' in context:
                            park_projects.append(line)
                            break
                
# Remove duplicates
unique_projects = list(dict.fromkeys(park_projects))
print('Found ' + str(len(unique_projects)) + ' park projects')

# Load funding data
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_data

# Match with funding and sum
total = 0
matches = []

for proj in unique_projects:
    for fund in funding:
        fund_name = fund['Project_Name']
        if proj == fund_name or proj in fund_name or fund_name in proj:
            amount = int(fund['Amount'])
            total += amount
            matches.append({'project': proj, 'funding': fund_name, 'amount': amount})
            break

print('Total funding: ' + str(total))
result = json.dumps({'total_funding': total, 'matches': matches, 'project_count': len(unique_projects)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
